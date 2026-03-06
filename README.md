
🌿 PlantCare AI

Plant Disease Detection using Transfer Learning

PlantCare AI is a deep learning–powered web application that detects plant diseases from leaf images. The system uses Transfer Learning with MobileNetV2 to classify plant leaves and identify potential diseases. This project was developed as part of the SmartBridge Experiential Learning Program by a team of four students.

The goal of the project is to demonstrate how Artificial Intelligence and Computer Vision can assist agriculture by providing a simple and accessible disease detection tool.

⸻

📌 Features

• Upload plant leaf images through a web interface
• AI-based plant disease detection
• Deep learning model using MobileNetV2
• Fast predictions using TensorFlow/Keras
• Simple and clean web interface using Flask
• Lightweight and efficient architecture

⸻

🧠 Model Architecture

The project uses Transfer Learning with the MobileNetV2 convolutional neural network.

MobileNetV2 is a lightweight deep learning architecture optimized for image classification tasks. Instead of training a neural network from scratch, pretrained weights are used and fine-tuned for plant disease detection.

Key advantages:

• Faster training
• High accuracy with smaller datasets
• Reduced computational cost

⸻

🏗 System Architecture

User Uploads Image
        │
        ▼
Frontend (HTML + CSS)
        │
        ▼
Flask Backend (app.py)
        │
        ▼
Image Preprocessing
        │
        ▼
MobileNetV2 Model
        │
        ▼
Prediction Output
        │
        ▼
Result Displayed to User


⸻

📂 Project Structure

PlantCare-AI
│
├── app.py
├── requirements.txt
├── labels.txt
├── mobilenetv2_best.keras
│
├── docs
│   └── generate_technical_pdf.py
│
├── static
│   └── styles.css
│
├── templates
│   ├── home.html
│   ├── upload.html
│   ├── result.html
│   └── about.html
│
└── README.md


⸻

⚙️ Tech Stack

Programming Language

Python

Machine Learning

TensorFlow
Keras

Deep Learning Model

MobileNetV2

Backend

Flask

Frontend

HTML
CSS

Version Control

Git
GitHub

⸻

📊 Dataset

The model was trained on a dataset of plant leaf images, specifically focusing on tomato plant diseases.

The dataset contains images labeled as:

• Healthy leaves
• Diseased leaves

Each image is processed and mapped to a class label stored in labels.txt.

⸻

🔄 System Workflow

1️⃣ User uploads an image of a plant leaf.

2️⃣ Flask backend receives the image.

3️⃣ Image preprocessing is applied (resizing, normalization).

4️⃣ The processed image is passed to the MobileNetV2 model.

5️⃣ The model predicts the disease class.

6️⃣ The result is displayed on the result page.

⸻

🚀 Installation

Clone the repository:

git clone https://github.com/yourusername/PlantCare-AI.git
cd PlantCare-AI

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open in browser:

http://127.0.0.1:5000


⸻

📈 Results

The model achieved strong accuracy in identifying plant diseases using transfer learning. The system successfully predicts disease classes from plant leaf images with reliable performance.

⸻

🔮 Future Improvements

• Support for multiple plant species
• Larger dataset for better accuracy
• Cloud deployment
• Mobile application integration
• Disease treatment recommendations

⸻

👨‍💻 Team

This project was developed as part of the SmartBridge Experiential Learning Program by a team of four students.

⸻

📜 License

This project is intended for educational and research purposes.

📂 Project Development Files (As Per Templates)

The PlantCare AI project follows a structured directory layout to separate the frontend, backend, model, and documentation components. Each file plays a specific role in the development and execution of the application.

⸻

Backend Files

app.py

This is the main Flask application file.
It performs the following functions:
	•	Loads the trained MobileNetV2 model
	•	Handles HTTP routes
	•	Processes image uploads
	•	Preprocesses images before prediction
	•	Sends the image to the deep learning model
	•	Returns prediction results to the frontend

This file acts as the bridge between the web interface and the AI model.

⸻

Model Files

mobilenetv2_best.keras

This file contains the trained deep learning model used for plant disease detection.

Key details:
	•	Architecture: MobileNetV2
	•	Framework: TensorFlow / Keras
	•	Training method: Transfer Learning
	•	Purpose: Predict disease classes from plant leaf images.

⸻

labels.txt

This file contains the class labels used by the model.

Example:

Healthy
Tomato Early Blight
Tomato Late Blight
Tomato Leaf Mold

The model outputs numerical predictions which are mapped to readable disease names using this file.

⸻

Frontend Templates

The templates folder contains the HTML pages used for the web interface.

templates/home.html
	•	Landing page of the application
	•	Introduces the PlantCare AI system
	•	Provides navigation to the upload page

⸻

templates/upload.html
	•	Allows users to upload plant leaf images
	•	Sends the uploaded image to the Flask backend for prediction

⸻

templates/result.html
	•	Displays the prediction result
	•	Shows the predicted plant disease or healthy status

⸻

templates/about.html
	•	Provides information about the project
	•	Describes the purpose and background of PlantCare AI

⸻

Static Files

static/styles.css

This file contains the CSS styling used for the frontend pages.

It controls:
	•	Layout
	•	Fonts
	•	Colors
	•	UI styling
	•	Page responsiveness

⸻

Documentation Files

docs/generate_technical_pdf.py

This script is used to generate the technical documentation PDF for the project.

It automatically creates a structured document containing:
	•	Project overview
	•	Architecture
	•	Model explanation
	•	Workflow
	•	Future improvements

⸻

Dependency Management

requirements.txt

This file contains all the Python dependencies required to run the project.

Example libraries:

Flask
TensorFlow
Keras
NumPy
Pillow

Users can install all dependencies using:

pip install -r requirements.txt


⸻

Configuration Files

.gitignore

Specifies files that should not be uploaded to GitHub, such as:
	•	cache files
	•	system files
	•	temporary files

⸻

.python-version

Specifies the Python version used for the project to maintain environment compatibility.

⸻

📁 Overall Project Structure

PlantCare-AI
│
├── app.py
├── mobilenetv2_best.keras
├── labels.txt
├── requirements.txt
│
├── docs
│   
│
├── static
│   └── styles.css
│
├── templates
│   ├── home.html
│   ├── upload.html
│   ├── result.html
│   └── about.html
│
├── .gitignore
└── .python-version


