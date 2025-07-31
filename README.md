# 🎬 Movie Rating Predictor using Machine Learning

This project was completed as part of my **GenAI Internship** at **System Tron** (Week01) . The objective of this task was to build and deploy a machine learning model that predicts the **IMDb rating** of a movie based on key attributes like **title, director, genre, and actors** using regression techniques.

---

## 🚀 Live Demo

You can check out the deployed Streamlit web app here:

🔗 [Movie Rating Prediction App – Streamlit Live](https://movie-rating-prediction-ml.streamlit.app/)

---

## 📌 Task Objective

Develop and deploy a **regression-based ML model** that can intelligently estimate the IMDb rating of a movie given its metadata. The final deliverable includes a **Streamlit-powered web application** that lets users enter movie details and instantly view the predicted rating.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* scikit-learn

  * Linear Regression
  * Label Encoding
  * Train-Test Split
  * Evaluation Metrics (`MSE`, `R² Score`)
* Jupyter Notebook
* Joblib (for model and encoder saving)

---

## 📁 Project Structure

```
movie-rating-predictor/
│
├── MovieRatingPrediction.ipynb   # Jupyter Notebook for model training and evaluation
├── movie_dataset.csv             # Cleaned dataset of movies with metadata
├── movie_rating_model.pkl        # Trained ML model (Linear Regression)
├── encoders.pkl                  # Saved LabelEncoders for categorical fields 
├── app.py                        # Streamlit web app for real-time predictions
├── README.md                     # Project documentation
```

---

## 🎞️ Dataset Description

The dataset includes a collection of movies with the following attributes:

* `Title`
* `Genre`
* `Director`
* `Actors`
* `Rating` (IMDb score, the target variable)

Key features used for prediction:

* Categorical columns encoded: `Title`, `Genre`, `Director`, `Actors`
* Regression target: `Rating` (continuous value between 1–10)

---

## 🔄 ML Workflow

1. Data preprocessing and null-value handling
2. Label encoding for all categorical fields
3. Feature and target separation
4. Model training using `LinearRegression`
5. Performance evaluation using `MSE` and `R² Score`
6. Saving model and encoders using `pickle`
7. Building an interactive web app using `Streamlit`

---

## 🖥️ Web App Features

* Enter movie **title**, **genre**, **director**, and **actors**
* Submit and get the **predicted IMDb rating** instantly
* Displays both the predicted rating and actual rating (for known test cases)
* Simple and clean UI for easy testing and demonstration

---

## 📷 Screenshot

> *Include screenshots of your Streamlit app here (optional)*
- **Before**
> ![App Screenshot](SS01.png)
> 
- **After**
> ![App Screenshot](SS02.png)

---
### 🎬 Sample Indian Movies for Model Testing (Across Years)

These randomly selected Indian movies span different years and genres, suitable for testing the ML model:

| 🎥 Movie Title         | 📅 Year | 🎭 Genre                 | ⭐ Rating | 🎬 Director              | 👤 Lead Actor         |
|------------------------|--------|--------------------------|----------|--------------------------|------------------------|
| Kabhi Haan Kabhi Naa   | 1994   | Comedy, Drama, Romance   | 7.8      | Kundan Shah              | Shah Rukh Khan         |
| Lagaan                 | 2001   | Drama, Musical, Sport    | 8.1      | Ashutosh Gowariker       | Aamir Khan             |
| Black Friday           | 2004   | Crime, Drama, History    | 8.4      | Anurag Kashyap           | Kay Kay Menon          |
| Bhool Bhulaiyaa        | 2007   | Comedy, Horror, Mystery  | 7.4      | Priyadarshan             | Akshay Kumar           |
| 3 Idiots               | 2009   | Comedy, Drama            | 8.4      | Rajkumar Hirani          | Aamir Khan             |
| Barfi!                 | 2012   | Comedy, Drama, Romance   | 8.1      | Anurag Basu              | Ranbir Kapoor          |
| Queen                  | 2014   | Adventure, Comedy, Drama | 8.2      | Vikas Bahl               | Kangana Ranaut         |
| Andhadhun              | 2018   | Crime, Drama, Music      | 8.2      | Sriram Raghavan          | Ayushmann Khurrana     |
| Shershaah              | 2021   | Action, Biography, Drama | 8.4      | Vishnuvardhan            | Sidharth Malhotra      |
| Pathaan                | 2023   | Action, Adventure, Thriller | 6.9   | Siddharth Anand          | Shah Rukh Khan         |


> ✅ You can test these inputs in the Streamlit app to compare predictions with real IMDb ratings!

---

## 🔧 Future Scope

* Upgrade to ensemble models (e.g., RandomForest, XGBoost) for better accuracy
* Add more features: year, runtime, budget, country, language, etc.
* Use embeddings for text-based fields (actors, genres)
* Deploy online using Streamlit Cloud, Hugging Face, or Render
* Add movie poster fetch API and ratings comparison chart

---

## 🎓 Internship & Task Details

* **Internship Track**: Generative AI & Machine Learning
* **Internship Provider**: System Tron
* **Week**: Week 01
* **Task Name**: Movie Rating Prediction Model
* **Environment**: Jupyter Notebook + Streamlit Web App 

---

## 📬 Contact

* **Difina George**
* 📧 [Gmail](difina.georgecs@gmail.com)
* 📍 Kerala, India
