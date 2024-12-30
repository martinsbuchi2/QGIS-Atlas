from PIL import Image
import os

# Set the directory containing your images
image_folder = "C:\\Users\\Marti\\Desktop\\REA WORK\\2024\\DECEMBER\\UKNAIF\\VIDA REPORT\\Images"

# List all files in the directory and filter out only PNG files
image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]

# Sort the files numerically (assuming the filenames are like 'output_1.png', 'output_2.png', etc.)
image_files.sort(key=lambda f: int(f.split('_')[1].split('.')[0]))

# List to hold the images for PDF creation
images = []

# Loop through each image, open it, and append to the list
for filename in image_files:
    img_path = os.path.join(image_folder, filename)
    img = Image.open(img_path)
    # Convert the image to RGB (required for PDF)
    img_rgb = img.convert('RGB')
    images.append(img_rgb)

# Save all the images as a multi-page PDF
if images:
    images[0].save("atlas_maps.pdf", save_all=True, append_images=images[1:])

print("PDF created successfully with images arranged correctly!")
