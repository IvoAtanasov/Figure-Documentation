from docx import Document
from docx.shared import Inches

def AddpictureToWordFile(picture,file,text_below,text_above):
    document = Document()

    p = document.add_paragraph()
    r = p.add_run()
    r.add_text(text_above)
    r.add_picture(picture)
    r.add_text(text_below)

    document.save(file)
    