import joblib

model = joblib.load("model.pkl")

def predict(sepal_length,
            sepal_width,
            petal_length,
            petal_width):

    prediction = model.predict([[

        sepal_length,
        sepal_width,
        petal_length,
        petal_width

    ]])

    return prediction[0]