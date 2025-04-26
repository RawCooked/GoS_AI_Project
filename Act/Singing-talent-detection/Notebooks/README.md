# Modèles

Ce répertoire contient les modèles et les notebooks associés pour la classification de la qualité vocale (belle voix vs non belle voix). Deux approches sont implémentées : une basée sur un CNN avec spectrogrammes Mel, et une autre utilisant Wav2Vec2 avec un MLP.

## Contenu

### Notebooks
- **notebook1.ipynb** : Classification avec un CNN et spectrogrammes Mel.
  - **Objectif** : Entraîner un modèle CNN pour classer des fichiers audio en "belle voix" ou "non belle voix".
  - **Étapes principales** :
    - Extraction de spectrogrammes Mel à partir de fichiers `.wav` (durée : 3s, taux d’échantillonnage : 22050 Hz).
    - Augmentation des données avec ajout de bruit.
    - Équilibrage des classes avec `RandomOverSampler`.
    - Entraînement d’un CNN avancé avec GRU (128 unités) et couches convolutives (64, 128, 256 filtres).
    - Évaluation avec métriques (accuracy, precision, recall, AUC) et visualisation (précision et perte par époque).
  - **Sortie** : Modèle entraîné sauvegardé (non spécifié dans le notebook, mais peut être ajouté).

- **notebook2.ipynb** : Classification avec Wav2Vec2 et MLP.
  - **Objectif** : Utiliser Wav2Vec2 pour extraire des caractéristiques audio et un MLP pour la classification.
  - **Étapes principales** :
    - Extraction de caractéristiques avec Wav2Vec2 (`facebook/wav2vec2-base-960h`) à partir de fichiers `.wav` (durée : 3s, taux d’échantillonnage : 16000 Hz).
    - Équilibrage des classes avec `RandomOverSampler`.
    - Entraînement d’un MLP (couches : 256, 128 neurones, dropout 0.3).
    - Évaluation avec accuracy sur l’ensemble de test.
  - **Sortie** : Modèle entraîné sauvegardé (non spécifié dans le notebook, mais peut être ajouté).

### Modèles
- Les modèles entraînés ne sont pas explicitement sauvegardés dans les notebooks. Pour les sauvegarder :
  - Dans `notebook1.ipynb`, ajoutez après l’entraînement :  
    ```python
    model.save("models/cnn_mel_model.h5")