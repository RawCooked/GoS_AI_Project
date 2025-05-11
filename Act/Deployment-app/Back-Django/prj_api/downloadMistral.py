from transformers import AutoModelForCausalLM, AutoTokenizer
import os

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
MODEL_PATH = os.path.expanduser("~/mistral-7b-instruct")

print("Downloading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto",
    cache_dir=MODEL_PATH
)

print("Model and tokenizer successfully downloaded.")