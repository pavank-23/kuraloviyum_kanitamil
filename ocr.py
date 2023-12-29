import fitz
from typing import Tuple
from google.cloud import vision
import os
from dotenv import load_dotenv
import google.generativeai as palm

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
    client = vision.ImageAnnotatorClient()
    with open(file, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    for text in texts:
        res.append(text.description)
    if response.error.message:
        raise Exception(
            print(response.error.message)
        )
    
# Generating image captions
def generate_caption(content, image_captions):
    load_dotenv()
    api_key = os.getenv("PALM_API_KEY")
    palm.configure(api_key=api_key)
    prompt = """
    You write detailed captions for images that image generating AIs can understand.
    Generate a caption for an image which helps in enhancing the understanding of the following piece of literary work: 
    """ + content + """
    Think about it carefully and generate a detailed caption of 3 sentences.
    """
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    completion = palm.generate_text(
        model=model,
        prompt=prompt
    )
    print(completion.result)
    
if __name__ == "__main__":
    import sys
    import glob
    input_file = sys.argv[1]
    # pdf2img(input_file)
    pngCounter = len(glob.glob1('.',"*.png"))
    res = []
    chapters = [0, 4, 6, 8,10, 12, 13, 15, 17, 18, 20, 22, 24, 26, 28, 30, 32, 35, 38, 40, 43, 45, 47, 50, 52, 56]
    print(pngCounter)
    for i in range(pngCounter):
        ocr("page_%s.png" % i, res)
    image_captions = []
    for i in range(1, len(chapters)):
        generate_caption("".join(res[chapters[i - 1]: chapters[i]]), image_captions)
    
