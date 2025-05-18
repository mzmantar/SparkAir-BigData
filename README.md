# 🌀 SparkAir – BigData

Predictive analytics pipeline to forecast air‑quality pollutants (NO₂, CO, O₃) at scale using **Apache Spark**, **PySpark ML**, and a multi‑output **Random Forest** model packaged in Docker.

---

## 📑 Table of Contents
1. [Project Overview](#project-overview)  
2. [Architecture](#architecture)  
3. [Quick Start](#quick-start)  
4. [Repository Structure](#repository-structure)  
5. [Usage](#usage)  
6. [Model Evaluation](#model-evaluation)  

---

## 🌍 Project Overview

**SparkAir – BigData** is a scalable predictive system to monitor air quality based on chemical sensor readings.

The model predicts three key air pollutants:  
- **NO₂** (Nitrogen Dioxide)  
- **CO** (Carbon Monoxide)  
- **O₃** (Ozone)

---

## 🏗️ Architecture

- 🐳 Dockerized Spark environment  
- 🧠 Random Forest model using `MultiOutputRegressor`  
- 📦 Model serialized in `.pkl` using `joblib`  
- 🧪 Evaluation via `RMSE` and `R²`  
- ⚙️ Deployable with `docker-compose`

---

## 🚀 Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/mzmantar/SparkAir-BigData.git
   cd sparkair-bigdata
   ```

2. Build and run with Docker:
   ```bash
   docker-compose up --build
   ```

3. Output predictions and model evaluation will appear in the container logs.

---

## 📁 Repository Structure

```
app/
├── main.py                 # Main execution script
├── random_forest_model.pkl # Trained model
├── Data1.csv               # Sensor input data
Dockerfile
docker-compose.yml
README.md
```

---

## ⚙️ Usage

Edit `main.py` to:
- Switch between prediction modes (CSV batch vs single input)
- Update test data or load new models
- Export results if needed

To run in local Python:
```bash
python3 app/main.py
```

---

## 📊 Model Evaluation

The model was trained using:
- MultiOutputRegressor(RandomForest)
- RMSE ≈ 0.05 on test set  
- R² ≈ 0.88 (depending on pollutant)

---
## 📥 Model Download

The trained model file `random_forest_model.pkl` exceeds GitHub's size limit (100MB) and is not included in this repository.

🔗 **[Download the model file here](https://drive.google.com/file/d/1-S0UTSqR-w-JDVPWVab0KEpP5_apWYuS/view?usp=sharing)**  
→ Place it inside the `app/` directory before running the project.
