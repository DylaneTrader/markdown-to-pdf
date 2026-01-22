import streamlit as st
import markdown
from weasyprint import HTML

# Page configuration
st.set_page_config(
    page_title="Markdown to PDF Converter",
    page_icon="📄",
    layout="wide"
)

# Custom CSS for better markdown rendering
MARKDOWN_CSS = """
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
}
h1, h2, h3, h4, h5, h6 {
    margin-top: 24px;
    margin-bottom: 16px;
    font-weight: 600;
    line-height: 1.25;
}
h1 { font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
h2 { font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
h3 { font-size: 1.25em; }
code {
    background-color: #f6f8fa;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
}
pre {
    background-color: #f6f8fa;
    padding: 16px;
    overflow: auto;
    border-radius: 3px;
}
pre code {
    background-color: transparent;
    padding: 0;
}
blockquote {
    padding: 0 1em;
    color: #6a737d;
    border-left: 0.25em solid #dfe2e5;
    margin: 0;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 16px 0;
}
table th, table td {
    padding: 6px 13px;
    border: 1px solid #dfe2e5;
}
table tr:nth-child(2n) {
    background-color: #f6f8fa;
}
a {
    color: #0366d6;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
img {
    max-width: 100%;
}
"""

def markdown_to_pdf(markdown_text):
    """Convert markdown text to PDF bytes"""
    # Convert markdown to HTML
    html_content = markdown.markdown(
        markdown_text,
        extensions=['extra', 'codehilite', 'tables', 'fenced_code']
    )
    
    # Wrap in complete HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>{MARKDOWN_CSS}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Generate PDF
    pdf_bytes = HTML(string=full_html).write_pdf()
    return pdf_bytes

def main():
    st.title("📄 Markdown to PDF Converter")
    st.markdown("Convert your Markdown documents to beautiful PDFs")
    
    # Sidebar for instructions
    with st.sidebar:
        st.header("📖 How to use")
        st.markdown("""
        1. **Import** a Markdown file or paste content
        2. **Edit** the Markdown in the editor
        3. **Preview** the rendered output
        4. **Export** to PDF
        """)
        
        st.divider()
        
        st.header("⚙️ Options")
        show_preview = st.checkbox("Show live preview", value=True)
        preview_height = st.slider("Preview height", 300, 800, 500, 50)
    
    # Main content area with two columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("✏️ Markdown Editor")
        
        # File upload option
        uploaded_file = st.file_uploader("Upload Markdown file", type=['md', 'markdown', 'txt'])
        
        # Default content
        default_content = """# Welcome to Markdown to PDF Converter

## Features

- **Easy to use**: Simply paste or upload your markdown
- **Live preview**: See changes in real-time
- **Export to PDF**: Download your document as PDF

## Example Code

```python
def hello_world():
    print("Hello, World!")
```

## Example Table

| Feature | Status |
|---------|--------|
| File Upload | ✅ |
| Live Edit | ✅ |
| PDF Export | ✅ |

## Example List

1. First item
2. Second item
3. Third item

> This is a blockquote example

---

**Bold text** and *italic text*
"""
        
        # Load content from file if uploaded
        if uploaded_file is not None:
            try:
                content = uploaded_file.read().decode('utf-8')
            except UnicodeDecodeError:
                st.error("Error: Unable to decode file. Please upload a valid text file.")
                content = default_content
        else:
            content = default_content
        
        # Text area for editing
        markdown_text = st.text_area(
            "Edit your Markdown here:",
            value=content,
            height=preview_height,
            key="markdown_editor"
        )
    
    with col2:
        if show_preview:
            st.subheader("👁️ Live Preview")
            
            # Convert markdown to HTML and display
            try:
                html_content = markdown.markdown(
                    markdown_text,
                    extensions=['extra', 'codehilite', 'tables', 'fenced_code']
                )
                
                # Display in a container with scrolling
                st.markdown(
                    f'<div style="height: {preview_height}px; overflow-y: auto; border: 1px solid #ddd; padding: 20px; border-radius: 5px;">{html_content}</div>',
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"Error rendering preview: {str(e)}")
    
    # Export section
    st.divider()
    
    col_export1, col_export2, col_export3 = st.columns([1, 1, 2])
    
    with col_export1:
        if st.button("🔄 Clear Content", use_container_width=True):
            # Clear session state to reset to default content
            if 'pdf_bytes' in st.session_state:
                del st.session_state['pdf_bytes']
            st.rerun()
    
    with col_export2:
        # Generate PDF and create download button
        if st.button("📥 Generate PDF", use_container_width=True):
            try:
                with st.spinner("Generating PDF..."):
                    pdf_bytes = markdown_to_pdf(markdown_text)
                    
                    # Store in session state for download
                    st.session_state['pdf_bytes'] = pdf_bytes
                    st.success("PDF generated successfully!")
            except Exception as e:
                st.error(f"Error generating PDF: {str(e)}")
    
    with col_export3:
        # Download button (only shows if PDF was generated)
        if 'pdf_bytes' in st.session_state:
            st.download_button(
                label="⬇️ Download PDF",
                data=st.session_state['pdf_bytes'],
                file_name="document.pdf",
                mime="application/pdf",
                use_container_width=True
            )

if __name__ == "__main__":
    main()
