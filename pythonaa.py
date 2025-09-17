import tensorflow as tf

# Load your existing Keras model
model = tf.keras.models.load_model("tb_model.h5")

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
with open("tb_model.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ Model converted to tb_model.tflite")
