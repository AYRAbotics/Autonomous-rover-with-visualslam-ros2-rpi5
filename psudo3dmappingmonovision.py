import cv2
import numpy as np

# Load depth model
model = cv2.dnn.readNet("model-small.onnx")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    # Small input for speed
    img = cv2.resize(frame, (256, 256))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    blob = cv2.dnn.blobFromImage(
        rgb,
        1/255.0,
        (256, 256),
        mean=(0,0,0),
        swapRB=False,
        crop=False
    )

    model.setInput(blob)

    depth = model.forward()
    depth = depth[0, :, :]

    # Normalize depth
    depth = cv2.normalize(depth, None, 0, 1, cv2.NORM_MINMAX)

    # Resize depth back
    depth = cv2.resize(depth, (w, h))

    # Create pseudo 3D shift
    shift = (depth * 30).astype(np.int32)

    pseudo = np.zeros_like(frame)

    for y in range(h):
        for x in range(w):
            nx = x + shift[y, x]

            if nx < w:
                pseudo[y, nx] = frame[y, x]

    cv2.imshow("Original", frame)
    cv2.imshow("Pseudo 3D", pseudo)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
