from PIL import Image
import math

from PIL import Image
import math

def is_close_to_white(rgb, threshold):
    """
    Determine if the RGB value is close to white using Euclidean distance.
    """
    r, g, b = rgb
    distance = math.sqrt((255 - r) ** 2 + (255 - g) ** 2 + (255 - b) ** 2)
    return distance < threshold

def make_transparent(image_path, output_path, threshold=30):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to RGBA (if not already in this mode)
    image = image.convert("RGBA")
    
    # Get the data of the image
    data = image.getdata()
    
    new_data = []
    for item in data:
        # Change all pixels close to white to transparent
        if is_close_to_white(item[:3], threshold):
            new_data.append((255, 255, 255, 0))  # Making close-to-white pixels transparent
        else:
            new_data.append(item)
    
    # Update image data
    image.putdata(new_data)
    
    # Save the new image
    image.save(output_path, "PNG")


# Example usage
make_transparent("bball.png", "basketball_transparent.png", threshold=50)
