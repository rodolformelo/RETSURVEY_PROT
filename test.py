import torch
from transformers import pipeline

# Test PyTorch installation
x = torch.rand(5, 3)
print(x)


# Test Transformers installation
nlp = pipeline('sentiment-analysis')
result = nlp('I love using Transformers library!')
print(result)