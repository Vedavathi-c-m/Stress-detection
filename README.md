# 🚨 Automatic Detection and Analysis of Stress Related Posts

## 📌 Project Summary

This project presents an innovative system designed to detect and analyze stress levels in individuals by combining physiological signal monitoring and facial emotion recognition. The core objective is to develop a reliable, real-time, and non-intrusive solution that leverages embedded systems and machine learning to identify stress and provide timely alerts to concerned parties. As mental health becomes an increasingly critical concern in today’s fast-paced world, early detection of stress can contribute significantly to well-being and preventive care.

The system utilizes **IoT-based hardware** comprising sensors such as the heartbeat sensor (TCRT1000), sweat sensor (FC-37), and temperature sensor (DS18B20), all interfaced with an Arduino Uno microcontroller. These sensors continuously collect data such as heart rate, perspiration levels, and body temperature. Once collected, the data is evaluated against predefined threshold values. If these thresholds are exceeded, indicating a potential stress response, the system activates a buzzer and displays an alert on an LCD screen. Simultaneously, a camera captures the user’s facial image.

On the software front, **OpenCV**, an open-source computer vision library, is employed to process the facial image. A **Convolutional Neural Network (CNN)** is then used to analyze facial expressions and detect emotional states associated with stress, such as anger, sadness, or anxiety. If the system confirms a stress condition both physiologically and emotionally, it sends a **notification via Telegram** to a designated individual, such as a caregiver, family member, or supervisor, ensuring timely support and intervention.

---

## 🛠 Key Technologies

- **Hardware:**
  - Arduino Uno
  - Heartbeat Sensor (TCRT1000)
  - Temperature Sensor (DS18B20)
  - Sweat Sensor (FC-37)
  - LCD Display
  - Buzzer

- **Software:**
  - Arduino IDE (Embedded C)
  - Python
  - OpenCV
  - Convolutional Neural Network (CNN)
  - Telegram API (for notification)

---

## ⚙️ Working Flow

1. Collect physiological data (heart rate, sweat, temperature).
2. Compare data against threshold values.
3. Trigger alert (buzzer & LCD) and activate the camera.
4. Use CNN to analyze the captured facial image for stress indicators.
5. Send a stress alert to designated contacts via Telegram.

---

## 📱 Applications

- Real-time mental health monitoring
- Workplace stress detection
- Preventive healthcare systems
- Student wellness programs

---

## ✅ Advantages

- Non-intrusive, continuous monitoring
- Combines physical sensor data and facial emotion analysis
- Scalable and cost-effective solution
- Promotes mental health awareness

---

## 🔮 Future Scope

- Improve accuracy with deeper learning models
- Expand emotion dataset for better classification
- Integrate mobile app for remote monitoring
- Add cloud-based analytics for stress trends and predictions

---

## 📷 Demo & Screenshots

*(Add demo images or a video/GIF here if available)*

---

## 🤝 Contributors

- Sindhu H S – 1EW21EC124  
- Srinidhi Deshpande – 1EW21EC128  
- Varsha N T – 1EW21EC139  
- Vedavathi C M – 1EW21EC140  
- **Guide:** Prof. Dhanyashree P N, Dept. of ECE, EWIT, Bengaluru

---

## 📄 License

This project is developed for academic purposes. Please check with the authors before using in commercial applications.

---

