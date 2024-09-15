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

## Approach

1. **Extracting Text from PDF**:
   - The application uses `PyPDF2` to read and extract text from the LinkedIn PDF file uploaded by the user.
   
2. **Generating HTML Resume**:
   - With the extracted text, the application sends a request to the Google Generative AI model (Gemini) using a prompt that asks for a professional HTML resume.
   - The model responds with an HTML structure styled with inline CSS, ensuring that the resume adheres to standard A4 dimensions and professional formatting guidelines.
   
3. **User Interface**:
   - The app interface is built using `Streamlit`. Users provide the API key, upload their LinkedIn PDF, and generate the HTML resume.
   - The app also offers an option to download the generated HTML file.

## Problem Breakdown

The goal of the assignment was to create a simple web application that:
1. Takes a LinkedIn PDF resume as input.
2. Extracts the relevant content from the PDF.
3. Generates a professional, single-page HTML resume.
4. Provides the user with an interface to upload the PDF and download the generated HTML file.
5. The application must use a Gemini API for content generation and be deployed on a platform like Vercel or GitHub Pages.

## My Solution

### 1. Input Handling (PDF Upload and Text Extraction)
- **Challenge**: The application needed to take a PDF resume as input, extract its content, and process it into plain text that can be passed to the AI model.
- **Solution**: I used the `Streamlit` framework to create a web interface where users could upload their LinkedIn PDF file. 
    - **PDF Text Extraction**: I used the `PyPDF2` library to extract text from the uploaded PDF. This allowed me to convert the PDF data into plain text that can be processed further by the AI model. The process involves reading each page of the PDF and concatenating the extracted text.

### 2. Generating the HTML Resume with AI
   - I crafted a specific prompt for the AI model, ensuring that it generates a clean, professional-looking HTML document. Key conditions in the prompt included:
   - The resume should fit on a single A4 page.
   - Proper alignment and spacing between headings and text.
   - Ignoring irrelevant sections, like the summary part, from the extracted text.
   - Keeping the resume content clean, bullet-pointed, and left-aligned.
   - The response from the AI provided the necessary HTML and inline CSS to create a professional resume layout.

### 3. User Interaction and HTML Resume Download
- **Challenge**: Provide an interface that allows users to easily interact with the application and download the HTML resume.
- **Solution**: Using `Streamlit`, I created a user-friendly interface that guides the user through the process:
    1. First, the user enters their **Gemini API key**.
    2. They then upload their LinkedIn PDF resume.
    3. Once the resume is uploaded, the extracted text is processed, and the HTML resume is generated.
    4. A button is provided to download the HTML resume file.
    - **Key Feature**: The user can download the generated HTML resume directly from the interface in one click.

### 4. Handling the API Key Securely
- **Challenge**: The application needed to use the OpenAI (Gemini) API, but the API key should not be hardcoded or exposed publicly.
- **Solution**: I implemented a simple input form in `Streamlit` where the user is prompted to enter their API key. This allows each user to provide their own Gemini API key securely without exposing it in the code or in the public domain.

### 5. Deployment
- **Challenge**: The application needed to be deployed and accessible via a public URL.
- **Solution**: I deployed the application using **Vercel**, a platform that allows fast, easy deployment of web apps.
    - **Alternative**: The app can also be deployed on **GitHub Pages** if needed. Both platforms ensure the app is accessible to users via a simple URL.

## Conclusion

### Why This Approach Works
- **Efficiency**: I used pre-built libraries (`PyPDF2` for PDF text extraction, `Streamlit` for web interface) and the powerful **Google Generative AI (Gemini)** for HTML generation. This allowed me to focus on the core logic of the application while letting the AI handle the heavy lifting of resume formatting.
- **User-Friendly Interface**: The `Streamlit` framework provided an intuitive and simple interface for users to interact with the application, upload their PDF, and download the HTML resume.
- **Customizability**: By using a dynamic prompt for the AI, the resume generation process can be easily modified to accommodate different styles or formats in the future.
- **Secure**: The API key handling is secure, as users are prompted to enter their key, which is never exposed publicly or stored.

This approach allowed me to solve the problem within the given 24-hour timeframe while ensuring a functional and easy-to-use application.
