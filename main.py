import streamlit as st
import PyPDF2
import google.generativeai as genai

# Function to configure API key for Gemini/Generative AI
def configure_api(api_key):
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        st.error(f"Error configuring API key: {e}")
        return False
    return True

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to generate HTML and CSS using the Gemini model
def generate_resume(resume_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Generate a professional HTML resume page with inline CSS using the following resume text while satisfying following conditions - 1) The page should be A4 2) The headings and texts must be properly aligned 3) The alignment and spaces between the headings and items must be quite profesional 4) The resume must be centered 5) Remove all the comments from the html and css code 6) The contents of the resume must be left aligned with bullet ponits 7) Limit the reusme to a single page that must look profesional 8) The summary part must be totaly ignored:\n{resume_text}"
    response = model.generate_content(prompt)
    return response.text

# Streamlit Web App
def main():
    st.title("LinkedIn PDF to HTML Resume Generator with Gemini")

    # Step 1: Ask for Gemini API Key
    st.subheader("Step 1: Enter your Gemini API Key")
    api_key = st.text_input("Gemini API Key", type="password")

    if api_key:
        # Configure the API key for the generative model
        if configure_api(api_key):
            # Step 2: Upload LinkedIn PDF
            st.subheader("Step 2: Upload your LinkedIn PDF")
            uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

            if uploaded_file is not None:
                # Extract text from the uploaded PDF
                st.write("Extracting text from PDF...")
                extracted_text = extract_text_from_pdf(uploaded_file)
                st.success("PDF text extracted successfully!")

                # Step 3: Generate HTML and CSS Using Gemini
                st.subheader("Step 3: Generate HTML and CSS with Gemini")
                if st.button("Generate HTML Resume"):
                    st.write("Generating HTML and CSS using Gemini...")
                    try:
                        html_and_css = generate_resume(extracted_text)
                        st.write("Generated HTML and CSS:")
                        st.code(html_and_css, language='html')

                        # Provide a download button for the HTML resume
                        st.download_button(
                            label="Download HTML Resume",
                            data=html_and_css,
                            file_name="resume.html",
                            mime="text/html"
                        )
                    except Exception as e:
                        st.error(f"Error generating HTML and CSS: {e}")
        else:
            st.error("Invalid API Key.")
    else:
        st.warning("Please provide your Gemini API key to proceed.")

if __name__ == "__main__":
    main()
