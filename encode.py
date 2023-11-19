from PIL import Image, ImageDraw, ImageFont

def encode_image(path_to_png, secret_message):
    """
    Add a hidden message to a PNG image.
    """
    # Open the original image using PIL:
    original_image = Image.open(path_to_png)

    # Get the pixels of the original image:
    hidden_message = write_text(secret_message, original_image.size)
    hidden_message_pixels = hidden_message.load()

    # Create a new PIL image with the same size as the original image:
    encoded_image = Image.new("RGB", original_image.size)
    encoded_image_pixels = encoded_image.load()
    x_size, y_size = original_image.size

    # split out all the channels
    red_channel, green_channel, blue_channel = original_image.split()

    for x in range(x_size):
        for y in range(y_size):
            red_value = red_channel.getpixel((x, y))
            green_value = green_channel.getpixel((x, y))
            blue_value = blue_channel.getpixel((x, y))
            hidden_message_pixel = hidden_message_pixels[x, y]

            # get the binary representation of the red value
            red_value = bin(red_value)
            # set the last bit to 0
            red_value = red_value[:-1] + '0'

            if hidden_message_pixel == (255, 255, 255):
                # If the hidden message pixel is white, set the LSB of the red value to 1
                red_value = red_value[:-1] + '1'

            # Convert the binary string back to an integer:
            red_value = int(red_value, 2)
            encoded_image_pixels[x, y] = (red_value, green_value, blue_value)

    # Save the image to disk:
    encoded_image.save("encoded_image.png") # For testing purposes


def write_text(text_to_write, image_size=(500, 500)):
    """
    Create an image that contains the text_to_write.
    """
    # Create a new PIL image with the same size as the original image:
    text_image = Image.new("RGB", image_size)
    draw = ImageDraw.Draw(text_image)

    # Use a truetype font:
    font = ImageFont.truetype("/Library/Fonts/Impact.ttf", 24)

    # Draw the text onto the image:
    draw.text((20, 20), text_to_write, font=font)

    # Save the image to disk:
    text_image.save("text_image.png") # For testing purposes
    return text_image





 

    

 


if __name__ == '__main__':
    encode_image("DalekOG.png","EXTERMINATE!")
