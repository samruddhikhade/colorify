# 🎨 Colorify

> AI-powered web app for colorizing black & white images.

---

## 🚀 Overview

Colorify is a web-based application that converts grayscale images into colored images using a deep learning model.

The application integrates a Flask backend with an AI model to process user-uploaded images and return colorized outputs through a simple and interactive web interface.

---

## ✨ Features

- Upload grayscale images  
- AI-based image colorization  
- Before & After comparison  
- Download processed images  
- Clean and responsive UI  

---

## ⚙️ Tech Stack

Frontend:
- HTML  
- CSS  
- JavaScript  

Backend:
- Python (Flask)  

AI Model:
- DeOldify (pre-trained image colorization model)

---

## 🧠 Working Architecture

1. User uploads a grayscale image  
2. Image is sent to Flask backend  
3. Backend processes the image using DeOldify model  
4. Model generates a colorized output  
5. Result is displayed with before/after comparison  
6. User can download the final image  

---

## 📁 Project Structure

colorify-project/

app.py  
requirements.txt  

templates/  
  index.html  

static/  
  css/  
  js/  
  images/  

---

## ▶️ Run Locally

git clone https://github.com/samruddhikhade/colorify-project.git  
cd colorify-project  

python -m venv venv  
venv\Scripts\activate  

pip install -r requirements.txt  

python app.py  

---

## ⚠️ Limitations

- Model performance depends on input image quality  
- Results may vary for complex images  
- Processing time can be higher for large images  

---

## 🔮 Future Improvements

- Improve model accuracy  
- Optimize performance  
- Enhance UI/UX for better experience  

---

## 👩‍💻 Author

Samruddhi  

---

## 🔗 Live Demo

Currently runs locally. Deployment in progress.
