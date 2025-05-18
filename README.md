# GoS\_AI\_Project

## 🧠 Overview

**GoS\_AI\_Project** is a deep learning system combining **image classification** and **object detection**. Designed for smart educational or security applications, this project uses powerful neural networks to recognize and detect objects in images, with a focus on deployment efficiency and accuracy.

---

## ✨ Features

* ✅ Image classification using pretrained CNN models (ResNet, VGG16, MobileNet)
* 🎯 Image Classification with custom datasets
* 📊 Performance metrics visualization (Accuracy, F1-Score, etc.)
* 🧠 Future-ready with support for self-supervised learning and edge deployment

---

## 🛠️ Tech Stack

### 🔹 Frontend

* **Angular** (for future real-time monitoring dashboard or visual results display)

### 🔹 Backend

* **Django** (REST API for serving predictions and managing models)

### 🔹 Deep Learning Frameworks

* **TensorFlow** / **Keras**
* **PyTorch**

### 🔹 Other Tools

* OpenCV – Image manipulation
* Matplotlib, Seaborn – Visualization
* Pandas, NumPy – Data manipulation
* Scikit-learn – Evaluation metrics
* Flask / FastAPI – Lightweight deployment
* Unsloth / LoRA – LLM fine-tuning
* Ollama – Advanced language model fine-tuning and inference

---

## 🚀 Getting Started

### Prerequisites

* **Node.js** (v18+)
* **Python** (v3.10+)
* **Django** (v4+)
* **Angular CLI** (v15+)

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/RawCooked/GoS_AI_Project.git
cd GoS_AI_Project
```

2. **Backend Setup**

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

3. **Frontend Setup**

```bash
cd ../frontend
npm install
ng serve
```

4. **Access the App**
   Open `http://localhost:4200` in your browser for the frontend and `http://localhost:8000` for the backend.

### 2️⃣ GitHub Organization

This is how this repo is organized:

```
/dataset
     /Act
          /Artistical-talent-detection
               /Datasets
               /Notebooks
          /Mathematical-logical-thinking
               /Notebooks
          /Singing-talent-detection
               /Notebooks
               /Datasets
                    /Audio-Preview
     /Engage
     /Investigate
```

---

## 🚧 Future Improvements

* 📚 Self-supervised learning for semi-labeled datasets
* ⚡ Real-time optimization (quantization, pruning)
* 🧠 Edge deployment on Raspberry Pi
* 🔋 Energy-efficient architectures

---

## 🙌 Acknowledgments

* Inspired by **Our Dear Professors** (❁´◡\`❁) & **Personal Experiences**
* Special thanks to **ESPRIT School of Engineering** for their continuous support and guidance

---

## 👥 Authors

* **Idriss Ben Moussa (RawCooked)** | [GitHub](https://github.com/RawCooked)
* **Achref Baaboura** | [GitHub](https://github.com/Baaboura)
* **Khalil Tombari** | [GitHub](https://github.com/khalilou123)
* **Heni Ouerfelli** | [GitHub](https://github.com/RawCooked)
* **Maha Mansi** | [GitHub](https://github.com/MahaMensi)
* **Azer Fattouch** | [GitHub](https://github.com/RawCooked)
