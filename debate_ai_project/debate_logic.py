from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Load GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = TFGPT2LMHeadModel.from_pretrained(model_name)

def debate_logic(user_input):
    # Construct the debate prompt with a more specific instruction
    prompt = f"The user said: '{user_input}'. Provide a counter-argument."

    # Tokenize the prompt and generate the AI response with improved parameters
    input_ids = tokenizer.encode(prompt, return_tensors='tf')
    output = model.generate(
        input_ids,
        max_length=100,             # Limit the length of the response
        num_return_sequences=1,      # Only return one response
        no_repeat_ngram_size=3,      # Avoid repeating phrases
        temperature=0.7,             # Adjust the randomness of the response
        top_p=0.9                    # Use nucleus sampling for diversity
    )

    # Decode the response
    ai_response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Return only the AI's counterpoint (not the prompt or user input)
    return ai_response
