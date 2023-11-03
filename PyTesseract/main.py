# import os
# os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'  # openMP fix

# from fastapi import FastAPI, File, UploadFile, Form
# from textExtractKERASocr import read_text
# from LLMQA import QAfromLLM,summarization

# app = FastAPI()

# @app.post("/qa")
# async def create_upload_file(image: UploadFile = File(...), question: str = Form(...), llm: str = Form(...)):
#     answer = ""
#     img = await image.read()  # convert the UploadFile type to image_bytes
#     text = read_text(img)  # call the read_text function from textExtraction.py and get the extracted text
#     answer = QAfromLLM(question, text, llm)
#     return answer

# @app.post("/summarization")
# async def create_upload_file(image: UploadFile = File(...), llm: str = Form(...)):
#     answer = ""
#     img = await image.read()  # convert the UploadFile type to image_bytes
#     text = read_text(img)  # call the read_text function from textExtraction.py and get the extracted text
#     answer = summarization(text, llm)
#     return answer


import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'     # openMP fix 

from fastapi import FastAPI, File, UploadFile, Form
# from textExtraction import read_text
# from textExtractKERASocr import read_text

from tesseractOCR import create_string
from LLMQA import QAfromLLM,summarization

app = FastAPI()

@app.post("/qa")
async def create_upload_file(image: UploadFile = File(...), question: str = Form(...), llm : str = Form(...)):

    answer = ""
    image_bytes = await image.read()     # convert the UploadFile type to image_bytes
    text = create_string(image_bytes)       # call the read_text function from textExtraction.py and get the extracted text

    answer = QAfromLLM(question,text,llm)
        
    return answer

@app.post("/summarization")
async def create_upload_file(image: UploadFile = File(...),llm : str = Form(...)):

    answer = ""
    image_bytes = await image.read()     # convert the UploadFile type to image_bytes
    text = create_string(image_bytes)       # call the read_text function from textExtraction.py and get the extracted text

    answer = summarization(text,llm)
    
    return answer






