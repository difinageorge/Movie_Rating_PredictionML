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
## 🧪 Example Predictions

| 🎬 **Film Name** | 🎥 **Director**   | 👥 **Actors**                                       | 🎭 **Genre** | ⭐ **Actual IMDb Rating** | 🔮 **Predicted Rating** |
| ---------------- | ----------------- | --------------------------------------------------- | ------------ | ------------------------ | ----------------------- |
| Inception        | Christopher Nolan | Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page | Sci-Fi       | 8.8                      | \~8.6                   |
| The Room         | Tommy Wiseau      | Tommy Wiseau, Greg Sestero, Juliette Danielle       | Drama        | 3.7                      | \~3.9                   |
| Titanic          | James Cameron     | Leonardo DiCaprio, Kate Winslet, Billy Zane         | Romance      | 7.8                      | \~7.6                   |
| PK               | Rajkumar Hirani   | Aamir Khan, Anushka Sharma, Saurabh Shukla          | Comedy       | 8.1                      | \~8.0                   |
| Baaghi 3         | Ahmed Khan        | Tiger Shroff, Riteish Deshmukh, Shraddha Kapoor     | Action       | 2.1                      | \~2.5                   |

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
