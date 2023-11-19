from PIL import Image

def decode_image(path_to_png):
    """
    Takes in a path to a PNG image, decodes the image, and saves the decoded image to disk.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    for x in range(x_size):
        for y in range(y_size):
            red_value = red_channel.getpixel((x, y))
            # Change red value to binary string representation:
            red_value = bin(red_value)
            last_bit = red_value[-1]
            if last_bit == '0':
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = (0, 0, 0)

    # DO NOT MODIFY. Save the decoded image to disk:
    # decoded_image.save("decoded_image.png")
    decoded_image.save("decoded_dalek.png") # Uncomment to test on the Dalek image

if __name__ == '__main__':
    # decode_image("doggo.png")
    decode_image("encoded_image.png") # Uncomment to test on the Dalek image
