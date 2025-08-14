import qrcode
import cv2
import os  # ✅ Needed to auto-open the image on Windows

def generate_qr(data, filename='qr_code.png'):
    img = qrcode.make(data)
    img.save(filename)
    print(f"[✅] QR Code saved as '{filename}'")

    # ✅ Automatically open the saved image
    try:
        os.startfile(filename)
    except Exception as e:
        print("[❌] Could not open image:", e)
def scan_qr_from_image(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    
    if bbox is not None and data:
        print(f"[📥] QR Code Data: {data}")
    else:
        print("[❌] No QR Code found in the image.")

def scan_qr_from_webcam():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    print("[📷] Scanning... Press 'q' to quit.")
    while True:
        _, frame = cap.read()
        data, bbox, _ = detector.detectAndDecode(frame)
        if data:
            print(f"[📥] QR Code Data: {data}")
            break
        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("QR Code Tool")
    print("1. Generate QR Code")
    print("2. Scan QR from Image")
    print("3. Scan QR from Webcam")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        data = input("Enter text/URL to encode: ")
        filename = input("Enter filename (default 'qr_code.png'): ") or "qr_code.png"
        generate_qr(data, filename)
    elif choice == '2':
        image_path = input("Enter image file path: ")
        scan_qr_from_image(image_path)
    elif choice == '3':
        scan_qr_from_webcam()
    else:
        print("Invalid choice.")
