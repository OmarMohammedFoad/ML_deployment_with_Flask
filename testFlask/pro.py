import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, request

IMG_SIZE = (256, 256)
THRESHOLD = 0.5
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

model = tf.keras.models.load_model("./imageclassifier.h5", compile=False)
app = Flask(__name__)


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess(file_bytes: bytes) -> np.ndarray:
    buffer = np.frombuffer(file_bytes, np.uint8)
    img_bgr = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
    if img_bgr is None:
        raise ValueError("Invalid image")
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    resized = tf.image.resize(img_rgb, IMG_SIZE)
    return np.expand_dims(resized / 255.0, 0)


@app.route("/api/predict", methods=["POST"])
def predict():
    file = request.files.get("image")
    if file is None or file.filename == "":
        return jsonify({"error": "No image provided"}), 400
    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file type"}), 400

    try:
        batch = preprocess(file.read())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    sad_probability = float(model.predict(batch, verbose=0)[0][0])
    is_sad = sad_probability > THRESHOLD

    return jsonify({
        "label": "sad" if is_sad else "happy",
        "confidence": round(sad_probability if is_sad else 1 - sad_probability, 4),
    })


if __name__ == "__main__":
    app.run()