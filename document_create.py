import os
from docx import Document
from docx.shared import Inches
import folder_managnment

def AddpictureToWordFile(targetfile):
    document = Document()
    folderPath=folder_managnment.folder

    document.add_paragraph()
    # r = p.add_run()
    with os.scandir(folderPath) as entries:
        for entry in entries:
            # print(entry.name)
            #r.add_text(text_above)
            document.add_picture(folderPath+ "\\" + entry.name)
            document.add_paragraph(entry.name)

    document.save(targetfile)
    