import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import Tk, filedialog, simpledialog
from shutil import copyfile
import pp


Tk().withdraw()

TESTING = True

if TESTING:
    input_folder = 'C:/Users/Luca Ciraolo/PycharmProjects/PDF-Encryptor/test_folder'
    output_folder = 'C:/Users/Luca Ciraolo/PycharmProjects/PDF-Encryptor/test_folder_output'
    password = 'test123'
else:
    input_folder = filedialog.askdirectory(title= "Select folder to encrypt")
    output_folder = filedialog.askdirectory(title= "Select output folder")
    password = simpledialog.askstring("Password", "Enter password to encrypt:")


def encrypt_pdf(source_path, target_path, password):
    """
    Encrypts a pdf at source_path using password and saves it to target_path
    :param source_path:
    :param target_path:
    :param password:
    :return: None
    """
    print('job started for', source_path)
    in_file = open(source_path, "rb")
    input_pdf = PdfFileReader(in_file)

    output_pdf = PdfFileWriter()
    output_pdf.appendPagesFromReader(input_pdf)
    output_pdf.encrypt(password)

    final_out_path = target_path[:-4] + '.protected.pdf'
    if not os.path.isdir(os.path.dirname(final_out_path)):
        os.mkdir(os.path.dirname(final_out_path))

    out_file = open(final_out_path, "wb")
    output_pdf.write(out_file)
    out_file.close()
    in_file.close()
    print('job completed for', source_path)


job_server = pp.Server()
print("Starting pp with", job_server.get_ncpus(), "workers")

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
            job_server.submit(encrypt_pdf, (src, target, password), (), ("os",))
            # encrypt_pdf(src, target, password)
            count += 1
        else:
            print(name, 'is not a PDF')
            copyfile(src, target)


print('Done!')
