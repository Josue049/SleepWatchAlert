import os
from functools import wraps
import base64
from PIL import Image
from io import BytesIO
from cs50 import SQL
from flask import (Flask, redirect, render_template, request, session, jsonify, make_response)
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import cv2
import mediapipe as mp
import numpy as np
from twilio.rest import Client
import sqlite3

mp_face_mesh = mp.solutions.face_mesh
index_left_eye = [33, 160, 158, 133, 153, 144]
index_right_eye = [362, 385, 387, 263, 373, 380]
EAR_THRESH = 0.20
NUM_FRAMES = 10
Frames_Dormido = 0
OJOS1 = ""
OJOS2 = ""
i = 0

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Si no existe, la creamos con sqlite3
if not os.path.exists("registros.db"):
    conn = sqlite3.connect("registros.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            user_baby TEXT NOT NULL,
            hash TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            twilio_number TEXT NOT NULL,
            account TEXT NOT NULL,
            token TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Ahora sí, conectamos con CS50
db = SQL("sqlite:///registros.db")

def apology(message, code=400):
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
        ("%", "~p"), ("#", "~h"), ("/", "~s"), ('\"', "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
@login_required
def index():
    try:
        base = db.execute("SELECT user_baby, phone_number FROM users WHERE id = (?)", session["user_id"])
        number = base[0]["phone_number"]
    except Exception as e:
        session.clear()
        return render_template("login.html")

    return render_template("index.html", number=number)

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Must provide username", 403)

        elif not request.form.get("password"):
            return apology("Must provide password", 403)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        print(rows)
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("username")
        name_baby = request.form.get("name_baby")
        phone_number = request.form.get("phone_number")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        account = request.form.get("account")
        token = request.form.get("token")
        twilio_number = request.form.get("twilio_number")

        if name == "" or name_baby == "" or phone_number == "" or password == "" or confirmation == "" or account == "" or token == "" or twilio_number == "":
            return apology("Complete your information", 400)
        
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
        password_matched = check_password_hash(hashed_password, confirmation)
        if password_matched:
            try:
                db.execute(
                    "INSERT INTO users (username, user_baby, hash, phone_number, twilio_number, account, token) VALUES ((?),(?),(?),(?),(?),(?),(?))", name, name_baby, hashed_password, phone_number, twilio_number, account, token)
                return render_template("login.html")
            except Exception as e:
                return make_response(
                    render_template("register.html", mostrar_alert=True), 400
                )
        else:
            return apology("Different passwords", 400)
        

    return render_template("register.html")

@app.route("/logout")
def logout():
    """Log user out"""
    try:
        os.remove(str(session["user_id"])+'nuevo_frame.jpg')
    except Exception as e:
        print("Unstored image")
    session.clear()
    return redirect("/")

@app.route('/get_frame', methods=['POST'])
def get_frame():
    global mp_face_mesh, index_left_eye, index_right_eye, EAR_THRESH, NUM_FRAMES, Frames_Dormido, OJOS1, OJOS2, i

    base = db.execute("SELECT user_baby, phone_number, twilio_number, account, token FROM users WHERE id = (?)", session["user_id"])
    number = base[0]["phone_number"]
    number = "+"+str(number)
    babyname = base[0]["user_baby"]
    babyname = "HAS WOKEN UP " + babyname
    account = base[0]["account"]
    token = base[0]["token"]
    twilio_number = base[0]["twilio_number"]
    twilio_number = "+"+str(twilio_number)

    client = Client(account, token)

    def eye_aspect_ratio(coordinates):
        A = np.linalg.norm(np.array(coordinates[1]) - np.array(coordinates[5]))
        B = np.linalg.norm(np.array(coordinates[2]) - np.array(coordinates[4]))
        C = np.linalg.norm(np.array(coordinates[0]) - np.array(coordinates[3]))
        return (A + B) / (2 * C)

    frame_data = request.form.get('frame')
    binary_data = base64.b64decode(frame_data.split(',')[1])
    new = Image.open(BytesIO(binary_data))
    new.save(str(session["user_id"])+'nuevo_frame.jpg')
    cap = cv2.VideoCapture(str(session["user_id"])+'nuevo_frame.jpg')

    with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1) as face_mesh:

        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            res = face_mesh.process(frame_rgb)

            coordinates_left_eye = []
            coordinates_right_eye = []

            if res.multi_face_landmarks is not None:
                for face in res.multi_face_landmarks:
                    for index in index_left_eye:
                            x = int(face.landmark[index].x * width)
                            y = int(face.landmark[index].y * height)
                            coordinates_left_eye.append([x, y])
                            cv2.circle(frame, (x, y), 2, (0, 255, 255), 1)
                            cv2.circle(frame, (x, y), 1, (128, 0, 250), 1)
                    for index in index_right_eye:
                            x = int(face.landmark[index].x * width)
                            y = int(face.landmark[index].y * height)
                            coordinates_right_eye.append([x, y])
                            cv2.circle(frame, (x, y), 2, (128, 0, 250), 1)
                            cv2.circle(frame, (x, y), 1, (0, 255, 255), 1)

                left = eye_aspect_ratio(coordinates_left_eye)
                right = eye_aspect_ratio(coordinates_right_eye)
                ear = (left + right)/2
                
                if ear < EAR_THRESH:
                    OJOS2 = OJOS1
                    Frames_Dormido += 1
                    if Frames_Dormido > NUM_FRAMES:
                        OJOS1 = "ASLEEP"
                        Frames_Dormido = 0
                elif ear > EAR_THRESH:
                    OJOS2 = OJOS1
                    OJOS1 = "AWAKE"
                else:
                    OJOS1="EYES NOT FOUND"
                if OJOS1 != OJOS2:
                    print(ear)
                    print(OJOS1)
                    if OJOS1 == "AWAKE" and i != 0:
                        client.messages.create(to=number, from_=twilio_number, body=babyname)

                i +=1
    cap.release()

    return jsonify({"message": "Frame received successfully"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)