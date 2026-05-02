# 📓 Aaj Kya Kiya - Digital Memory Board

A stunning, highly responsive Digital Memory Board built with **Streamlit**, **Tailwind CSS**, and **Firebase**. Capture your daily progress, stick memories, and organize your thoughts on a beautiful interactive board that feels like a physical fridge, but with cloud-powered persistence.

![Version](https://img.shields.io/badge/version-1.0.0-orange)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B)
![Firebase](https://img.shields.io/badge/Database-Firebase-FFCA28)

## ✨ Features

- **🚀 Instant Sticking**: Zero-latency note creation with optimistic UI updates.
- **🖼️ Smart Image Compression**: High-resolution photos are compressed instantly on the client side for lightning-fast saving.
- **🎨 Vibrant Aesthetics**: Beautifully colored sticky notes with rotating angles and realistic drop-shadows.
- **🔐 Personal Workspaces**: Isolated boards for every user—just enter your username and access your private memories.
- **💾 Real-time Persistence**: Powered by Firebase Firestore, ensuring your board looks exactly how you left it, even after a refresh.
- **📱 Responsive Design**: Works seamlessly across different screen sizes with a clean, modern sidebar for stats and navigation.

## 🛠️ Tech Stack

- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS (for premium styling).
- **Backend**: Python (Streamlit) acts as a secure shell for hosting and credential management.
- **Database**: Firebase Firestore (NoSQL) for real-time data sync.
- **Deployment**: Optimized for Streamlit Cloud.

## 🚀 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VINAYVISHWAKARMA20/DIgital-memory-baord.git
   cd DIgital-memory-baord
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Firebase Configuration**:
   Create a `.streamlit/secrets.toml` file and add your Firebase credentials:
   ```toml
   FIREBASE_API_KEY = "your_api_key"
   FIREBASE_AUTH_DOMAIN = "your_project.firebaseapp.com"
   FIREBASE_PROJECT_ID = "your_project_id"
   FIREBASE_STORAGE_BUCKET = "your_project.firebasestorage.app"
   FIREBASE_MESSAGING_SENDER_ID = "your_sender_id"
   FIREBASE_APP_ID = "your_app_id"
   ```

4. **Run the app**:
   ```bash
   streamlit run aapp.py
   ```

## 🌐 Deployment

This app is designed to be deployed on **Streamlit Cloud**. 
- Push your code to GitHub.
- Connect your repo to Streamlit Cloud.
- Add the credentials from `secrets.toml` into the **Advanced Settings > Secrets** section of the Streamlit dashboard.

---
Built with ❤️ for better daily productivity.
