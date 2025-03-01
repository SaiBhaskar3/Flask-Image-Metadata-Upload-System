# Flask Image Metadata Upload System

This is a Flask-based web application that allows users to upload images and view their metadata, such as dimensions, file type, size, and more. The system automatically extracts metadata from the uploaded images and displays it on the webpage.

## Features

- **Image Upload:** Allows users to upload images.
- **Metadata Extraction:** Automatically extracts metadata such as:
  - Image size (in bytes)
  - Image type (e.g., PNG, JPEG)
  - Image dimensions (width and height)
  - Image creation time and modification time
- **User-friendly interface:** The app displays metadata in a readable format after the image is uploaded.

## Requirements

- Python 3.x
- Flask
- Pillow (PIL)
- Flask-Login (for user management)
- werkzeug

## Installation

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/SaiBhaskar3/Flask-Image-Metadata-Upload-System.git
