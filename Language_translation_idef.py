from transformers import AutoTokenizer, AutoModelForImageTextToText
import torch

def translate_hindi_to_french(text):
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("HuggingFaceM4/Idefics3-8B-Llama3")
    model = AutoModelForImageTextToText.from_pretrained("HuggingFaceM4/Idefics3-8B-Llama3")
    
    # Set target language to French
    tokenizer.tgt_lang = "fr"
    
    # Prepare input
    encoded_hi = tokenizer(text, return_tensors="pt")
    
    # Generate translation
    with torch.no_grad():
        generated_tokens = model.generate(**encoded_hi)
    
    # Decode output
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    return translated_text

if __name__ == "__main__":
    hindi_text = "नमस्ते, आप कैसे हैं?"
    french_translation = translate_hindi_to_french(hindi_text)
    print(f"Hindi: {hindi_text}\nFrench: {french_translation}")
