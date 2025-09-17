import os
import shutil
import random

# Paths
base_dir = "../data"   # Original data (Normal & Tuberculosis folders)
output_dir = "../dataset_split"  # New split dataset

classes = ["Normal", "Tuberculosis"]

# Split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create output folders
for split in ["Train", "Validation", "Test"]:
    for cls in classes:
        path = os.path.join(output_dir, split, cls)
        os.makedirs(path, exist_ok=True)

# Split and copy files
for cls in classes:
    cls_dir = os.path.join(base_dir, cls)
    images = os.listdir(cls_dir)
    random.shuffle(images)

    total = len(images)
    train_end = int(train_ratio * total)
    val_end = int((train_ratio + val_ratio) * total)

    train_files = images[:train_end]
    val_files = images[train_end:val_end]
    test_files = images[val_end:]

    for f in train_files:
        shutil.copy(os.path.join(cls_dir, f), os.path.join(output_dir, "Train", cls, f))
    for f in val_files:
        shutil.copy(os.path.join(cls_dir, f), os.path.join(output_dir, "Validation", cls, f))
    for f in test_files:
        shutil.copy(os.path.join(cls_dir, f), os.path.join(output_dir, "Test", cls, f))

print("✅ Dataset successfully split into Train, Validation, and Test!")