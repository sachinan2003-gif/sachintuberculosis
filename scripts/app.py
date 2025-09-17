# from flask import Flask, render_template, request,jsonify
# from tb_detection_model import TBDetectionModel
# import os
# from flask_cors import CORS
# app = Flask(__name__)
# CORS(app)
# # Load model
# MODEL_PATH = r"C:\Users\91886\Downloads\tb-detection-app\tb_model.h5"
# tb_model = TBDetectionModel(model_path=MODEL_PATH)

# # Uploads folder
# UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     prediction = None
#     confidence = None

#     if request.method == "POST":
#         file = request.files["file"]
#         if file:
#             filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(filepath)

#             prediction, confidence = tb_model.predict(filepath)
#             print(prediction,confidence )
#             return jsonify({
#                 "prediction":prediction,
#                 "confidence": confidence

#             })

# if __name__ == "__main__":
#     app.run(debug=True)