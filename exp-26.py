from transformers import MarianMTModel, MarianTokenizer
def translate_to_french(text):
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    input_ids = tokenizer.encode(text, return_tensors="pt")
    translation_ids = model.generate(input_ids)
    translation = tokenizer.decode(translation_ids[0], skip_special_tokens=True)
    return translation
if __name__ == "__main__":
    english_text = "Hello, how are you?"
    french_translation = translate_to_french(english_text)
    print("Input (English):", english_text)
    print("Translation (French):", french_translation)
