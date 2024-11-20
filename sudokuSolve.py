import cv2
import numpy as np

def preprocess_image(image_path):
    # Read the image in grayscale mode
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply adaptive thresholding for better grid detection
    thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    return thresh

def detect_grid_and_cells(thresh_image):
    # Detect contours to find the largest square, assumed to be the Sudoku grid
    contours, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        print("No contours detected. Please check the preprocessing step.")
        return None

    # Find the contour with the maximum area, which is the Sudoku grid
    sudoku_grid = max(contours, key=cv2.contourArea)

    # Get the bounding box for the Sudoku grid
    rect = cv2.boundingRect(sudoku_grid)
    x, y, w, h = rect
    
    # Draw the bounding box (optional, for visualization purposes)
    image_with_grid = cv2.drawContours(thresh_image.copy(), [sudoku_grid], -1, (0, 255, 0), 2)

    # Warp perspective to get a straight 9x9 grid (you can implement this part later)
    # Note: You can also apply cv2.findHomography() if needed to adjust the perspective.
    
    return image_with_grid, sudoku_grid  # Return grid contour and processed image

def solveSudoku(image_path):
    thresh_image = preprocess_image(image_path)
    result_image, sudoku_grid = detect_grid_and_cells(thresh_image)

    if sudoku_grid is None:
        print("Error: Sudoku grid not detected.")
        return

    # Here, you can proceed with further processing (cell extraction, OCR, etc.)

    cv2.imwrite("detected_sudoku_grid.jpg", result_image)
    print("Image saved as 'detected_sudoku_grid.jpg'")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


