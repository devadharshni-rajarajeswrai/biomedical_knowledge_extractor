# Tasks:

# 1. Load `.txt` research paper.
    # How to read them in Python
    #   1. PyPDF2 for basic page text extraction
    #   2. pdfplumber for better layout and partial page extraction
    #   3. pdfminer.six for more advanced text parsing

# 2. Remove:
#     - references section
#     - figure captions
#     - citations like `(Smith et al., 2020)`
# 3. Convert to lowercase.
# 4. Remove special characters.
import os
import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    all_text = []
    for page in reader.pages:
        text = page.extract_text().lower()  # Convert to lowercase
        # print_citations(text)  # Print citations before cleaning
        print_figure_captions(text)  # Print figure captions before cleaning
        # clean = re.sub(r'\(.*?\)', '', text)  # Remove citations like (Smith et al., 2020)
        clean = re.sub(r"[^\x20-\x7E]", "", text)
        clean = re.sub(r"\s+", " ", clean).strip()
        if text:
            all_text.append(clean)
    
    txt_file_path = os.path.splitext(file_path)[0] + '.txt'
    with open(txt_file_path, 'w',encoding="utf-8", errors="replace") as txt_file:
        txt_file.write('\n\n'.join(all_text))

def print_citations(text):

    # pattern = r"\b\d+\b"
    
    citations = re.findall(r'\(.*?\)', text)
    # citations = re.findall(pattern, text)
    for citation in citations:
        print(citation)

def print_figure_captions(text):
    # This is a very basic pattern and may need to be adjusted based on the actual format of figure captions in the papers
    pattern = r"\b(fig\.?|figure)\s?\d+[a-zA-Z]?\b"
    captions = re.findall(pattern, text)
    for caption in captions:
        print(caption)
       
extract_text_from_pdf('data/sample_research_paper.pdf')


