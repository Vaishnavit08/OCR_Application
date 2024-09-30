
---

# 🌟 OCR Application: Extract Text and Search Keywords in Hindi & English!

Welcome to the **OCR Application**, a powerful web-based tool that lets you upload an image, extract text in **both Hindi and English**, and even search for specific keywords within that text. Whether you're looking to digitize documents, search through complex image-based text, or just experiment with cutting-edge OCR tech—**this application has got you covered!**

🎯 **Live Demo**: [https://hfprlobdfimpgxcykbpahc.streamlit.app](#)  
⚡ **Technologies**: Python, Streamlit, Huggingface Transformers, PyTorch, Gradio, ColPali, and Byaldi Libraries

---

## 🚀 Features at a Glance

- **Dual-language OCR**: Extracts text from images in both **Hindi** and **English**.
- **Keyword Search**: Easily search for words within the extracted text—matches are *highlighted* for clarity.
- **Text Extraction Options**: View the extracted text in-app or download it as **JSON** or **plain text**.
- **Interactive & Simple UI**: Intuitive interface built with **Streamlit**.
- **High-accuracy OCR Models**: Powered by advanced models such as **Byaldi** and **Qwen2-VL** for seamless text extraction.

---

## 📝 Table of Contents

- [About the Project](#about-the-project)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Deployment Guide](#deployment-guide)
- [Technical Stack](#technical-stack)
- [Sample Output](#sample-output)
- [Connect With Me](#connect-with-me)

---

## 💡 About the Project

This project is an **end-to-end OCR and search tool** that lets users:
1. Upload an image containing **Hindi** or **English** text.
2. Perform **Optical Character Recognition (OCR)** to extract that text.
3. **Search for keywords** within the extracted text with results dynamically highlighted.

Not only does the application achieve this with **high accuracy**, but it’s also lightweight, fast, and deployed online for easy access!

### 🎯 Objective

The aim is to create a simple yet functional web-based tool that can **extract and search text** from images, supporting both **Hindi and English** languages, all while being accessible via a public URL.

---

## 📂 Project Structure

Here's a breakdown of the file structure of the project:

```plaintext
OCR_Application/
├── app/
│   ├── ocr_processing.py          # Core OCR logic and model integration
│   ├── search_function.py         # Keyword search logic and text highlighting
│   └── utils.py                   # Helper functions for image preprocessing
│
├── web_app/
│   ├── app.py                     # Main Streamlit web application script
│   └── requirements.txt           # List of dependencies for easy setup
│
├── examples/
│   ├── sample_image.jpg           # Example image for OCR testing
│   ├── extracted_text.json        # Sample JSON output of extracted text
│   └── extracted_text.txt         # Sample plain text output of OCR
│
├── README.md                      # Project documentation
```

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Vaishnavit08/OCR_Application.git
cd OCR_Application
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure you have **Tesseract OCR** installed on your machine.  
For Ubuntu:
```bash
sudo apt install tesseract-ocr
```
For Windows, [download it here](https://github.com/tesseract-ocr/tesseract).

### 3. Run the Web Application

Launch the Streamlit app:
```bash
streamlit run web_app/app.py
```

### 4. Open the Browser

Head to `http://localhost:8501` and start uploading your images!

---

## 🛠️ How It Works

### 1. **Upload Image**

Simply drag and drop an image (JPEG, PNG, etc.) containing **text in Hindi or English**.

### 2. **Perform OCR**

The application uses a **pre-trained OCR model** (either **ColPali** or **General OCR Theory (GOT)**) to extract text from the image. The extracted text is returned in a structured format, either **plain text** or **JSON**.

### 3. **Search Keywords**

You can search for **multiple keywords** within the extracted text. All matching keywords are **highlighted** in different colors for easier reading.

### 4. **Download Results**

The extracted text can be downloaded as a **plain text file** or **JSON** for future use.

---

## 🚀 Deployment Guide

You can deploy this application to platforms like **Streamlit Sharing**, **Hugging Face Spaces**, or **Heroku**. Here’s a simple guide to deploy:

### Deploy to Streamlit Sharing

1. Fork or clone the repository.
2. Push the project to your own GitHub account.
3. Log in to [Streamlit Sharing](https://streamlit.io/sharing) and connect your GitHub repository.
4. Deploy the project, and get your live URL to share!

Other Deployment Options:
- **Heroku**: Follow their [Python deployment guide](https://devcenter.heroku.com/articles/deploying-python).
- **Hugging Face Spaces**: Follow their [spaces documentation](https://huggingface.co/docs/spaces).

---

## 🧑‍💻 Technical Stack

- **Frontend**: 
  - **Streamlit** for the UI
- **Backend**: 
  - **OCR Models**: ColPali (Byaldi implementation), Huggingface Transformers (Qwen2-VL), and General OCR Theory (GOT).
  - **Libraries**: PyTorch, Pillow for image processing
- **Deployment**: Deployed on [Streamlit Sharing](https://streamlit.io/sharing) (or any similar platform).

---

## 🔍 Sample Output

### 🖼️ Image 1: Input Image Example

![image](https://github.com/user-attachments/assets/c10a585b-e050-4091-bdcd-1d4c002f84d4)

Description: This is the sample image used for OCR processing in English and Hindi text.

---

### 🖼️ Image 2: Final Output After OCR and Highlighting

+--------------------------------+
|          Image Preview         |
+--------------------------------+
![image](https://github.com/user-attachments/assets/ea0774bd-6286-48a4-8e19-dc512e9464a7)

**Look at this!** The OCR has detected and highlighted the keywords perfectly. 🎉

---

## 🌐 Connect With Me

- 📧 **Email**: [vaishnavitalekar0811@gmail.com](mailto:vaishnavitalekar0811@gmail.com)  
- 👨‍💻 **GitHub**: [https://github.com/Vaishnavit08](https://github.com/Vaishnavit08)  
- 💼 **LinkedIn**: [linkedin.com/in/vaishnavii-talekar-548490218](https://linkedin.com/in/vaishnavii-talekar-548490218)

Feel free to reach out for suggestions, bugs, or collaboration opportunities!

---

