from transformers import AutoTokenizer, pipeline


''' 
    #load the model for question answering
modelQA = "deepset/roberta-base-squad2"
modelforQA = AutoModelForQuestionAnswering.from_pretrained(modelQA)
tokenizerQA = AutoTokenizer.from_pretrained(modelQA)
QAGenerator = pipeline('question-answering', model=modelQA, tokenizer=tokenizerQA)


    #load the model for summarization
modelSUM = "facebook/bart-large-cnn"
tokenizerSUM = AutoTokenizer.from_pretrained(modelSUM)
summarizer = pipeline("summarization", 
        model=modelSUM, 
        tokenizer=tokenizerSUM)

'''

#for Question-Answering task
def QAfromLLM(question,context,llm):

    modelQA = llm
    # modelforQA = AutoModelForQuestionAnswering.from_pretrained(modelQA)
    tokenizerQA = AutoTokenizer.from_pretrained(modelQA,load_in_4bit = True, device_map="auto")
    QAGenerator = pipeline('question-answering', model=modelQA, tokenizer=tokenizerQA)

    QA_input = {
        'question': question,
        'context': context 
    }
    res = QAGenerator(QA_input)

    return res['answer']

#for summarization task
def summarization(text,llm):

    modelSUM = llm
    tokenizerSUM = AutoTokenizer.from_pretrained(modelSUM, load_in_4bit=True, device_map="auto")
    summarizer = pipeline("summarization", 
        model=modelSUM, 
        tokenizer=tokenizerSUM)

    if llm == "google/pegasus-xsum":
        text = text[:512]

    ans = summarizer(text, do_sample=True) 

    return ans[0]['summary_text']







