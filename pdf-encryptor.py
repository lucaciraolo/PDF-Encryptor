import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import Tk, filedialog, simpledialog
from shutil import copyfile


Tk().withdraw()

input_folder = filedialog.askdirectory(title= "Select folder to encrypt")
# input_folder = 'C:/Users/Luca Ciraolo/PycharmProjects/PDF-Encryptor/test_folder'
output_folder = filedialog.askdirectory(title= "Select output folder")
# output_folder = 'C:/Users/Luca Ciraolo/PycharmProjects/PDF-Encryptor/test_folder_output'
password = simpledialog.askstring("Password", "Enter password to encrypt:")
# password = 'test123'

count = 1
for root, dirs, files in os.walk(input_folder, topdown=False):
    for name in files:
        print('encrypting file', count, 'of', len(files))
        src = os.path.join(root, name)
        # print('source', src)

        dir = root[len(input_folder):]
        target = os.path.join(output_folder + dir, name)
        # print('target', target)

        if (name.endswith('.pdf')):
            # print(target[:-4] + '.protected.pdf')
            in_file = open(src, "rb")
            input_pdf = PdfFileReader(in_file)

            output_pdf = PdfFileWriter()
            output_pdf.appendPagesFromReader(input_pdf)
            output_pdf.encrypt(password)

            final_out_path = target[:-4] + '.protected.pdf'
            if not os.path.isdir(os.path.dirname(final_out_path)):
                os.mkdir(os.path.dirname(final_out_path))

            out_file = open(final_out_path, "wb")
            output_pdf.write(out_file)
            out_file.close()
            in_file.close()
            count += 1
        else:
            print(name, 'is not a PDF')
            copyfile(src, target)


print('Done!')
