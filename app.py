import streamlit as st
import joblib
import numpy as np

# Load model and feature columns
model = joblib.load("model/random_forest_goals_model.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")

st.title("⚽ Player Goals Predictor")
st.write("Enter player stats to predict total goals.")

# Input form
with st.form("player_form"):
    age = st.slider("Age", 16, 40, 25)
    minutes = st.number_input(
        "Minutes Played Overall", min_value=0, value=2000)
    appearances = st.number_input("Appearances Overall", min_value=1, value=25)
    assists = st.number_input("Assists Overall", min_value=0, value=5)
    position = st.selectbox(
        "Position", ["Forward", "Midfielder", "Goalkeeper"])

    submit = st.form_submit_button("Predict Goals")

    if submit:
        # Feature engineering
        goals_per_appearance = 5  # Unknown for prediction
        minutes_per_appearance = minutes / appearances
        age_squared = age ** 2
        assists_per_appearance = assists / appearances

        # One-hot encoding
        position_forward = int(position == "Forward")
        position_midfielder = int(position == "Midfielder")
        position_goalkeeper = int(position == "Goalkeeper")
        is_forward = position_forward

        # Build the feature dict
        input_dict = {
            'goals_per_appearance': goals_per_appearance,
            'minutes_played_overall': minutes,
            'appearances_overall': appearances,
            'minutes_per_appearance': minutes_per_appearance,
            'assists_overall': assists,
            'age_squared': age_squared,
            'assists_per_appearance': assists_per_appearance,
            'age': age,
            'position_Forward': position_forward,
            'is_forward': is_forward,
            'position_Midfielder': position_midfielder,
            'position_Goalkeeper': position_goalkeeper
        }

        # Fill missing columns with 0
        input_data = [input_dict.get(col, 0) for col in feature_columns]
        input_array = np.array(input_data).reshape(1, -1)
# Predict
        predicted_goals = model.predict(input_array)[0]
        st.success(f"🏆 Predicted Total Goals: {predicted_goals:.2f}")
