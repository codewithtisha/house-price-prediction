from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None
    error = None

    if request.method == "POST":

        try:

            bedrooms = float(request.form["bedrooms"])
            bathrooms = float(request.form["bathrooms"])
            sqft_living = float(request.form["sqft_living"])
            floors = float(request.form["floors"])

            waterfront = 1 if request.form["waterfront"] == "Yes" else 0

            sqft_lot = float(request.form["sqft_lot"])
            yr_built = float(request.form["yr_built"])
            yr_renovated = float(request.form["yr_renovated"])
            schools_nearby = float(request.form["schools_nearby"])
            airport_distance = float(request.form["airport_distance"])

            features = np.array([[
                bedrooms,
                bathrooms,
                sqft_living,
                floors,
                waterfront,
                sqft_lot,
                yr_built,
                yr_renovated,
                schools_nearby,
                airport_distance
            ]])

            # model.predict() returns a 2D array, e.g. [[1171681.89]],
            # so flatten it down to a single scalar before doing anything else
            raw_result = model.predict(features)
            prediction = float(np.ravel(raw_result)[0])

        except Exception as e:

            print("Prediction Error:", e)
            error = "Something went wrong while predicting. Please check your inputs and try again."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
