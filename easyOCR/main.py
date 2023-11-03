import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'     # openMP fix 

from fastapi import FastAPI, File, UploadFile, Form
from textExtraction import read_text
from LLMQA import QAfromLLM,summarization

app = FastAPI()

@app.post("/qa")
async def create_upload_file(image: UploadFile = File(...), question: str = Form(...), llm : str = Form(...)):

    answer = ""
    image_bytes = await image.read()     # convert the UploadFile type to image_bytes
    text = read_text(image_bytes)       # call the read_text function from textExtraction.py and get the extracted text

    answer = QAfromLLM(question,text,llm)
        
    return answer

@app.post("/summarization")
async def create_upload_file(image: UploadFile = File(...),llm : str = Form(...)):

    answer = ""
    image_bytes = await image.read()     # convert the UploadFile type to image_bytes
    text = read_text(image_bytes)       # call the read_text function from textExtraction.py and get the extracted text

    answer = summarization(text,llm)
    
    return answer

# if __name__ == '__main__':
#     uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)