import numpy as np
import pickle
import os
from sklearn.tree import DecisionTreeClassifier

MODEL_PATH = "model/decision_tree.pkl"

def train_and_save_model():
    # Real-life inspired dataset
    X = np.array([
        [25, 25000, 1, 2, 2,0],
        [28, 30000, 2, 3, 3,0],
        [35, 60000, 6, 4, 4,0],
        [45, 80000, 15, 5, 4,1],
        [30, 28000, 2, 2, 2,1],
        [32, 40000, 4, 3, 3,1],
        [26, 26000, 1, 1, 1,1],
        [40, 75000, 10, 4, 3,1],
        [29, 32000, 3, 2, 2,0],
        [50, 90000, 20, 5, 5,1]
    ])

    # 1 = Leave, 0 = Stay
    y = np.array([1, 0, 0, 0, 1, 0, 1, 0, 1, 0])

    model = DecisionTreeClassifier(max_depth=4)
    model.fit(X, y)

    os.makedirs("model", exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved automatically")
    return model


def load_model():
    if not os.path.exists(MODEL_PATH):
        print("⚠️ Model not found. Training model...")
        return train_and_save_model()

    with open(MODEL_PATH, "rb") as f:
        print("✅ Model loaded from disk")
        return pickle.load(f)
