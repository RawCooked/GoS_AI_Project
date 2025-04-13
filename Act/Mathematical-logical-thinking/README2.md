# 🧠 Math Creativity Detector

A deep learning pipeline that extracts mathematical expressions from handwritten images, verifies the correctness of answers, and evaluates creativity using a **BERT-based NLP model**. This project is designed for analyzing children's mathematical problem-solving approaches (ages 5-10). 🚀

---

## 📌 Features
✅ **OCR Processing** – Extracts handwritten text and equations from images using Tesseract OCR.  
✅ **Mathematical Verification** – Solves equations and checks if the given answer is correct.  
✅ **Creativity Detection** – Uses a fine-tuned BERT model to classify responses as **Creative** or **Non-Creative**.  
✅ **End-to-End Pipeline** – Combines text extraction, answer verification, and creativity assessment.  

---

## 📂 Project Structure
```bash
📁 Math-Creativity-Detector
│── 📂 models            # Pre-trained BERT models
│── 📂 data              # Sample images and datasets
│── 📂 src               # Source code
│    │── ocr.py         # OCR extraction module
│    │── solver.py      # Equation solver
│    │── bert_model.py  # Creativity detection with BERT
│    │── main.py        # Full pipeline execution
│── README.md           # Project documentation
│── requirements.txt    # Python dependencies
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Math-Creativity-Detector.git
cd Math-Creativity-Detector
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Install Tesseract OCR
**Windows:** Download from [here](https://github.com/UB-Mannheim/tesseract/wiki) and add to PATH.  
**Linux/macOS:**
```bash
sudo apt install tesseract-ocr
```

---

## 🛠️ Usage
Run the full pipeline on an image containing handwritten math responses:
```bash
python src/main.py --image path/to/your/image.jpg
```

Example output:
```
Extracted Text: "I used a drawing to solve 5 + 3 = 8"
Extracted Equation: "5 + 3 = 8"
Correctness: ✅ Correct
Creativity Classification: 🎨 Creative
```

---

## 🧑‍💻 Contributing
We welcome contributions! To contribute:
1. **Fork** the repo.
2. **Create a branch** for your feature (`git checkout -b feature-name`).
3. **Commit your changes** (`git commit -m 'Added new feature'`).
4. **Push** to your branch (`git push origin feature-name`).
5. **Open a pull request** 🚀.

---

## 📝 License
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 📬 Contact
For questions or feedback, reach out at **your.email@example.com** or open an issue!

⭐ **If you like this project, don't forget to star the repo!** ⭐

