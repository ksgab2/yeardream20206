from transformers import pipeline

# Load the classification pipeline with the specified model
pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

# Classify a new sentence
sentence = "음식점이너무 쌰갈스러웠습니다."
result = pipe(sentence)

# Print the result
print(result)
