# KaniTamil - குறளோவியம்
--- 
### A generative AI project based on the literary work குறளோவியம்
---

The project aims to enrich Tamil language learning experience by leveraging generative AI to create contextually relevant images inspired by Kuralovium, facilitating a deeper understanding of the literary nuances embedded in the Tirukkural-based work. The proposed solution comprises a generative AI model for creating contextually relevant images. It includes a sophisticated image annotation system in Tamil, enabling users to contribute insights. This collaborative platform enhances Tamil language learning through visually
immersive content and community-driven exploration of குறளோவியம்'s intricacies. 

#### Progressive milestones:
- Research on current generative AI for image and text generation.
- Extracting images from the digital version of the literary work (குறளோவியம்.pdf) and processing the text using OCR from Google Cloud's [CloudVision](https://cloud.google.com/vision?hl=en) API.
- Processing the text further with Google's [PaLM](https://ai.google.dev/docs/palm_api_overview) API to generate image captions which shall be given as the input for our image generating model.

#### To-do:
- Look for alternatives to PaLM API as translating the extracted text to english to tamil might cause lose in effectiveness.
- Use an image generative model to generate contextually relevant images
- Create a frontend that users can access all the images along with the relevant text from the literary work.
- Allow user annotations on the images from the frontend.
---

### Results:
Image extraction:
![Alt text](/assets/image-2.png)

![Alt text](/assets/image-3.png)

OCR:
![Execution](/assets/image-1.png) 

![Extracted text](/assets/image.png)

