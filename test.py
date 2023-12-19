import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

hf_token = os.getenv('HUGGINGFACE_TOKEN')

def generate_response(full_prompt, max_length=100, num_beams=3):
    """
    Generate a response from the model based on a given prompt using beam search.

    This function takes a prompt, encodes it for the model, and generates a response. 
    It uses beam search to enhance the quality of the response. The function is optimized for 
    memory usage by clearing the CUDA cache and using torch.no_grad().

    Args:
        full_prompt (str): The prompt to which the model will generate a response.
        max_length (int): The maximum length of the model's response.
        num_beams (int): The number of beams to use in beam search for diversity in responses.

    Returns:
        str: The text generated by the model as a response to the prompt.

    The generated text is post-processed to ensure proper formatting, remove any 'EOS' tokens,
    and to ensure it doesn't contain the initial prompt.
    """
    # Set the device for computation based on CUDA availability
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    # Encode the combined prompt
    input_ids = tokenizer.encode(full_prompt, return_tensors='pt').to(device)

    # Generate response using the model with beam search
    output = model.generate(
        input_ids, 
        max_length=max_length,
        num_beams=num_beams,  # Set number of beams for beam search
        no_repeat_ngram_size=2,  # Prevents the model from repeating short phrases
        early_stopping=True,    # Stops when a sentence is completed
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode the output
    response_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Truncate at the last complete sentence if possible
    sentences = response_text.split('.')
    response_text = '.'.join(sentences[:-1]) + ('.' if len(sentences) > 1 else '')

    # Remove the 'EOS' token and any trailing spaces from the response
    response_text = response_text.replace("EOS", "").strip()

    # Ensure the response does not contain the full prompt
    if response_text.startswith(full_prompt):
        response_text = response_text[len(full_prompt):]

    # Trim leading and trailing spaces again after adjustments
    response_text = response_text.strip()

    return response_text
# Load the fine-tuned model and tokenizer
model = AutoModelForCausalLM.from_pretrained('RickSanchez-7b-q', token=hf_token)
tokenizer = AutoTokenizer.from_pretrained('RickSanchez-7b-q')

# Set the system prompt as in your Jupyter notebook
system_prompt = "You are Rick Sanchez from Rick and Morty. You are an eccentric and cynical genius. Respond in complete sentences, and only as Rick."

# Interactive testing of the model
if __name__ == "__main__":
    while True:
        user_input = input("Enter your input (type 'exit' to stop): ")
        if user_input.lower() == 'exit':
            break
        full_prompt = f"{system_prompt}\nMorty: {user_input}\nRick:"
        print("Rick's response:", generate_response(full_prompt))

