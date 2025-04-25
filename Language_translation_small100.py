# # Load model directly
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# hi_text = "जीवन एक चॉकलेट बॉक्स की तरह है।"
# chinese_text = "生活就像一盒巧克力。"

# tokenizer = AutoTokenizer.from_pretrained("alirezamsh/small100")
# model = AutoModelForSeq2SeqLM.from_pretrained("alirezamsh/small100")

# # translate Hindi to FrenchS
# tokenizer.tgt_lang = "de"
# encoded_hi = tokenizer(hi_text, return_tensors="pt")
# generated_tokens = model.generate(**encoded_hi)
# French=tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# print(French)
# # => "La vie est comme une boîte de chocolat."

# # translate Chinese to English
# tokenizer.tgt_lang = "de"
# encoded_zh = tokenizer(chinese_text, return_tensors="pt")
# generated_tokens = model.generate(**encoded_zh)
# tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# English=tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# print(English)
# # => "Life is like a box of chocolate."


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

def translate_hindi_to_french(text):
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("alirezamsh/small100")
    model = AutoModelForSeq2SeqLM.from_pretrained("alirezamsh/small100")
    
    # Explicitly set source and target languages
    tokenizer.src_lang = "hi"  # Hindi as source
    tokenizer.tgt_lang = "fr"  # French as target
    
    # Tokenize input
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


