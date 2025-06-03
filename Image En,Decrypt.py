from PIL import Image

def load_image(path):
    try:
        image = Image.open(path)
        print("Image loaded successfully.")
        return image
    except Exception as e:
        print("Error loading image:", e)
        return None

def save_image(image, path):
    try:
        image.save(path)
        print(f"Image saved to {path}")
    except Exception as e:
        print("Error saving image:", e)

def encrypt_by_swapping(image):
    pixels = list(image.getdata())
    pixels.reverse()  # Swapping by reversing the entire pixel list
    image.putdata(pixels)
    return image

def encrypt_by_math_operation(image):
    pixels = list(image.getdata())
    new_pixels = []

    for pixel in pixels:
        if isinstance(pixel, int):
            new_pixel = 255 - pixel  # For grayscale
        else:
            new_pixel = tuple(255 - val for val in pixel)  # For RGB
        new_pixels.append(new_pixel)

    image.putdata(new_pixels)
    return image

def main():
    print("=== Simple Image Encryption Tool ===")
    image_path = r"C:\Users\SANTHOSH KUMAR\Pictures\S logo.jpg"
    image = load_image(image_path)

    if image is None:
        return

    print("\nChoose Encryption Method:")
    print("1. Swap Pixel Values (reverse)")
    print("2. Apply Mathematical Operation (invert colors)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        encrypted_image = encrypt_by_swapping(image)
    elif choice == '2':
        encrypted_image = encrypt_by_math_operation(image)
    else:
        print("Invalid choice.")
        return

    output_path = input("Enter output image filename (e.g., output.png): ").strip()
    save_image(encrypted_image, output_path)

if __name__ == "__main__":
    main()
