# **SleepWatch ALERT 2.0** 🚼💤  
**Revolutionizing Baby Monitoring for Every Family**

---

### **🌟 A Free and Accessible Baby Monitoring Solution**  

**Why SleepWatch ALERT?**  
Not every family can afford specialized baby monitoring cameras. **SleepWatch ALERT** is a **lightweight, AI-driven solution** designed to run on low-resource computers, empowering parents to ensure their baby's well-being without breaking the bank.  

With just a local computer and a smartphone, parents can now:  
- Monitor their baby’s sleep status in real time.  
- Receive instant **SMS alerts** when the baby wakes up.  
- Optionally, get notified via **smartwatch vibrations** for a seamless experience.  

---

### **🚀 How Does It Work?**

1. **Web-Based Interface** 🌐  
   Parents access a simple web page to activate the camera and monitor their baby.  
   
2. **AI Eye Detection** 👀  
   - Leveraging **MediaPipe Face Mesh**, the system identifies if the baby’s eyes are open or closed with unparalleled accuracy.  
   - Eliminates false positives caused by objects like blankets or clothing.  

3. **Instant Notifications** 📱  
   - The **Twilio API** ensures reliable SMS delivery to notify parents instantly.  

4. **Optimized Performance** ⚡  
   - Eye detection is performed on the server side with a unique, efficient method of sending and analyzing frames.  

---

### **🎯 Key Features**

✅ **Accurate Eye Tracking**  
   - Uses advanced algorithms to determine sleep states.  

✅ **Instant Alerts**  
   - Notifies parents as soon as the baby wakes up.  

✅ **Resource Efficient**  
   - Designed for low-end computers to make it universally accessible.  

✅ **Secure Local Usage**  
   - HTTPS support ensures privacy and security within your home network.  

✅ **Family-Friendly Setup**  
   - Easy installation with clear instructions for parents of all tech skill levels.  

---

### **📖 Step-by-Step Installation**

1. **Clone the Repository**  
   Grab the code from GitHub:  
   👉 [SleepWatch ALERT GitHub Repository](https://github.com/Josue049/SleepWatchAlert)  

2. **Set Up the Environment**  
   - Install dependencies via `requirements.txt`.  
   - Use **OpenSSL** to generate the required certificate for HTTPS.  

3. **Run the Program**  
   - Launch the `app.py` file and access the interface using the provided port.  

4. **Start Monitoring**  
   - Create an account, log in, and let SleepWatch ALERT handle the rest!  

---

### **💡 Inspiration**  

The idea came from a **real-life challenge**: monitoring my niece during video calls. While effective, it had limitations:  
- Constant supervision required.  
- Risk of distractions.  

SleepWatch ALERT eliminates these problems by automating monitoring and notifications.  

---

### **🔬 The Science Behind It**

**MediaPipe Face Mesh & Eye Aspect Ratio (EAR)**  
Thanks to insights from research and tutorials, SleepWatch ALERT implements a precise algorithm to track the **eye aspect ratio**, identifying whether the baby is awake or asleep.  

**Efficient Frame Handling**  
The solution uploads a single frame per second to the server, reducing latency and resource usage.  

---

### **📷 Screenshots**

![Main Interface](https://i.ibb.co/jLNTdhg/Screenshot.png)  
![Eye Detection in Action](https://i.ibb.co/X3sSc80/Screenshot-1.png)  
![Notification Alert](https://i.ibb.co/NVcsPm6/Screenshot-2.png)  

---

### **👶 SleepWatch ALERT: Your Baby's Guardian Angel**

Originally developed as my **CS50 Final Project** at Harvard, this project has evolved into a robust, user-friendly tool for families everywhere. **Join me in making baby monitoring smarter, simpler, and accessible for everyone!**  

🚼 **Turn on. Log in. Relax.**  

👉 Try it now: [GitHub Repository](https://github.com/Josue049/SleepWatchAlert)
