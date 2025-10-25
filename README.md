# 🔐 Suspicious Login Alert

This project is a **Security-based Python Application** that detects **suspicious login attempts** based on the user's **login time** and **geographical location**.  
It is built using **Tkinter (for GUI)** and **Requests (for IP geolocation)**.

---

## 📌 Features
- 🧠 Simple GUI built with Tkinter  
- 🌍 Detects user's country and IP using `ipinfo.io`  
- ⏰ Alerts when login occurs from unusual time or country  
- 🚨 Shows warning message using popup alerts  
- 🧩 Easy to customize for college or security-based projects  

---

## 🧰 Technologies Used
| Component | Description |
|------------|-------------|
| **Python 3** | Main programming language |
| **Tkinter** | For GUI interface |
| **Requests** | To fetch IP & location details |
| **Datetime** | To check login time |

---

## ⚙️ How It Works
1. User enters **username** and **password**.  
2. The system checks if credentials are valid.  
3. It then fetches the **current IP and country** using `http://ipinfo.io`.  
4. If login occurs:
   - From a **different country**, or  
   - Outside the **normal working hours (7 AM - 1 PM)**  
   Then a **warning alert** is shown.  
5. Otherwise, it displays a **successful login** message.

---

## 📸 Project Interface
![App Screenshot](<![alt text](image.png)>)

---

## 🧪 Example Output
**Normal Login**
