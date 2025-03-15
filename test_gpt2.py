from transformers import pipeline

# Load GPT-2
writer = pipeline("text-generation", model="gpt2")

# Simple test
test_prompt = "Give me a restaurant discount: "
test_output = writer(test_prompt, max_length=20, num_return_sequences=1, pad_token_id=writer.tokenizer.eos_token_id, truncation=True, do_sample=True, top_k=10, top_p=0.6)
print("Test says:", test_output[0]["generated_text"].replace(test_prompt, '').strip())