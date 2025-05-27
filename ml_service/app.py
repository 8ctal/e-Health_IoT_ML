from flask import Flask, request
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = [data["hr"], data["sys"], data["dia"]]
    prediction = model.predict([features])[0]
    return {"alert": bool(prediction)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)