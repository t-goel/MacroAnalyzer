from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import List, Dict

MODEL_NAME = "ProsusAI/finbert"
_LABELS = ["positive","negative","neutral"]

_tokenizer = None
_model = None
#mac only, runs on cpu

