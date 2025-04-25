from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def chatbot_response(prompt):
    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained("MAGAer13/mplug-owl2-llama2-7b")
    tokenizer = AutoTokenizer.from_pretrained("MAGAer13/mplug-owl2-llama2-7b")
    
    # Tokenize input prompt
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generate response
    with torch.no_grad():
        output_tokens = model.generate(**inputs, max_length=200)
    
    # Decode output
    response = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    user_prompt = "What is the capital of France?"
    bot_response = chatbot_response(user_prompt)
    print(f"User: {user_prompt}\nBot: {bot_response}")
