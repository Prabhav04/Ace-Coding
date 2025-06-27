import cv2

# Force TCP transport and use credentials
rtsp_url = "rtsp://admin:LLPJRB@192.168.31.58:554/ch1/main"
cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)  # CAP_FFMPEG improves compatibility

if not cap.isOpened():
    print("Error: Failed to open stream. Check:")
    print("1. Credentials (local password, not cloud)")
    print("2. Camera IP/port")
    print("3. RTSP path (try /live, /h264, /Streaming/Channels/101)")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Frame grab failed")
            break
        cv2.imshow("RTSP Stream", frame)
        if cv2.waitKey(1) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


