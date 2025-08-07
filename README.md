# ⚽ Football Player Goals Prediction

A machine learning web app that predicts total goals scored by a football player using career stats like appearances, minutes, assists, and position.

---

## 🚀 App Demo

🔗 [Live App on Streamlit](https://football-analysis-jfdzw8bllcprmno2puervg.streamlit.app/)

---

## 📁 Project Structure

- `app.py`: Streamlit frontend for user inputs and prediction
- `model/`: Contains the trained Random Forest model (`.pkl`)
- `data/`: Raw and cleaned player statistics
- `notebooks/`: EDA, feature engineering, and modeling notebooks

---

## 📊 Data Overview

- Source: [Footstats 2018/19 Dataset](#)
- Players: 570
- Features: Appearances, goals, assists, minutes, nationality, position, etc.

---

## 📈 Model Details

- Type: Random Forest Regressor
- Input features: 12 engineered stats
- Output: Predicted total career goals

---

## 🛠 Features

- Cleaned & engineered dataset
- Exploratory Data Analysis (EDA)
- Random Forest training & evaluation
- Feature importance analysis
- Web app with interactive input form
- Deployed using Streamlit Cloud

---

## 🧠 Example Use

> *"If a midfielder played 1500 minutes with 5 assists and 20 appearances, how many goals would they likely score?"*

---

## 📌 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
