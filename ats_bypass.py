import os
import docx
import PyPDF2
from PyPDF2.generic import NameObject, TextStringObject

# ========== CONFIG ==========
RESUME_PATH = "C:/Users/brett/OneDrive/Desktop/brett_mayo.docx"   
JOB_DESCRIPTION = """ 
Penetration Tester
-Web application and API security testing (OWASP Top Ten, ASVS)
-Network penetration testing and adversary simulation
-Reverse engineering and exploit development
-Familiarity with Burp Suite, Metasploit, Nmap, and Wireshark
""" 
 # Replace with your job description
OUTPUT_DOCX = "C:/Users/brett/OneDrive/Desktop/brett_resume.docx"
OUTPUT_PDF = "C:/Users/brett/OneDrive/Desktop/resume_hidden.pdf"

# ========== STEP 1: Inject Zero-Width Characters (ATS Boost) ==========
def inject_zero_width(text):
    ZERO_WIDTH_SPACE = "\u200B"  # Unicode character
    return ZERO_WIDTH_SPACE.join(text)  # Inserts a hidden character between every letter

# ========== STEP 2: Modify DOCX (Word Resume) ==========
def modify_docx(input_path, output_path, hidden_text):
    doc = docx.Document(input_path)
    
    # Add hidden text in white font
    para = doc.add_paragraph(hidden_text)
    run = para.runs[0]
    run.font.color.rgb = docx.shared.RGBColor(255, 255, 255)  # White text
    

    doc.save(output_path)
    print(f"[+] Hidden job description added to {output_path}.decode")

# ========== STEP 3: Embed Metadata in PDF ==========
def modify_pdf_metadata(input_pdf, output_pdf, hidden_text):
    with open(input_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # Copy pages
        for page in reader.pages:
            writer.add_page(page)
        
        # Add hidden metadata
        metadata = reader.metadata or {}
        metadata.update({
            "/Title": inject_zero_width("Penetration Tester Resume"),
            "/Keywords": inject_zero_width(hidden_text),
            "/Subject": inject_zero_width("Webapp security, penetration testing, network security"),
            "/Author": "Anonymous"
        })
        
        writer.add_metadata(metadata)

        # Save the modified PDF
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

    print(f"[+] Hidden job description embedded in PDF metadata: {output_pdf}")

# ========== RUN ==========
if __name__ == "__main__":
    # Modify DOCX
    if os.path.exists(RESUME_PATH) and RESUME_PATH.endswith(".docx"):
        modify_docx(RESUME_PATH, OUTPUT_DOCX, JOB_DESCRIPTION)
    
    # Modify PDF
    if os.path.exists(RESUME_PATH.replace(".docx", ".pdf")):
        modify_pdf_metadata(RESUME_PATH.replace(".docx", ".pdf"), OUTPUT_PDF, JOB_DESCRIPTION)

    print("[✅] Resume successfully modified with hidden job description!")
