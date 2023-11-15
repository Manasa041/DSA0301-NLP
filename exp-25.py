import openai
api_key = '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'
prompt = "Translate the following English text to French: 'Hello, how are you?'"
response = openai.Completion.create(
    engine="text-davinci-002", 
    prompt=prompt,
    max_tokens=50  
)
generated_text = response.choices[0].text
print("Generated Text:")
print(generated_text)
