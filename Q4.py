import cv2
import numpy as np

# Create an empty image
img = np.zeros((500, 500, 3), np.uint8)

# Define colors for drawing
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)

# Define a list to store the points for each parallel line
points1 = []
points2 = []

# Define a function to handle mouse events
def draw_line(event, x, y, flags, param):
    global points1, points2
    
    # If left mouse button is clicked, add a point to the first set of points
    if event == cv2.EVENT_LBUTTONDOWN and len(points1) < 2:
        points1.append((x, y))
        cv2.circle(img, (x, y), 5, blue, -1)
    
    # If right mouse button is clicked, add a point to the second set of points
    if event == cv2.EVENT_RBUTTONDOWN and len(points2) < 2:
        points2.append((x, y))
        cv2.circle(img, (x, y), 5, green, -1)
    
    # If both sets of points have been marked, draw the lines and the horizon
    if len(points1) == 2 and len(points2) == 2:
        # Draw the two sets of parallel lines
        cv2.line(img, points1[0], points1[1], blue, 2)
        cv2.line(img, points2[0], points2[1], green, 2)
        
        # Find the vanishing points
        vx1, vy1, vx2, vy2 = cv2.fitLine(np.array(points1), cv2.DIST_L2, 0, 0.01, 0.01)
        vx3, vy3, vx4, vy4 = cv2.fitLine(np.array(points2), cv2.DIST_L2, 0, 0.01, 0.01)
        px, py = np.cross((vx1, vy1), (vx3, vy3))
        
        # Draw the horizon line
        cv2.line(img, (0, int(-px/py)), (img.shape[1], int(-px/py)), red, 2)
        
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_line)

while True:
    cv2.imshow('image', img)
    key = cv2.waitKey(1)
    if key == 27: # Press ESC to exit
        break

cv2.destroyAllWindows()
