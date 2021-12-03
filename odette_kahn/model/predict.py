import os

import joblib
import numpy as np

from odette_kahn.api import db

MODELS_PATH = os.environ['MODELS_PATH']

properties_names = [
    "fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide",
    "total_sulfur_dioxide", "density", "ph", "sulphates", "alcohol", "quality"
]


def predict_from_name(wine_name: str):
    model = joblib.load(MODELS_PATH + "/wine_sdg_model.pkl")
    properties, quality = db.get_wine_properties_and_quality(wine_name, properties_names)
    predict = model.predict(np.array(properties).reshape(1, -1))[0]
    answer = dict(zip(properties_names + ['predicted'], properties + [quality] + [predict]))
    print(answer)
    return answer
