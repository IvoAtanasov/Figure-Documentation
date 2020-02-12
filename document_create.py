import os
from docx import Document
from docx.shared import Inches
import folder_managnment
import string_manupulation
import collections

def AddpictureToWordFile(targetfile):
    document = Document()
    folderPath=folder_managnment.folder
    dictionaryPic={}
    document.add_paragraph()

    with os.scandir(folderPath) as entries:
        for entry in entries:
            print(entry.name)
            dictionaryPic[string_manupulation.FindNumber(entry.name)]=entry.name

    od=collections.OrderedDict(sorted(dictionaryPic.items()))
    
    for k, v in od.items():
        print(str(k) +" " + v)
        if(k>0):
            document.add_picture(folderPath+ "\\" + v)
            document.add_paragraph(v.replace("Step","Figure"))

    document.save(targetfile)
    