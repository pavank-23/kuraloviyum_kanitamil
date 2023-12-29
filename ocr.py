import fitz
from typing import Tuple
import easyocr

# Convert pdf to images
def pdf2img(input_file: str, pages: Tuple = None):
    doc = fitz.open(input_file)
    for page_index in range(len(doc)): 
        page = doc[page_index] 
        image_list = page.get_images()

        if image_list:
            print(f"Found {len(image_list)} images on page {page_index}")
        else:
            print("No images found on page", page_index)

        for image_index, img in enumerate(image_list, start=1): 
            xref = img[0]
            pix = fitz.Pixmap(doc, xref) 

            if pix.n - pix.alpha > 3:
                pix = fitz.Pixmap(fitz.csRGB, pix)

            pix.save("page_%s.png" % (page_index)) 
            pix = None

# Read characters
def ocr(file, res):
    reader = easyocr.Reader(['ta'], gpu = False)
    result = reader.readtext(file , detail = 0)
    res.append(" ".join(result))
    
if __name__ == "__main__":
    import sys
    import glob
    input_file = sys.argv[1]
    # pdf2img(input_file)
    pngCounter = len(glob.glob1('.',"*.png"))
    res = []
    chapters = [4, 6, 8,10, 12, 13, 15, 17, 18, 20, 22, 24, 26, 28, 30, 32, 35, 38, 40, 43, 45, 47, 50, 52, 56]
    # file = open('ocr.txt', 'w+')
    print(pngCounter)   
    for i in range(pngCounter):
        ocr('page_%s.png' % i, res)
    print(res)