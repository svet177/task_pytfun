import cv2
import pyautogui
import time
import numpy as np
from PIL import ImageGrab

def find_button_on_screen(reference_image_path, threshold=0.8):
    """
    Locate the button based on the reference image on the screen.
    
    :param reference_image_path: Path to the reference image of the button.
    :param threshold: The confidence threshold for template matching (default 0.8).
    :return: Coordinates of the button if found, otherwise None.
    """
    # Load the reference image (button image)
    button_image = cv2.imread(reference_image_path, cv2.IMREAD_COLOR)
    button_height, button_width = button_image.shape[:2]

    while True:
        # Capture a screenshot of the screen
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)

        # Convert screenshot to BGR format (OpenCV default)
        screenshot_bgr = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        # Perform template matching to find the button
        result = cv2.matchTemplate(screenshot_bgr, button_image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # If a match is found with sufficient confidence
        if max_val >= threshold:
            print(f"Button found at {max_loc} with confidence {max_val}")
            # Calculate the center of the button
            button_center = (max_loc[0] + button_width // 2, max_loc[1] + button_height // 2)
            return button_center

        # Pause for a short duration before checking again
        time.sleep(0.5)

def click_button(button_center):
    """
    Click the button at the specified coordinates.
    
    :param button_center: The (x, y) coordinates of the button.
    """
    pyautogui.moveTo(button_center[0], button_center[1], duration=0.5)  # Move mouse to button
    pyautogui.click()  # Click button
    print(f"Clicked at {button_center}")

if __name__ == "__main__":
    # Path to the reference image of the button you want to locate
    reference_image_path = r"C:\Users\Svetlin.Andonov\OneDrive - ADASTRA, s.r.o\Desktop\button_image.png"
    
    try:
        # Find the button on the screen
        button_center = find_button_on_screen(reference_image_path)
        
        if button_center:
            # Click the button
            click_button(button_center)
        else:
            print("Button not found.")
    except KeyboardInterrupt:
        print("Script interrupted by user.")
