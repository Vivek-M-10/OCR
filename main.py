import pathlib

from fastapi import FastAPI,File,UploadFile
import shutil
import pytesseract

app = FastAPI()


@app.post('/ocr')
def ocr(image: UploadFile = File(...)):
    filePath = 'txtFile'

    with open(filePath,'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return pytesseract.image_to_string(filePath,lang='eng')