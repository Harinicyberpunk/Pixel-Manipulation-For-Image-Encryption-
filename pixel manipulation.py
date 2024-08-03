from PIL import Image
import binascii

def text_to_bin(text):
    """Converts a text string to binary."""
    binary = bin(int(binascii.hexlify(text.encode('utf-8')), 16))
    return binary[2:]

def bin_to_text(binary):
    """Converts binary to text string."""
    n = int(binary, 2)
    text = binascii.unhexlify('%x' % n).decode('utf-8')
    return text

def encode_message(img_path, message, output_path):
    """Encodes a message into the image."""
    img = Image.open(img_path)
    binary_message = text_to_bin(message) + '1111111111111110'  # Delimiter to indicate end of message
    binary_len = len(binary_message)

    encoded_pixels = img.load()
    width, height = img.size
    index = 0

    for y in range(height):
        for x in range(width):
            if index < binary_len:
                r, g, b = img.getpixel((x, y))
                r = (r & 0xFE) | int(binary_message[index])
                if index + 1 < binary_len:
                    g = (g & 0xFE) | int(binary_message[index + 1])
                if index + 2 < binary_len:
                    b = (b & 0xFE) | int(binary_message[index + 2])
                encoded_pixels[x, y] = (r, g, b)
                index += 3
            else:
                break

    img.save(output_path)
    print(f"Message encoded and saved as {output_path}")

def decode_message(img_path):
    """Decodes the message from the image."""
    img = Image.open(img_path)
    binary_message = ""
    pixels = img.load()
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)

    delimiter = '1111111111111110'
    binary_message = binary_message.split(delimiter)[0]
    message = bin_to_text(binary_message)
    return message

def main():
    choice = input("Type 'encode' to encode a message or 'decode' to decode a message: ").strip().lower()
    if choice == 'encode':
        img_path = input("Enter the path to the image: ")
        message = input("Enter the message to encode: ")
        output_path = input("Enter the output image path: ")
        encode_message(img_path, message, output_path)
    elif choice == 'decode':
        img_path = input("Enter the path to the encoded image: ")
        message = decode_message(img_path)
        print(f"Decoded message: {message}")
    else:
        print("Invalid choice! Please type 'encode' or 'decode'.")

if __name__ == "__main__":
    main()
