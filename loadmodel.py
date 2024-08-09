from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch 

#load procesor and model
def load_model():
    model_name = 'Salesforce/blip2-opt-2.7b'
    processors = Blip2Processor.from_pretrained("processor/"+model_name)
    model      = Blip2ForConditionalGeneration.from_pretrained("model/"+model_name, 
                                                                torch_dtype=torch.float32)
                                                                #load_in_8bit=True, if you don't run the code with the GPU can't use the quantization
                                                                #torch_dtype=torch.float16)
    
    return processors, model