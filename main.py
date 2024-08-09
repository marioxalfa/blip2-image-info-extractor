from loadmodel import load_model
import torch
from utils import extract_image

processor, model = load_model()

device = "cuda" if torch.cuda.is_available() else "cpu"
#print(device)

image = extract_image("img/image.jpg")

prompt = "Question: what is the description of the image? Answer:"

inputs = processor(images=image, text=prompt, return_tensors="pt", padding=True).to(device=device, 
                                                                                    dtype=torch.float32)
                                                                                    #dtype=torch.float16)
generated_ids = model.generate(**inputs)

generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
print(generated_text)
