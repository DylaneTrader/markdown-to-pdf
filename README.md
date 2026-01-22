# Markdown to PDF Converter 📄

A simple and elegant Streamlit application to convert Markdown files to PDF documents.

## Features

✨ **Easy to Use**: Upload Markdown files or paste content directly  
✏️ **Live Editing**: Edit your Markdown in real-time  
👁️ **Live Preview**: See the rendered output as you type  
📥 **PDF Export**: Download your document as a beautifully formatted PDF  

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DylaneTrader/markdown-to-pdf.git
cd markdown-to-pdf
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## How to Use

1. **Import**: Upload a Markdown file or paste your content in the editor
2. **Edit**: Modify the Markdown content in the left panel
3. **Preview**: See the rendered output in the right panel (if enabled)
4. **Export**: Click "Generate PDF" and then "Download PDF" to save your document

## Dependencies

- `streamlit`: Web application framework
- `markdown`: Markdown to HTML conversion
- `weasyprint`: HTML to PDF conversion
- `Pillow`: Image processing support

## License

MIT License