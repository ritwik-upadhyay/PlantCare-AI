from flask import Flask, render_template, request, session, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
import os
import secrets

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", secrets.token_hex(16))

# Folder configuration
UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["STATIC_FOLDER"] = STATIC_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024

# Create folders if not exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.join(STATIC_FOLDER, "images"), exist_ok=True)

# Load trained model
model = load_model("mobilenetv2_best.keras", compile=False)

LABELS_PATH = "labels.txt"

def load_labels():
    if os.path.exists(LABELS_PATH):
        with open(LABELS_PATH, "r", encoding="utf-8") as f:
            labels = [line.strip() for line in f if line.strip()]
        if labels:
            return labels
    # Fallback if no labels file provided
    return [f"Class {i}" for i in range(38)]


class_labels = load_labels()


def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)

    confidence = float(np.max(prediction))
    label = class_labels[class_index] if class_index < len(class_labels) else f"Class {class_index}"

    return label, confidence


def parse_label(label):
    if "___" in label:
        plant, condition = label.split("___", 1)
    elif "__" in label:
        plant, condition = label.split("__", 1)
    else:
        plant, condition = label, "Unknown"
    plant_display = plant.replace("_", " ").strip()
    condition_display = condition.replace("_", " ").strip()
    is_healthy = "healthy" in condition_display.lower()
    return plant_display, condition_display, is_healthy


@app.route("/")
def upload():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/upload")
def upload_page():
    return render_template("upload.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return render_template("upload.html", error="No file uploaded."), 400

    file = request.files["file"]

    if file.filename == "":
        return render_template("upload.html", error="No file selected."), 400

    allowed_ext = {".jpg", ".jpeg", ".png", ".webp"}
    _, ext = os.path.splitext(file.filename.lower())
    if ext not in allowed_ext:
        return render_template("upload.html", error="Please upload a JPG, PNG, or WebP image."), 400

    if file:

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        file.save(filepath)

        try:
            prediction, confidence = predict_image(filepath)

            # Save image for display
            static_filename = f"upload_{secrets.token_hex(8)}.jpg"
            static_path = os.path.join(app.config["STATIC_FOLDER"], "images", static_filename)

            Image.open(filepath).convert("RGB").save(static_path, format="JPEG", quality=92)

            # Save in session
            session["prediction"] = prediction
            session["confidence"] = confidence
            session["image_path"] = f"images/{static_filename}"

            os.remove(filepath)

            return redirect(url_for("result"))

        except Exception as e:

            if os.path.exists(filepath):
                os.remove(filepath)

            return render_template("upload.html", error="Something went wrong. Please try again."), 500


@app.route("/result")
def result():

    prediction = session.get("prediction")
    confidence = session.get("confidence")
    image_path = session.get("image_path")

    if not prediction:
        return redirect(url_for("upload"))

    plant_type, condition, is_healthy = parse_label(prediction)
    if is_healthy:
        status = "Healthy Plant"
        tips = [
            "Continue regular watering and care.",
            "Ensure adequate sunlight and nutrients.",
            "Monitor for any changes in appearance.",
            "Maintain good air circulation."
        ]
    else:
        status = "Disease Detected"
        tips = [
            "Isolate affected plants to prevent spread.",
            "Remove and dispose of infected leaves.",
            "Consider appropriate treatment methods.",
            "Monitor nearby plants for similar symptoms."
        ]

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence,
        image_path=image_path,
        plant_type=plant_type,
        condition=condition,
        is_healthy=is_healthy,
        status=status,
        tips=tips
    )


if __name__ == "__main__":
    app.run()
