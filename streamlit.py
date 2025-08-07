import streamlit as s
import numpy as np
import pandas as pd
import pickle as pkl
from predictions import predict

s.title("Titanic Survival Prediction")

input_cabin_int = s.number_input("What is the cabin by interger?")

input_gender = s.number_input("What is the gender in interger(0 = female, 1 = male)?")

input_pclass = s.number_input("What is the passenger class by interger?")

input_age = s.number_input("What is the age?")

input_sib = s.number_input("If they had siblings, please enter 1. If not, enter 0.")

input_par = s.number_input("If they had children, please enter 1. If not, enter 0.")


if s.button("Predict"):
    result = predict(np.array([[int(input_cabin_int), int(input_gender), int(input_pclass), int(input_age), int(input_sib), int(input_par)]]))
    if result == 0:
        s.text("The person did not survive.")
    else:
        s.text("The person did survive.")
