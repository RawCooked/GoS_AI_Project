# 📝 Survey Paper: Cognitive and Creative Talent Assessment for Children

## 1. Introduction
The development of cognitive and creative talents in children is critical for shaping their future potential. This project aims to build a system that objectively evaluates children's talents across three domains: mathematical-logical intelligence, artistic skills, and musical abilities. By leveraging deep learning and large language models, we aim to automate talent assessment and provide actionable insights to teachers and parents.

## 2. Project Motivation and Goals
- Detect cognitive and creative talents early to personalize education.
- Offer objective, data-driven evaluation in math, drawing, and singing.
- Develop an integrated tool that supports teachers and parents with detailed feedback.

## 3. Overview of the Three Talent Domains

### 3.1 Mathematical-Logical Intelligence
- Analyze children's math exercise responses.
- Detect not only correctness but also creative problem-solving approaches.
- Focus on non-traditional methods and logical reasoning.

### 3.2 Artistic Talent
- Evaluate children's creativity through analysis of drawings.
- Focus on composition, use of colors, originality, and expression.

### 3.3 Musical Talent
- Assess children's musical performances via audio recordings.
- Analyze pitch, rhythm, timing, and expressiveness.

## 4. Current Work and Progress

### 4.1 Mathematical-Logical Intelligence Branch
- Fine-tuned multiple LLMs: `LLaMA 3`, `Mistral 7B`, `Qwen`, and `TinyLLaMA`.
- Compared LLaMA-based models to BERT models (early tests showed LLaMA's superiority).
- Logged unsuccessful trials with BERT and Gemini API to reflect learning.
- Organized initial models under clear notebooks and directory structure.

### 4.2 Artistic Talent Detection Branch
- Built drawing classification pipelines using `MobileNetV2` and `EfficientNetB0`.
- Combined deep learning vision models with GPT-4o prompting to enrich creativity evaluation.
- Set up an initial dataset and documentation for artistic data.

### 4.3 Musical Talent Detection Branch
- Developed preliminary models using `CNN-LSTM` architectures.
- Experimented with `Wav2Vec2 + MLP` to capture audio features.
- Collected basic dataset examples ("belle voix" vs "non belle voix").

## 5. Future Work

### 5.1 Mathematical Branch
- Fine-tune and finalize the best model (likely LLaMA or Mistral).
- Implement creativity score evaluation in addition to correctness.
- Improve prompt engineering for complex reasoning cases.

### 5.2 Artistic Branch
- Expand dataset with wider age groups and drawing themes.
- Introduce multi-label classification (e.g., creativity + composition + color usage).
- Optionally explore transformer-based vision models (e.g., ViT).

### 5.3 Musical Branch
- Collect more diverse and longer singing recordings.
- Add rhythmic and tempo analysis to complement pitch evaluation.
- Prepare a simple real-time evaluation demo.

### 5.4 Deployment and Integration
- Integrate math, art, and music evaluation into a single web-based application.
- Deploy lightweight versions of models (pruned or quantized).
- Generate child-specific evaluation reports.

## 6. Conclusion
The initial results are promising across all three domains. With further polishing, larger datasets, and final integration, the project could serve as a powerful tool to help teachers and parents nurture children's talents more effectively. Future work will focus on improving model performance, enriching datasets, and building a user-friendly deployment.

## 7. References
- [1] Vaswani et al., "Attention is All You Need," 2017.
- [2] He et al., "MobileNetV2: Inverted Residuals and Linear Bottlenecks," 2018.
- [3] Baevski et al., "wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations," 2020.
- [4] Various HuggingFace and Kaggle datasets used for prototyping.
