# Multimodal-on-a-pdf
In this a rag that can store images,tables along with text are stored and retrievd from a vector db
# RAG Multimodal on a PDF

This project demonstrates a **Retrieval-Augmented Generation (RAG)** workflow that combines text and image extraction from PDFs using the `unstructured` library and integrates it with OpenAI's **GPT-4 and GPT-4 Vision** models for content summarization. The pipeline processes PDFs, extracts textual components (like `NarrativeText`, `ListItem`, `Table`, etc.), and generates retrieval-optimized summaries for tables and images.

---

## 🧠 Features

- Extracts headers, footers, titles, narrative text, list items, tables, and images from PDFs using `unstructured.partition.pdf`.
- Uses **GPT-4** to summarize tabular content for optimized semantic retrieval.
- Uses **GPT-4 Vision** to summarize images with base64 encoding.
- Supports multiple PDFs and separates content handling for each.

---

## 🛠️ Technologies Used

- Python
- [Unstructured](https://github.com/Unstructured-IO/unstructured) for PDF parsing
- LangChain (`ChatPromptTemplate`, `StrOutputParser`, `ChatOpenAI`)
- OpenAI GPT-4 and GPT-4 Vision
- Google Colab (used for execution environment)

---

## 📁 Folder Structure


project_root/
│
├── data/                           # Folder for input PDFs
│   ├── cj.pdf
│   └── Retrieval-Augmented-Generation-for-NLP.pdf
│
├── extracted_data/                # Images extracted from cj.pdf
├── extracted_data2/               # Images extracted from second PDF
│   └── figure-17-4.jpg
│
├── your_script.py                 # The main code file (this one)
└── README.md                      # This file

## ⚙️ Setup & Installation
💡 This project is intended for Google Colab. If using locally, ensure required libraries are installed.

1. Install dependencies:
bash
Copy
Edit
pip install unstructured
pip install langchain
pip install openai
2. Set your OpenAI API key:
python
Copy
Edit
import os
os.environ["OPENAI_API_KEY"] = "your-key-here"
Or if using Colab:

python
Copy
Edit
from google.colab import userdata
os.environ["OPENAI_API_KEY"] = userdata.get('OPENAI_API_KEY')
🚀 How to Run
Place the PDFs in the /content/data/ or similar path.

Run the extraction logic using partition_pdf.

Use summarize_chain.batch(tab) to get summaries for tables.

Use generate_img_summaries() to summarize images from the extracted folder.
