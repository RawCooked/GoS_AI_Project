# 🎓 **School Project: Assessing Mathematical Creativity & Correctness** 🚀

Welcome to the **official documentation** for our project! This document will guide you through our approach to detecting **mathematical creativity and correctness** in children's test papers using AI. 🧠✨

---

## 📌 **Table of Contents**

- [📖 Overview](#-overview)
- [💡 Key Concepts](#-key-concepts)
  - [🔧 Fine-Tuning](#-fine-tuning)
  - [🎨 Pre-Prompting (Prompt Engineering)](#-pre-prompting-prompt-engineering)
- [🛠️ Project Pipeline](#-project-pipeline)
- [📸 Using Qari-OCR for OCR](#-using-qari-ocr-for-ocr)
- [📊 Fine-Tuning for Math Creativity & Correction](#-fine-tuning-for-math-creativity--correction)
- [📋 Data Preparation and Annotation](#-data-preparation-and-annotation)
- [🚀 Next Steps](#-next-steps)

---

## 📖 **Overview**

🎯 This project aims to **evaluate** children’s **math creativity** and **correctness** based on their test responses.  
We use **OCR, object detection, and LLMs** to analyze student answers from images of test sheets.  

Our primary **data source** is the **Tunisian Ministry of Education's math book for children**. 📚🇹🇳

---

## 💡 **Key Concepts**

### 🔧 **Fine-Tuning**
✅ **Definition**: Training a model on new data to make it specialize in a task.  
📌 **When to use**:  
- You need the model to learn new patterns.  
- Domain-specific knowledge is required.  

💎 **Pros**:  
✔️ Adapts to your specific dataset.  
✔️ Can generalize well if trained properly.  

⚠️ **Cons**:  
❌ Requires labeled data & computation power.  
❌ Can overfit if not done correctly.  

---

### 🎨 **Pre-Prompting (Prompt Engineering)**
✅ **Definition**: Using carefully crafted prompts to guide the model’s output **without changing its parameters**.  
📌 **When to use**:  
- You want quick results without retraining.  
- The model already understands your domain but needs guidance.  

💎 **Pros**:  
✔️ Quick and easy implementation.  
✔️ No additional training needed.  

⚠️ **Cons**:  
❌ Limited flexibility.  
❌ Inconsistent performance across different cases.  

🆚 **Fine-Tuning vs. Pre-Prompting**  
| Feature           | Fine-Tuning 🔧 | Pre-Prompting 🎨 |
|------------------|--------------|----------------|
| Customization    | ✅ High       | ⚠️ Medium       |
| Training Needed  | ✅ Yes        | ❌ No          |
| Speed           | ⚠️ Slow       | ✅ Fast        |
| Cost            | 💰 Expensive  | 💲 Cheap       |

---

## 🛠️ **Project Pipeline**

Below is the **step-by-step** workflow of our project:  

```mermaid
graph TD;
    A[📄 Image/Text Input] --> B[🔍 Object Detection (OCR)];
    B --> C[📊 Image Classification];
    C --> D[🤖 LLM for Math Creativity & Correction];
    D --> E[✅ Final Result: Creativity & Correctness];
```

**Pipeline Breakdown**:
1️⃣ **OCR** extracts math expressions & numbers from test sheets.  
2️⃣ **Image classification** analyzes structure & neatness.  
3️⃣ **LLM** assesses **correctness** and **creativity** of responses.  
4️⃣ **Final result** is displayed with explanations.  

---

## 📸 **Using Qari-OCR for OCR**

We use **Qari-OCR**, a powerful OCR model, to extract text from images. 🖼️🔍  

```python
!pip install transformers qwen_vl_utils accelerate>=0.26.0 PEFT -U
!pip install -U bitsandbytes

from PIL import Image
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
import torch
import os
from qwen_vl_utils import process_vision_info

model_name = "NAMAA-Space/Qari-OCR-0.1-VL-2B-Instruct"
model = Qwen2VLForConditionalGeneration.from_pretrained(model_name, torch_dtype="auto", device_map="auto")
processor = AutoProcessor.from_pretrained(model_name)
max_tokens = 2000

# Load an image
image_path = "test_paper.png"
image = Image.open(image_path)
src = "image.png"
image.save(src)

# Define a prompt
prompt = "Extract all numbers and math expressions from this image."

# Prepare input
messages = [{"role": "user", "content": [{"type": "image", "image": f"file://{src}"}, {"type": "text", "text": prompt}]}]
text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(text=[text], images=image_inputs, videos=video_inputs, padding=True, return_tensors="pt").to("cuda")

# Generate output
generated_ids = model.generate(**inputs, max_new_tokens=max_tokens)
output_text = processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
os.remove(src)
print(output_text)
```

💡 *This script processes test papers to extract math problems automatically!* 🤖📜

---

## 📊 **Fine-Tuning for Math Creativity & Correction**

**🛠 Goal:**  
- ✅ Detect mathematical creativity.  
- ✅ Evaluate correctness of student responses.  

### 📂 **Dataset & Annotations**
We will create a **custom dataset** based on **student responses**:  
- **Correctness** → Correct ✅ / Incorrect ❌  
- **Creativity** → Score from **1 to 10** 🎨  

Example JSON format:  
```json
{
  "image": "path/to/image.png",
  "text": "Extract the question and answer.",
  "labels": {
    "correctness": "correct",
    "creativity": "8"
  }
}
```

---

## 🚀 **Next Steps**

✅ **1. Collect Data** → Label responses with correctness & creativity scores.  
✅ **2. Test OCR** → Ensure accurate text extraction.  
✅ **3. Fine-Tune Model** → Train it on creative math answers.  
✅ **4. Evaluate Results** → Compare with human judgment.  
✅ **5. Deploy & Improve** → Make it useful for teachers! 👩‍🏫👨‍🏫  

---

🎉 *This project has great potential to enhance how we assess children's mathematical abilities!*  

📢 **Stay tuned for updates! 🚀**  
