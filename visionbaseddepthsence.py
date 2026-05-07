import cv2
import numpy as np

# Speed tweaks
cv2.setUseOptimized(True)
cv2.setNumThreads(2)

MODEL_PATH = "model-small.onnx"
CAM_INDEX = 0

# Smaller inference size = faster
INFER_W, INFER_H = 256, 256

# Process every Nth frame
FRAME_SKIP = 4

model = cv2.dnn.readNet(MODEL_PATH)

# Try to speed up inference if available
try:
    model.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    model.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
except Exception:
    pass

cap = cv2.VideoCapture(CAM_INDEX)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap.set(cv2.CAP_PROP_FPS, 10)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

if not cap.isOpened():
    print("Failed to open camera")
    raise SystemExit

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    frame_count += 1

    # Keep UI responsive, but skip inference on some frames
    if frame_count % FRAME_SKIP != 0:
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) == 27:
            break
        continue

    # Resize before inference for speed
    small = cv2.resize(frame, (INFER_W, INFER_H), interpolation=cv2.INTER_LINEAR)

    img = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    blob = cv2.dnn.blobFromImage(
        img,
        scalefactor=1 / 255.0,
        size=(INFER_W, INFER_H),
        mean=(0, 0, 0),
        swapRB=False,
        crop=False
    )

    model.setInput(blob)
    depth = model.forward()

    depth = depth[0, :, :]
    depth = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
    depth = np.uint8(depth)

    # Resize back only for display
    depth = cv2.resize(depth, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_LINEAR)
    depth_colored = cv2.applyColorMap(depth, cv2.COLORMAP_INFERNO)

    cv2.imshow("Webcam", frame)
    cv2.imshow("Depth Map", depth_colored)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
