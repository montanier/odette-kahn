import os

import joblib
import numpy as np

from odette_kahn.api import db

MODELS_PATH = os.environ['MODELS_PATH']

properties_names = [
    "fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar", "chlorides", "free_sulfur_dioxide",
    "total_sulfur_dioxide", "density", "ph", "sulphates", "alcohol"
]


def predict_from_name(wine_name: str):
    model = joblib.load(MODELS_PATH + "/wine_sdg_model.pkl")
    properties, quality = db.get_wine_properties_and_quality(wine_name, properties_names + ["quality"])
    predict = model.predict(np.array(properties).reshape(1, -1))[0]
    answer = dict(zip(properties_names + ['quality', 'predicted'], properties + [quality, predict]))
    return answer


def predict_from_properties(properties: dict):
    model = joblib.load(MODELS_PATH + "/wine_sdg_model.pkl")
    properties_values = [properties[key] for key in properties_names]
    predict = model.predict(np.array(properties_values).reshape(1, -1))[0]
    answer = dict(zip(properties_names + ['predicted'], properties_values + [predict]))
    return answer
