# blip2-image-info-extractor
## Extract information from images with a prompt

This simple project allows you to download the LLM model Blip2 locally and use it to extract simple information from an image

### Steps
1. Create the virtual env
2. Install dependencies with pip
3. Run the savemodel.py file to download the model locally
4. Run the main.py to load the model and get the extraction
5. Edit the prompt and have fun

#

**NOTE:**
If the device in the main.py (line 7) is cuda, you will be able to use your GPU and the model will be faster. Also you can change the dtype=torch.float32 in dtype=torch.float16. You can also decomment the line 10 of the loadmodel.py to use the quantization