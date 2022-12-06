from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from transformers import pipeline   


def summarize(data):
    print("hello")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print("world")
    return summarizer(data, max_length=130, min_length=30, do_sample=False)
