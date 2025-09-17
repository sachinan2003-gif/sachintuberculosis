# import tensorflow as tf
# import numpy as np
# from tensorflow.keras.preprocessing import image

# class TBDetectionModel:
#     def __init__(self, model_path):
#         # Load trained model
#         self.model = tf.keras.models.load_model(model_path)
#         self.img_size = (224, 224)  # must match training size

#     def predict(self, img_path):
#         # Load and preprocess image
#         img = image.load_img(img_path, target_size=self.img_size)
#         img_array = image.img_to_array(img)
#         img_array = np.expand_dims(img_array, axis=0) / 255.0

#         # Prediction
#         prediction = self.model.predict(img_array)
#         print(prediction,"hi bro hello")

#         # Interpret
#         if prediction[0][0] > 0.5:
#             return "Tuberculosis Detected", float(prediction[0][0])
#         else:
#             return "Normal", float(1 - prediction[0][0])