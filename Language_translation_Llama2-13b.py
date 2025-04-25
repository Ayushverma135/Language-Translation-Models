from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
article_en = "The head of the United Nations says there is no military solution in Syria"
model = MBartForConditionalGeneration.from_pretrained("SnypzZz/Llama2-13b-Language-translate")
tokenizer = MBart50TokenizerFast.from_pretrained("SnypzZz/Llama2-13b-Language-translate", src_lang="en_XX")

model_inputs = tokenizer(article_en, return_tensors="pt")

# Translate to Hindi and print the result
generated_tokens = model.generate(
    **model_inputs,
    forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]
)
hindi_translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print("Hindi translation:", hindi_translation)

# Translate to Chinese and print the result
generated_tokens = model.generate(
    **model_inputs,
    forced_bos_token_id=tokenizer.lang_code_to_id["de_DE"]
)
chinese_translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print("Chinese translation:", chinese_translation)