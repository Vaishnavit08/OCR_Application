import streamlit as st
from PIL import Image, ImageOps
import pytesseract
import re
import json
import time

# Highlight multiple keywords in different colors
def highlight_multiple_keywords(text, keywords):
    colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF6']
    for i, keyword in enumerate(keywords):
        color = colors[i % len(colors)]
        text = re.sub(rf"\b({keyword})\b", rf"<span style='color: {color}; font-weight: bold;'>{keyword}</span>", text, flags=re.IGNORECASE)
    return text

# OCR process with image preprocessing and language selection
def ocr_process(image, query_text, language, preprocess):
    start_time = time.time()  # Track extraction time

    # Open and preprocess image
    image = Image.open(image)
    if preprocess == "Grayscale":
        image = ImageOps.grayscale(image)
    elif preprocess == "Resize (50%)":
        image = image.resize((image.width // 2, image.height // 2))

    # Configure Tesseract for selected language
    tesseract_config = "--psm 6"
    if language == "English":
        tesseract_config += " -l eng"
    elif language == "Hindi":
        tesseract_config += " -l hin"
    else:
        tesseract_config += " -l eng+hin"

    # Extract text using Tesseract OCR
    extracted_text = pytesseract.image_to_string(image, config=tesseract_config)

    # Handle multiple keywords
    keywords = [kw.strip() for kw in query_text.split(',')]
    highlighted_text = highlight_multiple_keywords(extracted_text, keywords)

    # Search keyword positions
    matches_info = []
    for keyword in keywords:
        matches = re.finditer(rf"\b{keyword}\b", extracted_text, re.IGNORECASE)
        match_positions = [match.start() for match in matches]
        matches_info.append(f"Keyword '{keyword}' found at positions: {match_positions}" if match_positions else f"Keyword '{keyword}' not found.")

    search_result = "\n".join(matches_info)

    # Create downloadable JSON
    result_data = {
        'extracted_text': extracted_text,
        'search_query': query_text,
        'search_result': search_result
    }
    result_json = json.dumps(result_data, indent=4)
    with open("ocr_result.json", "w") as file:
        file.write(result_json)

    # Save plain text
    with open("ocr_extracted_text.txt", "w") as file:
        file.write(extracted_text)

    # Calculate extraction time
    extraction_time = time.time() - start_time

    return highlighted_text, search_result, "ocr_result.json", "ocr_extracted_text.txt", f"Time taken for extraction: {extraction_time:.2f} seconds"


# Streamlit UI
st.title("Multilingual OCR & Advanced Keyword Search Application")
st.write("Upload an image, preprocess it, extract text in English or Hindi, search for multiple keywords, and download results in JSON or plain text.")

# Image upload and input options
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
query_text = st.text_input("Enter search keywords (comma-separated for multiple)")
language = st.selectbox("Choose OCR Language", ["English", "Hindi", "English + Hindi"])
preprocess = st.radio("Image Preprocessing", ["None", "Grayscale", "Resize (50%)"])

# Run OCR and display results
if st.button("Run OCR"):
    if uploaded_image and query_text:
        highlighted_text, search_result, json_file, txt_file, extraction_time = ocr_process(uploaded_image, query_text, language, preprocess)

        # Display results
        st.markdown(f"### OCR Results with highlighted search text")
        st.markdown(f"<div>{highlighted_text}</div>", unsafe_allow_html=True)
        st.text_area("Search Result", search_result)

        # Download extracted text as JSON and plain text
        with open(json_file, "r") as file:
            st.download_button("Download Extracted Text as JSON", file, file_name="ocr_result.json", mime="application/json")

        with open(txt_file, "r") as file:
            st.download_button("Download Extracted Text as .txt", file, file_name="ocr_extracted_text.txt")

        # Display extraction time
        st.text(extraction_time)
    else:
        st.error("Please upload an image and provide search keywords.")
