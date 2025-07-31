import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Title
st.title("🎥 IMDb India Movie Rating Predictor")

# Load model and encoders
model = joblib.load('movie_rating_model.pkl')
le_genre = joblib.load('genre_encoder.pkl')
le_director = joblib.load('director_encoder.pkl')
le_actors = joblib.load('actors_encoder.pkl')

# Load dataset
df = pd.read_csv('Movies_India.csv', encoding='latin1')
df.fillna('Unknown', inplace=True)

# Combine actor columns
df['Actors'] = df[['Actor 1', 'Actor 2', 'Actor 3']].astype(str).agg(' '.join, axis=1)

# Movie list for dropdown
movie_titles = sorted(df['Name'].unique())

# --- UI ---
selected_movie = st.selectbox("🎬 Select a movie", movie_titles)
predict_button = st.button("🔍 Show Details & Predict Rating")

# --- On Submit ---
if predict_button:
    movie_row = df[df['Name'] == selected_movie].iloc[0]

    # Extract details
    director = movie_row['Director']
    actor1 = movie_row['Actor 1']
    actor2 = movie_row['Actor 2']
    actor3 = movie_row['Actor 3']
    genre = movie_row['Genre']
    actual_rating = movie_row['Rating']
    actors = f"{actor1} {actor2} {actor3}"

    # Display Movie Info
    st.subheader("📄 Movie Details")
    st.markdown(f"**🎬 Title:** {selected_movie}")
    st.markdown(f"**🎭 Genre:** {genre}")
    st.markdown(f"**🎬 Director:** {director}")
    st.markdown(f"**👤 Actor 1:** {actor1}")
    st.markdown(f"**👤 Actor 2:** {actor2}")
    st.markdown(f"**👤 Actor 3:** {actor3}")
    st.markdown(f"**⭐ Actual IMDb Rating:** {actual_rating}")

    # Handle Unseen Labels
    if genre not in le_genre.classes_ or director not in le_director.classes_ or actors not in le_actors.classes_:
        st.warning("⚠️ Cannot predict: one or more values (genre, director, or actors) were not seen during training.")
    else:
        # Encode
        genre_enc = le_genre.transform([genre])[0]
        director_enc = le_director.transform([director])[0]
        actors_enc = le_actors.transform([actors])[0]

        # Predict
        features = [[genre_enc, director_enc, actors_enc]]
        predicted_rating = model.predict(features)[0]

        # Show prediction
        st.subheader("🔮 Predicted IMDb Rating")
        st.success(f"{predicted_rating:.1f}")
