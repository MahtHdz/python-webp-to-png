
# WebP to PNG Converter

This Python script is designed to convert WebP images to PNG format. It provides a straightforward way to convert WebP images to a more widely supported format, making it easier to work with images in various applications.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example](#example)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Prerequisites

Before using this script, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- Pillow library (PIL)

To create a virtual environment on python run:

```bash
python -m venv venv
```

Activate the virtual environment by running:

```bash
source venv/bin/activate
```

If you are using Windows, run in Powershell:

```bash
venv\Scripts\Activate.ps1
```

You can install the script requirements by running:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is located.

    ```bash
    cd python-webp-to-png
    ```

4. Run the script with the following command:

    ```bash
    python main.py input.webp output.png
    ```

Replace `input.webp` with the path to the WebP image you want to convert and `output.png` with the desired name for the converted PNG image. The converted PNG image will be saved in the same directory as the script.

## Example

```bash
python main.py my_image.webp my_image.png
```

This command will convert `my_image.webp` to `my_image.png`.

## License

This script is released under the MIT License.

## Acknowledgments

- Pillow - The Python Imaging Library that makes image processing easy.
- Inspired by the need to convert WebP images to PNG for broader compatibility.
