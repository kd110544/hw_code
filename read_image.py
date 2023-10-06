import cv2

# Step 1: Read the image
image_path = '/Users/cwchan/Desktop/IMG_1946.PNG'  # Replace with the path to your image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Step 2: Display the image
    cv2.imshow('Image', image)
    
    # Step 3: Get image dimensions
    height, width, channels = image.shape
    print(f"Image Dimensions: Width={width}, Height={height}, Channels={channels}")

    # Step 4: Get image bit depth
    bit_depth = image.dtype
    print(f"Bit Depth: {bit_depth}")

    # Step 5: Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
