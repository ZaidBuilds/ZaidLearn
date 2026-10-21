import cv2
import mediapipe as mp
import math
import time
import numpy as np

# --- CONFIGURATION ---
HUD_COLOR = (255, 255, 0)      # Cyan (BGR)
ACCENT_COLOR = (0, 165, 255)   # Orange (BGR)
TEXT_COLOR = (255, 255, 255)   # White
THICKNESS = 1

class MarvelHUD:
    def __init__(self):
        self.angle = 0
        self.pulse = 0
        self.scan_line = 0
        
    def draw_dashed_circle(self, img, center, radius, color, thickness=1, dash_len=20, speed=1):
        """Draws a rotating segmented circle"""
        n_dashes = 12
        step = 360 / n_dashes
        start_angle = self.angle * speed
        
        for i in range(n_dashes):
            s = start_angle + (i * step)
            e = s + dash_len
            cv2.ellipse(img, center, (radius, radius), 0, s, e, color, thickness)

    def draw_tech_lines(self, img, center, radius):
        """Draws the crosshair lines"""
        x, y = center
        gap = 10
        # Horizontal
        cv2.line(img, (x - radius, y), (x - gap, y), HUD_COLOR, 1)
        cv2.line(img, (x + gap, y), (x + radius, y), HUD_COLOR, 1)
        # Vertical
        cv2.line(img, (x, y - radius), (x, y - gap), HUD_COLOR, 1)
        cv2.line(img, (x, y + gap), (x, y + radius), HUD_COLOR, 1)

    def render(self, img, landmarks):
        h, w, c = img.shape
        
        # 1. Calculate Hand Center (Approximate using Wrist & Middle Finger)
        wrist = landmarks[0]
        middle_mcp = landmarks[9]
        
        cx = int((wrist.x + middle_mcp.x) / 2 * w)
        cy = int((wrist.y + middle_mcp.y) / 2 * h)
        center = (cx, cy)
        
        # Calculate dynamic size based on hand distance (wrist to middle tip)
        middle_tip = landmarks[12]
        dist = math.hypot(middle_tip.x - wrist.x, middle_tip.y - wrist.y)
        base_radius = int(dist * w * 0.6)  # Scale HUD with hand

        # --- DRAW THE HUD LAYERS ---

        # Layer 1: Central Reactor (Orange Glow)
        cv2.circle(img, center, int(base_radius * 0.2), ACCENT_COLOR, 2)
        cv2.circle(img, center, int(base_radius * 0.1), (255, 255, 255), -1) # White core

        # Layer 2: Rotating Cyan Rings
        self.draw_dashed_circle(img, center, int(base_radius * 0.5), HUD_COLOR, 2, dash_len=15, speed=2)
        self.draw_dashed_circle(img, center, int(base_radius * 0.7), HUD_COLOR, 1, dash_len=5, speed=-1)
        
        # Layer 3: Outer Scale Ring (Static)
        cv2.circle(img, center, int(base_radius * 0.9), HUD_COLOR, 1)
        
        # Layer 4: Tech Crosshair
        self.draw_tech_lines(img, center, int(base_radius * 0.9))

        # Layer 5: Connecting Lines (The Skeleton)
        # MediaPipe connections
        connections = mp.solutions.hands.HAND_CONNECTIONS
        for connection in connections:
            start_idx = connection[0]
            end_idx = connection[1]
            
            p1 = (int(landmarks[start_idx].x * w), int(landmarks[start_idx].y * h))
            p2 = (int(landmarks[end_idx].x * w), int(landmarks[end_idx].y * h))
            
            cv2.line(img, p1, p2, HUD_COLOR, 1)
            # Draw Joint Nodes (Orange)
            cv2.circle(img, p1, 4, ACCENT_COLOR, -1)

        # Layer 6: Floating Data Text (From your screenshot "83??")
        # Generate a random tech number based on hand position
        tech_val = int((cx + cy) % 100)
        text_pos = (int(landmarks[8].x * w) + 20, int(landmarks[8].y * h) - 20)
        cv2.putText(img, f"TARGET: {tech_val}%", text_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.6, TEXT_COLOR, 2)
        cv2.putText(img, "LOCK_ON", (center[0]-40, center[1]+int(base_radius)+30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ACCENT_COLOR, 1)

        # Update Animation State
        self.angle += 2
        if self.angle >= 360: self.angle = 0

def main():
    # Setup MediaPipe
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    )
    
    # Setup Webcam
    cap = cv2.VideoCapture(0)
    
    hud = MarvelHUD()
    
    print("System Online. Calculating Neural Handlers...")

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # Flip image for mirror effect
        image = cv2.flip(image, 1)
        
        # Convert BGR to RGB for MediaPipe
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        
        # Darken the background slightly to make the HUD pop (Sci-Fi look)
        image = cv2.convertScaleAbs(image, alpha=0.8, beta=-20)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                hud.render(image, hand_landmarks.landmark)

        # Display
        cv2.imshow('Stark Tech Interface v1.0', image)

        # Exit on 'q'
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()