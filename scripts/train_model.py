import os
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Paths to dataset
train_dir = r"C:\Users\91886\Downloads\tb-detection-app\dataset_split\Train"
val_dir = r"C:\Users\91886\Downloads\tb-detection-app\dataset_split\Validation"
test_dir = r"C:\Users\91886\Downloads\tb-detection-app\dataset_split\Test"

# Image parameters
img_size = (224, 224)
batch_size = 32

# Data generators
train_datagen = ImageDataGenerator(rescale=1.0/255)
val_datagen = ImageDataGenerator(rescale=1.0/255)
test_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    shuffle=False
)

# Model architecture
def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(learning_rate=0.0001),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

# Train model
def train_tb_model():
    model = build_model()
    history = model.fit(
        train_generator,
        epochs=10,
        validation_data=val_generator
    )
    return model, history

# Plot training history
def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 5))

    # Accuracy plot
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc="lower right")
    plt.title("Training and Validation Accuracy")

    # Loss plot
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc="upper right")
    plt.title("Training and Validation Loss")

    plt.savefig("../training_history.png")  # Save as PNG
    plt.show()

if __name__ == "__main__":
    print("🚀 Training TB Detection Model")
    model, history = train_tb_model()

    # Save model
    model.save("../tb_model.h5")
    print("✅ Model saved as tb_model.h5")

    # Evaluate on test set
    test_loss, test_acc = model.evaluate(test_generator, verbose=1)
    print(f"🎯 Test Accuracy: {test_acc:.4f}")

    # Plot results
    plot_history(history)
    print("📊 Training history plot saved as training_history.png")