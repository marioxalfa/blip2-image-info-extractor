from transformers import Blip2Processor, Blip2ForConditionalGeneration

#save tokens
model_name = 'Salesforce/blip2-opt-2.7b'
processor = Blip2Processor.from_pretrained(model_name)
processor.save_pretrained(f"processor/{model_name}")

#save model
model = Blip2ForConditionalGeneration.from_pretrained(model_name)
model.save_pretrained(f"model/{model_name}")