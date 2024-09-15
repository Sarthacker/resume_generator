# LinkedIn PDF to HTML Resume Generator

This is a simple web application that generates an HTML resume from a LinkedIn PDF download using Google Generative AI (Gemini) API. The application extracts text from the uploaded PDF, and with the help of Gemini, it generates a professional HTML resume with inline CSS.

## Features
- Extracts text from a LinkedIn PDF file.
- Generates a professional HTML resume with inline CSS using Google Generative AI (Gemini).
- Supports download of the generated HTML resume.
- Deployed using platforms like Vercel or GitHub Pages.

## Tech Stack
- **Python**: Core programming language used for developing the application.
- **Streamlit**: Framework for creating a simple web interface for uploading PDF files and interacting with the application.
- **PyPDF2**: Python library used to extract text from PDF files.
- **Google Generative AI (Gemini)**: Utilized to generate the HTML resume and inline CSS.
- **Deployment**: Deployed using Vercel/GitHub Pages for easy sharing.

## Approach

1. **Extracting Text from PDF**:
   - The application uses `PyPDF2` to read and extract text from the LinkedIn PDF file uploaded by the user.
   
2. **Generating HTML Resume**:
   - With the extracted text, the application sends a request to the Google Generative AI model (Gemini) using a prompt that asks for a professional HTML resume.
   - The model responds with an HTML structure styled with inline CSS, ensuring that the resume adheres to standard A4 dimensions and professional formatting guidelines.
   
3. **User Interface**:
   - The app interface is built using `Streamlit`. Users provide the API key, upload their LinkedIn PDF, and generate the HTML resume.
   - The app also offers an option to download the generated HTML file.