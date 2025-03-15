from transformers import pipeline, BertTokenizer, BertModel

# Load AI - GPT-2 writes, mBERT thinks
writer = pipeline("text-generation", model="gpt2")
tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
model = BertModel.from_pretrained("bert-base-multilingual-cased")

# Promo Agent - 5 unique restaurant discounts
promo_prompt = "Generate 5 short restaurant discounts, e.g., '20% off lunch', '$5 off orders', 'Buy one pizza, get one free': "
promos = writer(promo_prompt, max_length=20, num_return_sequences=5, pad_token_id=writer.tokenizer.eos_token_id, truncation=True, do_sample=True, top_k=10, top_p=0.6, temperature=0.7)
print("Promo Agent says:")
for i, promo in enumerate(promos, 1):
    print(f"{i}. {promo['generated_text'].replace(promo_prompt, '').strip()}")

# Lurer Agent - 2 catchy restaurant promos
lure_prompt = "Create 2 short, catchy restaurant promos, e.g., '$5 off now', 'Free drink today': "
lures = writer(lure_prompt, max_length=15, num_return_sequences=2, pad_token_id=writer.tokenizer.eos_token_id, truncation=True, do_sample=True, top_k=10, top_p=0.6, temperature=0.7)
print("\nLurer Agent says:")
for i, lure in enumerate(lures, 1):
    print(f"{i}. {lure['generated_text'].replace(lure_prompt, '').strip()}")

# Menu Agent - 2 top items with descriptions
menu_prompt = "Name exactly 2 restaurant items with short descriptions, e.g., 'juicy burgers', 'crispy fries': "
menu_items = writer(menu_prompt, max_length=25, num_return_sequences=1, pad_token_id=writer.tokenizer.eos_token_id, truncation=True, do_sample=True, top_k=10, top_p=0.6, temperature=0.7)[0]["generated_text"]
print("\nMenu Agent says:", menu_items.replace(menu_prompt, '').strip())

# Surge Agent - 1 busy time + tactic
surge_sentence = "Lunch is busy!"
surge_tokens = tokenizer(surge_sentence, return_tensors="pt")
surge_output = model(**surge_tokens)  # mBERT processes the busy time
surge_tactic = writer("Suggest a short deal for a busy lunch, e.g., '15% off lunch': ", max_length=15, num_return_sequences=1, pad_token_id=writer.tokenizer.eos_token_id, truncation=True, do_sample=True, top_k=10, top_p=0.6, temperature=0.7)[0]["generated_text"]
print("\nSurge Agent says:", surge_tactic.replace("Suggest a short deal for a busy lunch, e.g., '15% off lunch': ", '').strip())

# Bumper Agent - 2 food add-ons with prices
bumper_prompt = "Suggest exactly 2 food add-ons with prices, e.g., 'fries for $2', 'soda for $1': "
bumpers = writer(bumper_prompt, max_length=15, num_return_sequences=2, pad_token_id=writer.tokenizer.eos_token_id, truncation=True, do_sample=True, top_k=10, top_p=0.6, temperature=0.7)
print("\nBumper Agent says:")
for i, bumper in enumerate(bumpers, 1):
    print(f"{i}. {bumper['generated_text'].replace(bumper_prompt, '').strip()}")