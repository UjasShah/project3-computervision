import cv2
import numpy as np

for number in range(316,328):
    # Define the callback function for mouse events
    def get_mouse_points(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append([x, y])

    # Load the input image
    img = cv2.imread(f'/Users/ujas/Desktop/Computer Vision/project3-materials/rectifying/IMG_0{number}.jpg')

    # Define a list to store the source points
    points = []
    aspect_ratio = 1.33

    # Display the input image and wait for mouse clicks
    cv2.namedWindow('Input')
    cv2.setMouseCallback('Input', get_mouse_points)
    cv2.imshow('Input', img)
    cv2.waitKey(0)

    # Define the corresponding four points in the destination image
    dst_width = 500
    dst_height = int(dst_width * aspect_ratio)
    dst_pts = np.array([[0, 0], [dst_width, 0], [dst_width, dst_height], [0, dst_height]], dtype=np.float32)

    # Convert the source points to a numpy array and calculate the perspective transform matrix
    src_pts = np.array(points, dtype=np.float32)
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)

    # Apply the perspective transform to the input image
    dst_img = cv2.warpPerspective(img, M, (dst_width, dst_height))
    cv2.imwrite(f'results/Q3-0{number}.jpg', dst_img)

    # Display the output image
    cv2.imshow('Output', dst_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()