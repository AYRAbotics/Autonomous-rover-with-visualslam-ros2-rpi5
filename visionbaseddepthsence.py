import cv2
import numpy as np

# Load MiDaS small ONNX model
model = cv2.dnn.readNet("model-small.onnx")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Prepare input
    blob = cv2.dnn.blobFromImage(
        img,
        1/255.0,
        (256, 256),
        mean=(0,0,0),
        swapRB=False,
        crop=False
    )

    model.setInput(blob)

    # Depth prediction
    depth_map = model.forward()

    depth_map = depth_map[0, :, :]

    # Normalize
    depth_map = cv2.normalize(
        depth_map,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    depth_map = np.uint8(depth_map)

    # Resize to webcam size
    depth_map = cv2.resize(
        depth_map,
        (frame.shape[1], frame.shape[0])
    )

    # Apply color map
    depth_colored = cv2.applyColorMap(
        depth_map,
        cv2.COLORMAP_INFERNO
    )

    # Show results
    cv2.imshow("Webcam", frame)
    cv2.imshow("Depth Map", depth_colored)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()