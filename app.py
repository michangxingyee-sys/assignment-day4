import streamlit as st
from src.inference import predict

st.title("Iris Flower Prediction")

st.write("Enter flower measurements")

sepal_length = st.number_input("Sepal Length", 4.0, 8.0, 5.1)
sepal_width = st.number_input("Sepal Width", 2.0, 5.0, 3.5)
petal_length = st.number_input("Petal Length", 1.0, 7.0, 1.4)
petal_width = st.number_input("Petal Width", 0.1, 3.0, 0.2)

if st.button("Predict"):

    result = predict(
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    )

    st.success(f"Predicted species: {result}")