# Cobra Cartoonizer

Cobra Cartoonizer is a Python-based application that allows users to apply various cartoon and artistic filters to images. Built with OpenCV and Tkinter, this tool provides a user-friendly interface for image processing, enabling users to transform their photos into fun, artistic renditions.

## Features

- **Image Selection**: Users can select images from their file system.
- **Filter Options**: Apply a variety of filters, including:
- Cartoon
- Sketch
- Pencil
- Color Filter
- Grayscale
- Blur
- Edge Detection
- Sepia
- Negative
- Emboss
- Sharpen
- Posterization
- Pencil Sketch
- HDR
- Pixelate
- Bilateral Filter
- Stylization
- Pencil Color
- Motion Blur
- Median Blur
- Canny
- Gaussian Blur
- Brighten
- Darken
- Inverse
- Saturation Boost
- Color Swap
- Solarize

- **Image Preview**: Preview the selected image and the applied filter.
- **Image Saving**: Save the processed image in PNG or JPEG formats.
- **Reset Functionality**: Clear the selected image and reset settings.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Pillow
- Tkinter

You can install the required packages using pip in your Command Prompt or in your Virtual env:

```bash
pip install opencv-python numpy pillow
```

# Usage

## 1. Clone the repository or download the source code.
   ```bash
       git clone https://github.com/kingofallsnakes/Cobra_Cartoonizer.git
   ```
## 2. Navigate to the project directory in Cmd or in vs code.
   ```bash
       cd Cobra_Cartoonizer_main
  ```
## 3. Run the application:
  ```bash
       python main.py
   ```
![Screenshot 2024-10-15 070614](https://github.com/user-attachments/assets/08ec60cb-a7ca-4e64-a9e8-aa384255b3e2)
## 4. Select an image using the "Select Image" button pick an image in Training data.
![Screenshot 2024-10-15 070725](https://github.com/user-attachments/assets/8f95baa4-c88f-40e5-bd9a-a7a722b97a50)

## 5. Choose a filter from the dropdown menu.
![Screenshot 2024-10-15 071813](https://github.com/user-attachments/assets/4616b7af-86a0-41c1-b228-0a863146db07)
## 6. Click the "Apply Filter" button to see the effects.
![Screenshot 2024-10-15 071918](https://github.com/user-attachments/assets/5b9abadb-6f36-47e4-a16e-596c6b88edae)
## 7. Save the processed image using the "Save" button or reset the application with the "Reset" button.

# Before
![Screenshot 2024-10-15 070725](https://github.com/user-attachments/assets/8f95baa4-c88f-40e5-bd9a-a7a722b97a50)
# After
## Type 1
![Screenshot 2024-10-15 070743](https://github.com/user-attachments/assets/7a986a5d-d44d-4d6f-bca6-6592a3415e20)
## Type 2
![Screenshot 2024-10-15 070812](https://github.com/user-attachments/assets/d4d67524-88f0-4a83-9b06-55c77eab7af4)
## Type 3
![Screenshot 2024-10-15 070850](https://github.com/user-attachments/assets/d9afaa8f-9c21-4aed-861a-06956e1b1891)
## Type 4
![Screenshot 2024-10-15 070918](https://github.com/user-attachments/assets/6b174e6c-6f15-48c1-afec-33701d1784b9)

## Code Structure

- `Cartoonizer` class: Contains the image processing logic, including the rendering of cartoon effects and various filters.
- `App` class: Handles the GUI setup and user interactions.
