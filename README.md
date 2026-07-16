# 🧠 Deepfake Authentification Detection System

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-6.0-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)

> AI-powered system to detect deepfake videos using deep learning.

---

## 📌 Overview

This project uses a **Res-NeXt CNN + LSTM RNN** model to distinguish AI-generated deepfake videos from real ones. It provides a web interface for user authentication, video/image upload, and real-time detection results.

---

## ✨ Features

- 🔐 User registration, login & logout with CSRF protection  
- 🎥 Upload videos or images for deepfake analysis  
- 🤖 AI detection using Res-NeXt + LSTM  
- 📊 Dashboard with detection history  
- 📱 Fully responsive design  

---

## 🛠️ Tech Stack

- **Backend:** Django 6.0 (Python 3.11)  
- **Database:** SQLite3  
- **Frontend:** HTML5, CSS3, JavaScript  
- **AI/ML:** Res-NeXt CNN, LSTM RNN  

---

## 🚀 Quick Setup

```bash
git clone https://github.com/FRANKFRANK5/Deepfake-Authentification-Detection-system.git
cd Deepfake-Authentification-Detection-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py migrate

# Run server
python manage.py runserver

Visit http://127.0.0.1:8000/ to start using the system.
📂 Project Structure
text

├── project_settings/       # Django settings & URLs
├── ml_app/                 # Main application logic
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── media/                  # User-uploaded files
├── models/                 # Pretrained AI models
├── uploaded_videos/        # Uploaded videos
└── uploaded_images/        # Uploaded images

🙏 Credits

Special thanks to abhijitjadhav1998/Deepfake_detection_using_deep_learning for the foundational research and code.
📝 License

MIT License – see LICENSE for details.
📧 Contact

GitHub: FRANKFRANK5
