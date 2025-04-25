from transformers import AutoProcessor, AutoModelForImageTextToText
import torch

def translate_hindi_to_french(text):
    # Load processor and model
    processor = AutoProcessor.from_pretrained("Salesforce/instructblip-vicuna-7b")
    model = AutoModelForImageTextToText.from_pretrained("Salesforce/instructblip-vicuna-7b")

    # Create input prompt
    prompt = f"Translate the following Hindi text to French:\n{text}"

    # Tokenize input
    inputs = processor(text=prompt, return_tensors="pt")

    # Generate translation
    with torch.no_grad():
        generated_tokens = model.generate(**inputs)

    # Decode output
    translated_text = processor.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    return translated_text

if __name__ == "__main__":
    hindi_text = "नमस्ते, आप कैसे हैं?"
    french_translation = translate_hindi_to_french(hindi_text)
    print(f"Hindi: {hindi_text}\nFrench: {french_translation}")
