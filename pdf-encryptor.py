import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import Tk, filedialog, simpledialog

Tk().withdraw()
# file_paths = filedialog.askopenfilenames(title = "Select PDF's to encrypt", filetypes = ("PDF files","*.pdf"))
file_paths = filedialog.askopenfilenames(filetypes=(('PDF files', '*.pdf'),
                                   ('All files', '*.*')),
                                   title="Select PDF's to encrypt")
output_folder = filedialog.askdirectory(title= "Select output folder")
password = simpledialog.askstring("Password entry", "Enter password to encrypt:")

count = 1
for file_path in file_paths:
    print('encrypting file', count, 'of', len(file_paths))
    in_file = open(file_path, "rb")
    input_pdf = PdfFileReader(in_file)

    output_pdf = PdfFileWriter()
    output_pdf.appendPagesFromReader(input_pdf)
    output_pdf.encrypt(password)

    target_file_path = os.path.join(output_folder, os.path.basename(file_path))
    out_file = open(target_file_path, "wb")
    output_pdf.write(out_file)
    out_file.close()
    in_file.close()

    count = count + 1

print('Finished!')
