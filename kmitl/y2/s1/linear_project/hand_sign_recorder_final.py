import os
import sys
import cv2
import numpy as np
import tensorflow as tf
import mediapipe as mp
import tkinter as tk
from tkinter import StringVar, messagebox
from threading import Thread
import datetime
from PIL import Image, ImageTk
import time

# Load the pre-trained model
if getattr(sys, 'frozen', False):
    model_path = os.path.join(sys._MEIPASS, 'model.keras')
else:
    model_path = "D:\\valentine\\mycode\\kmitl\\y2\s1\\linear_project\\model.keras"
model = tf.keras.models.load_model(model_path)

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Define the alphabet
alphabets = list("ABCDEFGHIKLMNOPQRSTUVWXY")

# Global variables
predictions = []  # List to store predictions
recording = False  # Flag to control recording
video_thread = None  # Variable to hold the video thread
camera_indices = []  # Global variable for camera indices
last_prediction_time = 0  # To track the time of the last prediction (for debouncing)
debounce_delay = 3  # Debounce delay of 1 second

# Create a Tkinter window
root = tk.Tk()
root.title("Hand Sign Recorder")
root.geometry("400x400")
root.config(bg="#009081")

# Configure grid layout for responsiveness
root.grid_columnconfigure(0, weight=1)

# Frame for Camera Selection
camera_frame = tk.Frame(root, bg="#009081", padx=10, pady=10)
camera_frame.grid(row=0, column=0, sticky="ew")



# Configure row and column weights for expanding
root.grid_rowconfigure(6, weight=1)  # ให้แถว 6 ขยาย
root.grid_columnconfigure(0, weight=1)  # ให้คอลัมน์ 0 ขยาย

# Dropdown menu for camera selection
camera_index_var = StringVar(camera_frame)

# Function to list available camera devices
def get_camera_devices():
    camera_indices = []
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.isOpened():
            break
        camera_indices.append(index)
        index += 1
        cap.release()
    return camera_indices

# Load available camera devices
def load_cameras():
    global camera_indices
    camera_indices = get_camera_devices()

    if not camera_indices:
        messagebox.showerror("Camera Error", "No camera devices found. Please check your camera connection.")
        root.quit()

    camera_index_var.set(camera_indices[0] if camera_indices else "")
    camera_menu = tk.OptionMenu(camera_frame, camera_index_var, *camera_indices, command=lambda _: update_camera_label())
    camera_menu.config(width=20, font=("Sixfour Conovergence", 12))
    camera_menu.grid(row=0, column=0, padx=10)

    update_camera_label()

def update_camera_label():
    selected_camera = camera_index_var.get()
    if selected_camera:
        selected_camera_label.config(text=f"Camera: {selected_camera}")
        toggle_button.config(state="normal")
        global video_thread
        if video_thread is None or not video_thread.is_alive():
            video_thread = Thread(target=video_capture)
            video_thread.start()
    else:
        selected_camera_label.config(text="Camera: Please select a camera")
        toggle_button.config(state="disabled")

# Label to display selected camera
selected_camera_label = tk.Label(camera_frame, text="Camera: Please select a camera", font=("Sixfour Conovergence", 12), bg="#009081", fg="#EEE")
selected_camera_label.grid(row=1, column=0, padx=10)

# Status label to show recording status
status_var = StringVar(value="Not Recording")
status_label = tk.Label(root, textvariable=status_var, font=("Sixfour Conovergence", 14), bg="#009081", fg="#fcdc64")
status_label.grid(row=1, column=0, pady=5)

# Title Label
title_label = tk.Label(root, text="Hand Sign Recorder", font=("Sixfour Conovergence", 24, "bold"), bg="#009081", fg="#EEE")
title_label.grid(row=2, column=0, pady=10)

# Function to toggle recording state
def toggle_recording():
    global recording
    if recording:
        recording = False
        status_var.set("Not Recording")
        status_label.config(fg="#fcdc64")
        toggle_button.config(text="Start Recording")
        save_recordings()
        print("Recording stopped and saved.")
    else:
        recording = True
        predictions.clear()
        prediction_list.delete(1.0, tk.END)
        status_var.set("Recording...")
        status_label.config(fg="#fcdc64")
        toggle_button.config(text="Stop Recording")
        print("Recording started.")

# Function to clear predictions
def clear_predictions():
    predictions.clear()
    prediction_list.delete(1.0, tk.END)
    prediction_var.set("Predicted Sign: None")

# Create a frame for buttons
button_frame = tk.Frame(root, bg="#009081")
button_frame.grid(row=3, column=0, pady=10)

# Create buttons
toggle_button = tk.Button(button_frame, text="Start Recording", command=toggle_recording, bg="#688A83", fg="#ffffff", font=("Sixfour Conovergence", 12), width=15, activebackground="#b1cdce", activeforeground="#ffffff", state="disabled")
toggle_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_predictions, bg="#688A83", fg="#ffffff", font=("Sixfour Conovergence", 12), width=15, activebackground="#b1cdce", activeforeground="#ffffff")
clear_button.grid(row=0, column=1, padx=10)

# ปุ่ม Exit เพื่อออกจากโปรแกรม
exit_button = tk.Button(button_frame, text="Exit", command=root.quit, bg="#688A83", fg="#ffffff", font=("Sixfour Conovergence", 12), width=15, activebackground="#b1cdce", activeforeground="#ffffff")
exit_button.grid(row=0, column=2, padx=10)

# Label to display predicted signs
prediction_var = StringVar(value="Predicted Sign: None")
prediction_label = tk.Label(root, textvariable=prediction_var, font=("Sixfour Conovergence", 20), bg="#009081", fg="#EEE")
prediction_label.grid(row=4, column=0, pady=10)

# Text widget to display the list of predictions
prediction_list = tk.Text(root, height=10, width=50, font=("Sixfour Conovergence", 14), bg="#EEE", fg="#009081")
prediction_list.grid(row=5, column=0, pady=10)

def predict_hand_sign(hand_landmarks):
    landmark_vertices_xyz = [coord for l in hand_landmarks.landmark for coord in (l.x, l.y, l.z)]
    data = np.array(landmark_vertices_xyz).reshape(1, -1)
    data_reshaped = data.reshape(1, 7, 9, 1)
    prediction = model.predict(data_reshaped)
    label_idx = np.argmax(prediction)
    return alphabets[label_idx]

def save_predictions_to_file(predictions):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'predictions_{timestamp}.txt'
    with open(filename, 'w') as f:
        f.writelines(f"{sign}" for sign in predictions)
    print(f"Predictions saved to {filename}")

def video_capture():
    global recording, last_prediction_time
    camera_index = camera_index_var.get()
    if not camera_index:
        return
    cap = cv2.VideoCapture(int(camera_index))
    with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            image = cv2.flip(image, 1)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Get bounding box for the hand
                    x_min = int(min(l.x for l in hand_landmarks.landmark) * image.shape[1])
                    y_min = int(min(l.y for l in hand_landmarks.landmark) * image.shape[0])
                    x_max = int(max(l.x for l in hand_landmarks.landmark) * image.shape[1])
                    y_max = int(max(l.y for l in hand_landmarks.landmark) * image.shape[0])

                    # Draw gray overlay with 15% opacity
                    overlay_color = (128, 128, 128)  # Gray color
                    overlay = np.zeros_like(image, dtype=np.uint8)
                    cv2.rectangle(overlay, (x_min, y_min), (x_max, y_max), overlay_color, -1)
                    cv2.addWeighted(overlay, 0.15, image, 1 - 0.15, 0, image)

                    current_time = time.time()
                    if current_time - last_prediction_time > debounce_delay:
                        predicted_sign = predict_hand_sign(hand_landmarks)
                        last_prediction_time = current_time
                        if recording:
                            predictions.append(predicted_sign)
                            prediction_list.insert(tk.END, f"{predicted_sign}")
                            prediction_list.see(tk.END)
                        prediction_var.set(f"Predicted Sign: {predicted_sign}")

                        # Change overlay color to yellow with 80% opacity
                        overlay_color = (224, 255, 255)  # Yellow color
                        overlay = np.zeros_like(image, dtype=np.uint8)
                        cv2.rectangle(overlay, (x_min, y_min), (x_max, y_max), overlay_color, -1)
                        cv2.addWeighted(overlay, 0.8, image, 1 - 0.8, 0, image)

                    # Draw hand landmarks
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            else:
                prediction_var.set("Predicted Sign: No hand detected")

            resized_image = cv2.resize(image, (400, 400)) 
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img_tk = ImageTk.PhotoImage(image=img)
            video_label.config(image=img_tk)
            video_label.image = img_tk

            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

# Create a label to display video feed
video_label = tk.Label(root, bg="#009081")
video_label.grid(row=0, column=0, pady=10)

def save_recordings():
    if predictions:
        save_predictions_to_file(predictions)

# Start loading camera devices on program startup
load_cameras()

# Create a label to display video feed
video_label = tk.Label(root)
video_label.grid(row=0, column=0, pady=10, sticky="nsew") 

# Start the Tkinter main loop
root.mainloop()
