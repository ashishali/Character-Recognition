# Character Recognition:

This repository contains a python code that recognizes characters from an image file and writes/inputs them into a textfile.

## Prerequisites:

Install OpenCV:

```bash
pip install opencv-python 
```

Install pytesseract:
```bash
pip install pytesseract
```

Install pillow:
```bash
pip install pillow
```

## Usage

```python
# import necessary packages
import cv2
from PIL import Image
import pytesseract
import subprocess
import os
```

```python
image_to_be_processed = cv2.imread('path_to_image') # read the image and store it to a variable
converted = pytesseract.image_to_string(image_to_be_processed) # convert it to string
```

```python
f = open('path_to_the_textfile','w') # open a file in write mode
f.write(converted) # write the characters recognised into the file
f.close() # save and close file
```

```python
subprocess.call(['open','-a','TextEdit','path_to_the_text']) # open your .txt file
original_image = Image.open('path_to_image') 
original_image.show() # opens your image file
```

### cv2.imread(): 
Used to read the image from a specific path.
### pytesseract.image_to_be_string(): 
Using pytesseract to recognize the characters in the image.
### subprocess.call():
This method helps launch your .txt file.(basically used to launch a program).
### Image.open():
Using pillow to load image.
### show()
Displaying the image.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
