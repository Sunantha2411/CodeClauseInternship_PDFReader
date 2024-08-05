import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader

class PDFReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Reader")
        self.root.geometry("600x400")

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = tk.Label(self.root, text="Select a PDF file to read", font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Open File Button
        self.open_button = tk.Button(self.root, text="Open PDF", command=self.open_pdf)
        self.open_button.pack(pady=10)

        # Text Widget for PDF Content
        self.text_widget = tk.Text(self.root, wrap="word", font=("Helvetica", 12))
        self.text_widget.pack(expand=True, fill="both", padx=10, pady=10)

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.read_pdf(file_path)

    def read_pdf(self, file_path):
        try:
            with open(file_path, "rb") as file:
                reader = PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                self.display_text(text)
        except FileNotFoundError:
            messagebox.showerror("Error", "The file was not found.")
        except IOError:
            messagebox.showerror("Error", "Error opening the file.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def display_text(self, text):
        self.text_widget.delete(1.0, tk.END)
        if text:
            self.text_widget.insert(tk.END, text)
        else:
            self.text_widget.insert(tk.END, "No text found in the PDF or PDF extraction failed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFReaderApp(root)
    root.mainloop()
