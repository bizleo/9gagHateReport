import pandas as pd
from transformers import pipeline


def add_label_column(comments_df):
    """Apply the check_hate_speech function on each comment in the dataframe.
        Using Hugging Face."""
    comments_df[["label", "confidence"]] = df["text"].apply(check_hate_speech).apply(pd.Series)
    return comments_df


def check_hate_speech(text):
    """Use Facebook model to check hate speech."""
    classifier = pipeline("text-classification", model="facebook/roberta-hate-speech-dynabench-r4-target")
    # use the model
    result = classifier(text)
    label = result[0]['label']
    score = result[0]['score']
   
    return {"label": label, "confidence": score}