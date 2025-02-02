# 📚 AI Research Assistant 🤖

A powerful AI-driven tool to summarize research papers and answer questions using Ollama’s Qwen2.5:14B model.

---

## 🔍 Overview

AI Research Assistant processes multiple research papers in PDF format, extracts key insights, and answers user questions with the power of Ollama’s Qwen2.5:14B LLM.

### ✅ Key Features
- **Summarizes research papers** in bullet points.
- **Answers questions** based on research paper content.
- **Interactive Streamlit UI** for easy usage.
- **Works with multiple PDFs** in the `data/sample_papers/` folder.

---

## 🚀 Features

- **Summarization:** Get a structured summary of all research papers.
- **Q&A System:** Ask any research-related question and get AI-generated responses.
- **Streamlit UI:** Use an easy-to-navigate web interface.
- **Command-line Interface (CLI):** Use directly from the terminal.
- **Ollama's Qwen2.5:14B Model:** Leverages powerful AI for understanding and answering queries.

---

## 📂 Folder Structure

```
AI-Research-Assistant/
├── main.py                 # CLI for summarization & Q&A
├── app.py                  # Streamlit UI for interactive use
├── data/
│   └── sample_papers/      # Folder containing research paper PDFs
├── requirements.txt        # Required dependencies
└── README.md               # Project documentation
```

---

## ⚡ Installation & Setup

### 🔹 1. Install Dependencies
Ensure you have Python installed (>=3.10). Then run:

```bash
pip install -r requirements.txt
```

### 🔹 2. Install Ollama & Qwen2.5:14B Model
Download and install Ollama from [ollama.ai](https://ollama.ai) and pull the Qwen2.5:14B model:

```bash
ollama pull qwen2.5:14b
```

### 🔹 3. Add Research Papers
Place your research PDFs in the `data/sample_papers/` folder.

---

## 🖥️ Running the AI Research Assistant

### 📌 Option 1: Use the Command-Line Interface (CLI)
Run the assistant using:

```bash
python main.py
```

**Available options:**

1️⃣ Summarize all research papers  
2️⃣ Ask a question about the research papers  
3️⃣ Exit  

### 📌 Option 2: Use the Streamlit Web UI
Launch the web application:

```bash
streamlit run app.py
```

This will open an interactive UI in your browser where you can:
- ✅ Summarize PDFs with a single click
- ✅ Ask questions and get AI-powered answers

---

## 🛠️ Example Usage

### 📌 Summarization (CLI)

```bash
Enter your choice (1/2/3): 1
```

**Output (Example):**

```yaml
Summary of Research Papers:
- Paper 1: Discusses LSTM networks and their role in deep learning.
- Paper 2: Analyzes residual connections in CNNs.
...
```

### 📌 Q&A (CLI)

```bash
Enter your choice (1/2/3): 2
What would you like to ask about the papers? What is the role of residual connections in deep neural networks?
```

**Output (Example):**

```bash
Answer: Residual connections help deep neural networks by mitigating vanishing gradients...
```

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).
