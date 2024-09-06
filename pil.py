from PIL import Image

# Open an image file
img = Image.open("1.png")

# Get image size
width, height = img.size
print(f"Width: {width}, Height: {height}")

# Get image mode (e.g., RGB, Grayscale)
print(f"Mode: {img.mode}")
