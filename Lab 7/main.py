# Before the program run, sure that image's path is correct
# Task 1
import cv2
# Task 2
img = cv2.imread('C:/Users/samet/Desktop/pexels-mccutcheon-1317559.jpg')
# Controlling if the image is added or not
if img is None:
    print("The image is not read")
else:
    print("Image read successfully")
# new width and new height because my original image is too big
width=700
height=700
resized_img=cv2.resize(img,(width,height))

# Task3 & 4
(B,G,R) = cv2.split(resized_img)

# Task 5
cv2.imshow("Blue",B)
cv2.imshow("Red",R)
cv2.imshow("Green",G)

# Task 6
# Set the green channel values to 0
G[:, :] = 0

# Task 7
# Merge the modified color channels back together
modified_image = cv2.merge([B, G, R])

# Display the modified image
cv2.imshow('Modified Image', modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()