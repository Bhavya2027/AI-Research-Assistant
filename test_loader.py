from src.pdf_loader import load_pdfs

docs = load_pdfs("data/pdfs")

print("\nSUCCESS")
print("Total documents:", len(docs))