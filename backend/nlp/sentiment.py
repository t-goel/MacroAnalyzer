from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import List, Dict

MODEL_NAME = "ProsusAI/finbert"
LABELS = ["positive","negative","neutral"]

tokenizer = None
model = None
device = torch.device("mps" if torch.mps.is_available() else "cpu")

def load_model():
    global tokenizer, model
    if model is None:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        model.to(device)
        model.eval()

def analyze_batch(texts: List[str]) -> List[Dict[str,float]]:

    load_model()
    inputs = tokenizer(
        texts,
        return_tensors="pt",
        truncation = True,
        padding = True,
        max_length = 512
        ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1).cpu().numpy()

    results = []
    for p in probs:
        results.append({
            "sentiment" : LABELS[p.argmax()],
            "positive" : p[0],
            "negative" : p[1],
            "neutral" : p[2]
        })
    return results