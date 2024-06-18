# Medical Image Reconstruction

This project focuses on reconstructing medical images using the Radon Transform and various algorithms to enhance the quality of the reconstructions. It includes implementing the Radon and inverse Radon transforms, filtering techniques, and iterative reconstruction methods like SART (Simultaneous Algebraic Reconstruction Technique).

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Description
This project aims to reconstruct medical images from their sinograms using advanced image processing techniques. The main steps include applying the Radon Transform to create sinograms, using various filtering techniques to enhance the image, and reconstructing the original image using inverse Radon Transform and SART.

Key features:
- **Radon Transform**: Converts images into sinograms.
- **Inverse Radon Transform**: Reconstructs images from sinograms.
- **Filtering Techniques**: Enhances image quality by reducing noise.
- **SART**: An iterative method for high-quality image reconstruction.

## Installation
To install and run this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/osmancanaksoy/medical-image-reconstruction.git
    cd medical-image-reconstruction
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Here is a basic guide on how to use the project:
<p align="center">
  <img src="screenshots/gif.gif"/>
</p>

## Contributing
We welcome contributions to improve this project. Here are some ways you can contribute:

- **Report Bugs**: If you find a bug, please open an issue with detailed information.
- **Submit Pull Requests**: If you have a fix or a new feature, submit a pull request. Please ensure your code follows the project's coding standards.

## License
This project is licensed under the MIT License. See the [MIT License](LICENSE) file for more information.
