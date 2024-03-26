# docx2txt processing
import sys

import docx2txt
import os

def convert_docx2txt(import_dir,export_dir):

    try:

        print(import_dir)

        doc = docx2txt.process(import_dir)

        if doc != ' ':
            outfile = open(export_dir,'w',encoding='utf-8')
            outfile.write(doc)

        print("Transformation successfully.")

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Parameter doe not match.")
        sys.exit(1)
    
    import_dir = sys.argv[1]
    export_dir = sys.argv[2]

    convert_docx2txt(import_dir,export_dir)