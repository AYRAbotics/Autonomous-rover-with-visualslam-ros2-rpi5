import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load depth model
model = cv2.dnn.readNet("model-small.onnx")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Failed to open camera")
    raise SystemExit

ret, frame = cap.read()
cap.release()

if not ret:
    print("Failed to capture frame")
    raise SystemExit

h, w = frame.shape[:2]

# Prepare input for the model
img = cv2.resize(frame, (256, 256))
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

blob = cv2.dnn.blobFromImage(
    rgb,
    1 / 255.0,
    (256, 256),
    mean=(0, 0, 0),
    swapRB=False,
    crop=False
)

model.setInput(blob)
depth = model.forward()
depth = depth[0, :, :]

# Normalize depth to 0..1
depth = cv2.normalize(depth, None, 0, 1, cv2.NORM_MINMAX)

# Resize depth back to original frame size
depth = cv2.resize(depth, (w, h), interpolation=cv2.INTER_LINEAR)

# Camera-like projection values
fx = fy = 500.0
cx = w / 2.0
cy = h / 2.0

# More points = denser mapping
step = 4

points = []
colors = []

for v in range(0, h, step):
    for u in range(0, w, step):
        d = float(depth[v, u])

        # Relative pseudo depth
        z = (1.0 - d) * 4.0 + 0.2

        x = (u - cx) / fx * z
        y = (v - cy) / fy * z

        points.append([x, y, z])
        colors.append(frame[v, u] / 255.0)

points = np.array(points)
colors = np.array(colors)

# Show original image + point cloud
fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
ax1.set_title("Original Image")
ax1.axis("off")

ax2 = fig.add_subplot(1, 2, 2, projection="3d")
ax2.scatter(points[:, 0], points[:, 1], points[:, 2], c=colors, s=1)
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
ax2.set_title("Pseudo 3D Point Cloud")

plt.tight_layout()
plt.show()
