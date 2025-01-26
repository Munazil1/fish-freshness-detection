from flask import Flask, render_template, request, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)

# Load your model (update the path if needed)
model = load_model(r"C:\Users\Munazil\OneDrive\Documents\project\fisheye\web_app\model.h5")

# Route for upload page
@app.route('/')
@app.route('/upload')
def upload():
    return render_template('upload.html')

# Route to handle prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('upload'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('upload'))

    if file:
        # Save uploaded file temporarily
        filepath = os.path.join('static', file.filename)
        file.save(filepath)

        # Preprocess the image
        img = load_img(filepath, target_size=(224, 224))  # Adjust size if needed
        img = img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        # Make prediction
        prediction = model.predict(img)
        result_message = "The fish is not fresh." if prediction[0][0] > 0.5 else "The fish is fresh."

        # Remove temporary file
        os.remove(filepath)

        return render_template('result.html', result_message=result_message)

if __name__ == "__main__":
    app.run(debug=True)
