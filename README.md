# 🌙 SleepWatch ALERT 🚼  
**Your Baby's Safety, Simplified.**  

### 💡 **Project Overview**  
SleepWatch ALERT is a free, user-friendly solution to monitor your baby. Designed for families without access to costly baby surveillance systems, this tool offers peace of mind by detecting if your baby is awake or asleep. It’s lightweight, efficient, and optimized to run on low-resource computers.  

![Interface Screenshot](https://i.ibb.co/jLNTdhg/Screenshot.png)  

---

### 🌟 **Why SleepWatch ALERT?**  
- 🍼 **Affordable and Accessible**: No need for expensive equipment.  
- ⚡ **Fast and Reliable**: Real-time baby monitoring with minimal delay.  
- 💻 **Easy Setup**: Works locally on your computer with simple instructions.  
- 📳 **Smart Alerts**: Sends notifications via SMS or your smartwatch when your baby wakes up.

---

### 🛠 **How It Works**  

1. **Eye Detection with AI** 👀  
   Using MediaPipe Face Mesh, SleepWatch ALERT precisely detects your baby’s eye status, avoiding false positives from objects like blankets or clothing.  
   - **Result**: Reliable real-time detection of "ASLEEP" or "AWAKE."  

2. **Instant Alerts** 📲  
   Powered by the **Twilio API**, SleepWatch ALERT sends SMS notifications to your phone or smartwatch the moment your baby wakes up.  

3. **Web-Based Convenience** 🌐  
   - Securely access the tool from any device within your local network.  
   - HTTPS ensures safe and reliable camera activation.  

![Alert Screenshot](https://i.ibb.co/X3sSc80/Screenshot-1.png)  

---

### 🚀 **Setup Instructions**  
1. Clone the repository from GitHub: [**SleepWatch ALERT Repository**](https://github.com/Josue049/SleepWatchAlert).  
2. Set up a virtual environment and install the dependencies listed in `requirements.txt`.  
3. Use **OpenSSL** to create a certificate and save it in the `cert` folder.  
4. Run `app.py` and access the displayed port.  
5. Create a Twilio account for SMS alerts.  
6. Register, log in, and start monitoring!

---

### 🧪 **Tech Behind SleepWatch ALERT**  
- **MediaPipe Face Mesh**: Tracks facial landmarks for precise eye detection.  
- **Python + OpenCV**: Optimized for real-time image processing.  
- **Twilio API**: Handles instant SMS notifications.  
- **Flask**: Powers the user-friendly web interface.  

---

### 🎯 **Features at a Glance**  

| Feature                     | Description                                   |  
|-----------------------------|-----------------------------------------------|  
| **Eye Detection**           | Reliable AI-based tracking of open/closed eyes. |  
| **Real-Time Notifications** | Alerts via SMS or smartwatch vibrations.      |  
| **Web Access**              | Local, secure access through a browser.       |  
| **Lightweight**             | Runs smoothly on low-resource devices.        |  
| **Customizable**            | Compatible with different user setups.        |  

---

### 🍼 **Inspiration from Real Life**  
SleepWatch ALERT was born out of necessity. My family used video calls to monitor my niece, but this method was prone to distractions and delays. This project aims to eliminate these issues, giving parents a reliable, automated way to ensure their baby's safety.  

---

### 🌍 **Future Potential**  
The project is designed with scalability in mind. With further development, it can evolve into a universally accessible tool that ensures baby safety worldwide.  

![Result Screenshot](https://i.ibb.co/NVcsPm6/Screenshot-2.png)  

---

### 💪 **Built with Love**  
SleepWatch ALERT began as my final project for **Harvard CS50** in 2023. It has since evolved into version 2.0, refined for real-world applications.  

👉 **Ready to give it a try? Download now and experience peace of mind!**  
[**GitHub Repository**](https://github.com/Josue049/SleepWatchAlert)  

---  

💤 **SleepWatch ALERT**: Because every parent deserves a good night's sleep.
