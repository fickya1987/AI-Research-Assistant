import subprocess
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
        print(f"Error reading {file_path}: {e}")
    return pdf_text

# Function to read all PDFs in a given folder and concatenate their contents
def read_all_pdfs_in_folder(folder_path):
    all_text = ""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            pdf_text = read_pdf(file_path)
            all_text += f"\n--- PDF: {file_name} ---\n" + pdf_text
    return all_text

# Function to run the Ollama qwen2.5:14b model

def run_qwen2dot5_model(prompt, model="qwen2.5:14b"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Automatically handles string encoding and decoding
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Error running the model:", result.stderr)
            return "Error: Could not generate a response."
    except Exception as e:
        return f"Exception occurred: {str(e)}"

# Summarization function
def summarize_all_pdfs(folder_path):
    papers_content = read_all_pdfs_in_folder(folder_path)
    prompt = f"Summarize the following collection of research papers in bullet points:\n\n{papers_content}"
    summary = run_qwen2dot5_model(prompt)
    return summary

# Q&A function
def ask_question_across_pdfs(folder_path, question):
    papers_content = read_all_pdfs_in_folder(folder_path)
    prompt = f"The following text contains research papers:\n\n{papers_content}\n\nQuestion: {question}\nAnswer:"
    answer = run_qwen2dot5_model(prompt)
    return answer

# Main function to provide user options
def main():
    print("Welcome to the AI Research Assistant!")
    print("Options:\n1. Summarize all PDFs in the folder\n2. Ask a question about the PDFs\n3. Exit\n")

    folder_path = "data/sample_papers"
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            print("\nSummarizing all PDFs...")
            summary = summarize_all_pdfs(folder_path)
            print("\nSummary of the Research Papers:\n", summary)

        elif choice == "2":
            question = input("What would you like to ask about the papers? ")
            print("\nProcessing your question...")
            answer = ask_question_across_pdfs(folder_path, question)
            print("\nAnswer:", answer)

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
