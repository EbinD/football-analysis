import joblib
import numpy as np

# Load model and feature columns
model = joblib.load("model/random_forest_goals_model.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")

# Example player data: [same order as feature_columns]
# Manually create a test input matching the feature list
sample_player = {
    'goals_per_appearance': 0.4,
    'minutes_played_overall': 2500,
    'appearances_overall': 30,
    'minutes_per_appearance': 83.3,
    'assists_overall': 6,
    'age_squared': 625,
    'assists_per_appearance': 0.2,
    'age': 25,
    'position_Forward': 1,
    'is_forward': 1,
    'position_Midfielder': 0,
    'position_Goalkeeper': 0
}

# Fill all missing features with 0
input_data = [sample_player.get(col, 0) for col in feature_columns]

# Reshape for prediction
input_array = np.array(input_data).reshape(1, -1)

# Predict goals
predicted_goals = model.predict(input_array)[0]

# Print result
print(f"Predicted goals: {predicted_goals:.2f}")
