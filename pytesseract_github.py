import cv2
from PIL import Image
import pytesseract
import subprocess
#import os uncomment, if you are on windows

def character_recognition():
    image_to_be_processed = cv2.imread('path_to_image')
    converted = pytesseract.image_to_string(image_to_be_processed)
    f = open('path_to_the_textfile','w')
    f.write(converted)
    f.close()
 
#   if you are on windows, then 
#   "uncomment this line" os.startfile("filename.txt") and comment the next line
    subprocess.call(['open','-a','TextEdit','path_to_the_text'])
    original_image = Image.open('path_to_image')
    original_image.show()
    
    
    
character_recognition()
