import argparse
from PIL import Image

# Convert the WEBP image to a PNG image and return the image object
def convert_webp_to_png(webp_image_path, png_image_path):
    img = Image.open(webp_image_path)
    img.save(png_image_path, 'PNG')
    return img

def main():
    parser = argparse.ArgumentParser(
        description="Converts a WebP image to PNG format.")

    # Positional arguments
    parser.add_argument("input", help="Input WebP image path")
    parser.add_argument("output", help="Output PNG image path")

    """ # Help option
    parser.add_argument("-h", "--help", nargs='?', const=True,
                        help="Show this help message and exit") """

    args = parser.parse_args()

    # Check if the input file is a WebP image
    if not args.input.lower().endswith('.webp'):
        print("Error: Input file must be a WebP image.")
        return

    # Convert the WebP image to a PNG image
    try:
        convert_webp_to_png(args.input, args.output)
    except Exception as e:
        print(f"Error: {e}")

    print(f"Converted {args.input} to {args.output}")


if __name__ == "__main__":
    main()
