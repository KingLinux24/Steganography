from PIL import Image

def to_bin(data):
    """Convert data to binary format as string"""
    if isinstance(data, str):
        return ''.join([format(ord(i), '08b') for i in data])
    elif isinstance(data, bytes) or isinstance(data, bytearray):
        return ''.join([format(i, '08b') for i in data])
    elif isinstance(data, int):
        return format(data, '08b')
    else:
        raise TypeError("Type not supported.")

def encode(image_path, secret_message, output_path):
    """Encode secret_message into image and save as output_path"""
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    binary_secret_msg = to_bin(secret_message) + '1111111111111110'  # Delimiter to mark end of message
    data_len = len(binary_secret_msg)
    img_data = iter(image.getdata())

    new_pixels = []
    for i in range(data_len):
        pixel = list(next(img_data))
        for n in range(3):  # For R, G, B channels
            if i < data_len:
                # Replace LSB with message bit
                pixel[n] = pixel[n] & ~1 | int(binary_secret_msg[i])
                i += 1
            else:
                break
        new_pixels.append(tuple(pixel))

    # Add remaining pixels
    for pixel in img_data:
        new_pixels.append(pixel)

    # Create new image with modified pixels
    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(new_pixels)
    encoded_image.save(output_path)
    print(f"Secret message encoded and saved to {output_path}")

def decode(image_path):
    """Decode and return the secret message hidden in the image"""
    image = Image.open(image_path)
    binary_data = ""
    for pixel in image.getdata():
        for n in range(3):  # For R, G, B channels
            binary_data += str(pixel[n] & 1)

    # Split by 8 bits
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_msg = ""
    for byte in all_bytes:
        if byte == '11111111':  # Check for delimiter part 1
            # Check next byte for full delimiter
            next_index = all_bytes.index(byte) + 1
            if next_index < len(all_bytes) and all_bytes[next_index] == '11111110':
                break
        decoded_msg += chr(int(byte, 2))
    return decoded_msg

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="LSB Image Steganography")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode a secret message into an image")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode a secret message from an image")
    parser.add_argument("-i", "--image", type=str, required=True, help="Path to the input image")
    parser.add_argument("-o", "--output", type=str, help="Path to save the output image (for encoding)")
    parser.add_argument("-m", "--message", type=str, help="Secret message to encode")

    args = parser.parse_args()

    if args.encode:
        if not args.message:
            print("Please provide a secret message to encode using -m or --message")
        elif not args.output:
            print("Please provide an output image path using -o or --output")
        else:
            encode(args.image, args.message, args.output)
    elif args.decode:
        secret = decode(args.image)
        print("Decoded secret message:")
        print(secret)
    else:
        print("Please specify either --encode or --decode")
