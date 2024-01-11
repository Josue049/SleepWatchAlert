# SLEEPWATCH ALERT

#### Description:

Through this project, I seek to create a free alternative to baby video surveillance cameras. This was done thinking about families who do not have the financial resources to purchase a specialized camera. The goal is to provide easy and free access so that parents can monitor and ensure the well-being of their baby. Additionally, the project is designed to be lightweight and run smoothly on low-resource computers.

![Screenshot0](https://i.ibb.co/jLNTdhg/Screenshot.png)
![Screenshot1](https://i.ibb.co/X3sSc80/Screenshot-1.png)

At the moment the project is being planned so that a person can download it and run it on their computer locally.

It is a project with a lot of growth potential and in which I have put a lot of effort these days.


### USE
The project consists of creating a web page that the mother or father can access, activate the camera and, through artificial intelligence, detect the baby's eyes to verify if she is awake or still sleeping. If the baby wakes up, she will automatically send an SMS to the mother's phone, although ideally the mother will have a smart watch to feel the vibration on her arm when the SMS arrives.

To install and test the program, follow these steps:
1. Clone the project repository from GitHub: [SleepWatch Alert Repository]
https://github.com/Josue049/SleepWatchAlert
2. Create a virtual environment and install all the dependencies mentioned in the
`requirements.txt`
3. Download OpenSSL to create your license and key. Then, create a folder called "cert" and
place the files there.
4. Run the `app.py` file and enter the port shown in the terminal.
5. Register (you'll need a Twilio account to complete some fields), log in, and use the page as
normal.

### INSPIRATION FROM A REAL CASE
In my house we constantly make video calls to monitor my niece and notify her mother if she wakes up, and although it seems like a good solution, this can be subject to several inconveniences such as always having to ask someone else for help or simply having whoever is watching get distracted

### EYE DETECTION
The objective is to detect if the baby has its eyes open or closed. My first go was to use OpenCV with a Haarcascade for eye detection. Sometimes it worked well, but it also had a problem with false positives. Which could be problematic in a home environment where eyes could be detected on the baby's blanket or polo shirt. So after some searching I found a perfect solution: MediaPipe Face Mesh. Basically, it provides a mesh that covers the face, and by only using the points that form the eyes, we exponentially reduce errors, to the point that I haven't had any problems so far. To go deeper into the topic I found this page: [https://omes-va.com/contador-de-parpadeos-python-mediapipe-facemesh-opencv/](https://omes-va.com/contador -de -blinks-python-mediapipe-facemesh-opencv/) (Credits to the authors). This page talks about an article that explains an equation for measuring the aspect ratio between the eyes, as well as providing an example of practical use. The full article is here: [https://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf](https://vision.fe.uni-lj.si/cvww2016/proceedings/ articles/05.pdf). Thanks to these resources I was able to carry out this project. I implemented the equation mentioned in the article, performed frame-by-frame recognition in real time, marking "ASLEEP" or "AWAKE" on the console. And finally I eliminated the repetitions so that it only shows when going from one state to another.

### SEND AN SMS MESSAGE
The Twilio API is used with which SMS can be sent. Therefore, it is necessary for the user to create an account and fill out the necessary fields on the page to be able to use this service. Use of the API is not sponsored in any way and is only used for its efficiency.

### PUT IT ON A WEB PAGE
This was THE BIGGEST PROBLEM without a doubt and the most time consuming. I had to change my approach to the problem at least 5 times (if I don't forget any).

1. First, I had the idea to turn on the camera on the client, send it to the server and from the server send the image by applying eye recognition to the client. But this was extremely slow and, due to the nature of the project, it had to be as fast as possible so that the signal reached the mother practically instantly.

2. The next idea was to move the entire project to JavaScript with OpenCV.js and run detection on the client side. However, this would mean starting over from scratch, and OpenCV.js also had a bug that said you had to recompile OpenCV.js by changing a default configuration.

3. It occurred to me that if we removed the highlighting of the eyes so that they are not shown to the client, we could drastically reduce the wait times (so that the eye detection would be done on the server side and not reflected so that the client saw it). I tried running the program from my PC, but it was too slow. Despite everything, I kept the idea of ​​only doing eye detection on the server.

4. At some point, I even thought about doing a computer project, but since it was not practical for mother's use, I quickly discarded it.

5. It occurred to me that the frames were literally images or, rather, an image. The idea is simple: the camera turns on on the client side, takes the current image and sends it to the server every second (in my experience, doing it faster causes problems). The server receives the image "new_frame.jpg" and, with a loop, updates the image to the current frame, causing a single image "new_frame.jpg" to constantly change its content and constantly perform eye detection on it. It sounds confusing, but it works very well and is almost immediate. This idea was the definitive one as it worked and did not consume many resources with the creation of new images.

### LOCAL USE OF THE PROGRAM
I recommend using HTTPS, since activating the camera on the client side is not allowed when using HTTP. The best practice would be to use the program from a local network so that it can be accessed from a cell phone within the same house. To achieve this, HTTPS can be implemented with OPENSSL.

A certificate must be generated with OPENSSL and then copy the "server.cer" and "server.key" files to the "cert" folder.


## And finally, the sum of all this effort led to the creation of SleepWatch ALERT 2.0
The operation is simple: Turn on the server, enter the page, create an account, log in and READY! You can now focus on your baby and wait for an alert on your smart watch or cell phone by default.

![Screenshot2](https://i.ibb.co/NVcsPm6/Screenshot-2.png)

I originally created this project as my final project for Harvard CS50 in December 2023, but I refined it for release in competition in 2024. So it's a version 2.0 in spirit, but the first to be made public.
