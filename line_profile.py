import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define a custom event handler to close the figure when spacebar is pressed
def on_key(event):
    if event.key == ' ':
        plt.close()

def print_img(img):
    if len(img.shape) == 3:
        height, width, channels = img.shape
        print(f"Image Dimensions: Width={width}, Height={height}, Channels={channels}")
    else:
        # If not, assume it has only two dimensions
        height, width = img.shape
        print(f"Image Dimensions: Width={width}, Height={height})")

    bit_depth = image.dtype
    print(f"Bit Depth: {bit_depth}")


# Define the image size
height, width = 2064, 2472
# height, width = 500, 600

# Create a grayscale image filled with zeros (black)
image = np.zeros((height, width), dtype=np.uint16)
image_8bits = image.copy()

# Define Gaussian parameters
peak        = 3500        # height of the curve's peak
center_x    = width  // 2   # the position of the center of the peak (in x)
center_y    = height // 2   # the position of the center of the peak (in y)
sigma       = 2000        # the standard deviation | Adjust this value to control the spread of the Gaussian function
# Create a Gaussian gradient where the center is brighter
for y in range(height):
    for x in range(width):
        distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        
        value = int(peak * np.exp(-distance**2 / (2 * sigma**2)))
        image[y, x] = value
        image_8bits[y, x] = value >> 4  # Shift right by 4 bits to convert to 8-bit

# convert the 12-bits image to 8-bits for display
image_8bits = image_8bits.astype(np.uint8)

# Define the starting and ending points for the line profile
start_point = (0, image.shape[0] // 2)  # Middle-left edge
end_point = (image.shape[1] - 1, image.shape[0] // 2)  # Middle-right edge

# Extract the line profile
# rgb_image = cv2.cvtColor(image_8bits, cv2.COLOR_GRAY2BGR)
show_img_with_line = cv2.line(image.copy(), start_point, end_point, color=(180,119,30), thickness=2)
# show_img_with_line = cv2.cvtColor(show_img_with_line, cv2.COLOR_BGR2RGB)

# Display Images
# image_display = image >> 4

# cv2.imshow("Gaussian", image_display.astype(np.uint8))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow("Gaussian", image_8bits)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow("line_profile", show_img_with_line)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Create a Matplotlib figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 6), gridspec_kw={'width_ratios': [3, 4]})

# Display the first image in the first subplot
axes[0].imshow(image, cmap='gray')
# axes[0].set_title('Simulated Flatfield - Gaussian')

middle_line_position = image.shape[0] // 2
# axes[0].axvline(x=middle_line_position, color='red', linestyle='--', linewidth=1)
axes[0].axhline(y=middle_line_position, color='red', linestyle='--', linewidth=1)
axes[0].set_title(f'Simulated Gaussian Flatfield\n(a={peak}, σ={sigma})')

# Display the plot in the third subplot
# axes[2].plot(x, y)
# axes[2].set_title('Plot')
line_profile = image
axes[1].plot(np.arange(0, line_profile.shape[1]), line_profile[line_profile.shape[1] // 2, :], label='Gaussian', color='red')
axes[1].set_xlim(0, line_profile.shape[1])  # Set x limits from 0 to the width of the line profile
axes[1].set_ylim(0, 5000)
axes[1].set_title("Horizontal Line Profile")
axes[1].set_xlabel("Pixel, [DN]")
axes[1].set_ylabel("Center Line Profile, [DN]")
axes[1].legend()
axes[1].grid(True)
# fig.set_size_inches(8, 4)


# # Plot the line profile
# plt.figure(figsize=(8, 4))
# plt.plot(np.arange(0, line_profile.shape[1]), line_profile[line_profile.shape[1] // 2, :], label='Gaussian')
# # plt.plot(np.arange(0, line_profile.shape[0]), line_profile[line_profile.shape[0] // 2, :], label='Gaussian')

# # plt.plot(np.arange(0, line_profile.shape[1]), line_profile[line_profile.shape[1] // 2][:])

# plt.xlim(0, line_profile.shape[1])  # Set x limits from 0 to the width of the line profile
# plt.ylim(0, 5000)
# plt.title("Horizontal Line Profile")
# plt.xlabel("Pixel, [DN]")
# plt.ylabel("Center Line Profile, [DN]")
# plt.legend()
# plt.grid(True)

# Connect the custom event handler to the figure
plt.connect('key_press_event', on_key)

# Save the figure to the desktop
desktop_path = os.path.expanduser("~/Desktop")
output_file = os.path.join(desktop_path, "Gaussian_line_profile_plot.png")
plt.savefig(output_file, dpi=300)

# Show the plot (optional)
plt.show()
print('plot finished!')





# print(f"Line profile plot saved to {output_file}")


#----------------------------------------------------------------------------------------

# # Create a gradient from the center to the corners
# for y in range(height):
#     for x in range(width):
#         distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
#         # Normalize the distance to the range [0, 255]
#         value = int((distance / np.sqrt(width**2 + height**2)) * 255)
#         image[y, x] = value

# # Create a gradient where the center is brighter and corners are darker
# for y in range(height):
#     for x in range(width):
#         distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
#         # Reverse the gradient by subtracting the normalized distance from 255
#         value = 255 - int((distance / np.sqrt(width ** 2 + height ** 2)) * 255)
#         image[y, x] = value