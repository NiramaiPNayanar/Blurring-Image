import cv2
import numpy as np

# Global variables to store coordinates
dragging = False
start_x, start_y = None, None
end_x, end_y = None, None

def select_blur_area(image):
    """
    This function allows the user to select a rectangular area on the image
    using mouse clicks and drag. The selected area will be returned as a NumPy array.
    """
    def on_mouse(event, x, y, flags, param):
        global dragging, start_x, start_y, end_x, end_y
        if event == cv2.EVENT_LBUTTONDOWN:
            dragging = True
            start_x, start_y = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if dragging:
                end_x, end_y = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            dragging = False
            end_x, end_y = x, y

    cv2.namedWindow("Select Blur Area")
    cv2.setMouseCallback("Select Blur Area", on_mouse)

    while True:
        temp_image = image.copy()  
        if dragging and start_x is not None and start_y is not None and end_x is not None and end_y is not None:
            cv2.rectangle(temp_image, (start_x, start_y), (end_x, end_y), (255, 0, 0), 2)

        cv2.imshow("Select Blur Area", temp_image)

        key = cv2.waitKey(1) & 0xFF
        if key == 27: 
            break
        elif key == 13: 
            if start_x is not None and start_y is not None and end_x is not None and end_y is not None:
                selected_area = image[start_y:end_y, start_x:end_x]
                cv2.destroyWindow("Select Blur Area")
                return selected_area, start_x, start_y, end_x, end_y

    cv2.destroyAllWindows()
    return None, None, None, None, None  

def main():
    # Load the image
    image_path = "C:/Users/Lenovo/Pictures/Screenshots/Screenshot 2024-04-09 004950.png" 
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Select blur area
    selected_area, start_x, start_y, end_x, end_y = select_blur_area(image.copy())

    if selected_area is not None:
        
        blurred_area = cv2.blur(selected_area, (15, 15))  

        
        processed_image = image.copy()

        # Replace the selected area in the copy with the blurred area
        processed_image[start_y:end_y, start_x:end_x] = blurred_area

        # Display both original and processed images
        cv2.imshow("Original Image", image)
        cv2.imshow("Processed Image", processed_image)
        cv2.waitKey(0)
    else:
        print("No area selected.")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
