# Pixel Manipulation for Encryption

This Python script demonstrates how to perform pixel manipulation for encryption by encoding a message into the least significant bits of pixel values in an image. The script allows users to encode a message into an image or decode a message from an image.

## Features

- Encode a message into an image by manipulating pixel values.
- Decode a message from an image by reading manipulated pixel values.
- Handles both encoding and decoding through a simple user interface.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install the Pillow library using pip:
    ```sh
    pip install pillow
    ```

## Usage

1. Clone the repository or download the script.
2. Run the script using Python.
3. Follow the on-screen prompts to either encode or decode a message.

### Encoding a Message

To encode a message into an image:

```sh
python pixel_encryption.py
```

Follow the prompts:
- Type 'encode' to encode a message.
- Provide the path to the input image.
- Enter the message to encode.
- Provide the path to save the output image.

### Decoding a Message

To decode a message from an image:

```sh
python pixel_encryption.py
```

Follow the prompts:
- Type 'decode' to decode a message.
- Provide the path to the encoded image.

## Code Explanation

### Functions

1. **text_to_bin(text)**:
    - Converts a text string to a binary string.

2. **bin_to_text(binary)**:
    - Converts a binary string back to a text string.

3. **encode_message(img_path, message, output_path)**:
    - Encodes a given message into the image by modifying the least significant bits of the pixel values.
    - Saves the modified image to the specified output path.

4. **decode_message(img_path)**:
    - Decodes the message from the image by reading the least significant bits of the pixel values.
    - Returns the decoded message.

5. **main()**:
    - Handles user input and calls the appropriate functions to either encode or decode a message.

### Running the Script

To run the script, execute the following command in your terminal or command prompt:

```sh
python pixel_encryption.py
```

### Example

1. Encoding a message:
    ```sh
    python pixel_encryption.py
    Type 'encode' to encode a message or 'decode' to decode a message: encode
    Enter the path to the image: input.png
    Enter the message to encode: Hello, World!
    Enter the output image path: output.png
    Message encoded and saved as output.png
    ```

2. Decoding a message:
    ```sh
    python pixel_encryption.py
    Type 'encode' to encode a message or 'decode' to decode a message: decode
    Enter the path to the encoded image: output.png
    Decoded message: Hello, World!
    ```

## License

This project is licensed under the MIT License.

## Author

Harini

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

Inspired by classical steganography techniques.

---

This `README` file provides an overview of the script, its features, usage instructions, and other relevant information for users and contributors.
