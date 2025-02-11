import streamlit as st
import subprocess
import shutil
import os
import PyPDF2

# Function to read a single PDF file
def read_pdf(file_path):
    pdf_text = ""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_text += page.extract_text() + "\n"
    except Exception as e:
        st.error(f"Error reading {file_path}: {e}")
    return pdf_text

# Function to read all PDFs in the folder
def read_all_pdfs_in_folder(folder_path):
    all_text = ""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            pdf_text = read_pdf(file_path)
            all_text += f"\n--- PDF: {file_name} ---\n" + pdf_text
    return all_text

# Function to run the Ollama Qwen2.5:14b model
def run_qwen2dot5_model(prompt, model="qwen2.5:14b"):
    # Check if 'ollama' is installed
    if shutil.which("ollama") is None:
        return "Error: Ollama is not installed or not found in system PATH."

    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode(),  # Encode input to bytes
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            return result.stdout.decode().strip()
        else:
            return f"Error: {result.stderr.decode()}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"


# Summarization function
def summarize_all_pdfs(folder_path):
    papers_content = read_all_pdfs_in_folder(folder_path)
    prompt = f"Summarize the following collection of research papers in bullet points:\n\n{papers_content}"
    return run_qwen2dot5_model(prompt)

# Q&A function
def ask_question_across_pdfs(folder_path, question):
    papers_content = read_all_pdfs_in_folder(folder_path)
    prompt = f"The following text contains research papers:\n\n{papers_content}\n\nQuestion: {question}\nAnswer:"
    return run_qwen2dot5_model(prompt)

# Streamlit UI
st.title("AI Research Assistant 📚🤖")
st.markdown("This application allows you to summarize research papers or ask questions about them using **Ollama’s Qwen2.5:14b**.")

# Sidebar for user options
with st.sidebar:
    option = st.radio(
        "Select an option:",
        ("Summarize PDFs", "Ask a Question")
    )

# Folder containing PDFs
folder_path = "data/sample_papers"

if option == "Summarize PDFs":
    st.header("Summarize Research Papers")
    if st.button("Summarize All PDFs"):
        st.info("Summarizing all research papers in the folder...")
        summary = summarize_all_pdfs(folder_path)
        st.success("Summary generated successfully!")
        st.text_area("Summary of Research Papers", summary, height=300)

elif option == "Ask a Question":
    st.header("Ask a Question about the Research Papers")
    question = st.text_input("Enter your question:")
    
    if st.button("Get Answer"):
        if question.strip() == "":
            st.error("Please enter a valid question.")
        else:
            st.info("Processing your question...")
            answer = ask_question_across_pdfs(folder_path, question)
            st.success("Answer generated successfully!")
            st.text_area("Answer", answer, height=200)
