import os
from docx import Document
from docx.shared import Inches
import folder_managnment

def AddpictureToWordFile(targetfile,text_below,text_above):
    document = Document()
    folderPath=folder_managnment.folder

    p = document.add_paragraph()
    r = p.add_run()

    with os.scandir(folderPath) as entries:
        for entry in entries:
            # print(entry.name)
            r.add_text(text_above)
            r.add_picture(folderPath+ "\\" + entry.name)
            r.add_text(text_below)

    
    document.save(targetfile)
    