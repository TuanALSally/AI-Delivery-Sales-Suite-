from transformers import pipeline, BertTokenizer, BertModel
import random

# Set up GPT-2 and mBERT
writer = pipeline("text-generation", model="gpt2")
tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")
model = BertModel.from_pretrained("bert-base-multilingual-cased")

# Fake menu for testing
menu_items = ["Burger $10", "Pizza $12", "Fries $3", "Soda $2"]

# Promo Agent - 3 discount ideas
def promo_agent():
    prompt = "Create a food discount deal: "
    deals = writer(prompt, max_length=20, num_return_sequences=3, truncation=True)
    return [deal["generated_text"] for deal in deals]

# Lurer Agent - 2 quick messages
def lurer_agent():
    prompt = "Write a short message to attract food orders: "
    messages = writer(prompt, max_length=15, num_return_sequences=2, truncation=True)
    return [msg["generated_text"] for msg in messages]

# Menu Agent - Pick 2 items and describe
def menu_agent(menu):
    top_items = random.sample(menu, 2)
    descriptions = []
    for item in top_items:
        prompt = f"Describe this food item: {item.split()[0]} - "
        desc = writer(prompt, max_length=20, num_return_sequences=1, truncation=True)
        descriptions.append(desc[0]["generated_text"])
    return list(zip(top_items, descriptions))

# Surge Agent - Guess busy time + deal
def surge_agent():
    hours = ["11 AM", "12 PM", "1 PM", "6 PM", "7 PM"]
    busy_time = random.choice(hours)
    prompt = f"Create a deal for {busy_time}: "
    deal = writer(prompt, max_length=20, num_return_sequences=1, truncation=True)
    return f"{busy_time} - {deal[0]['generated_text']}"

# Bumper Agent - Suggest 2 add-ons
def bumper_agent(menu):
    add_ons = random.sample(menu, 2)
    suggestions = []
    for item in add_ons:
        prompt = f"Suggest an add-on: {item.split()[0]} for "
        suggestion = writer(prompt, max_length=15, num_return_sequences=1, truncation=True)
        suggestions.append(suggestion[0]["generated_text"])
    return suggestions

# Boost Agent - 1 big welcome deal
def boost_agent():
    prompt = "Create a welcome deal for a new restaurant: "
    deal = writer(prompt, max_length=25, num_return_sequences=1, truncation=True)
    return deal[0]["generated_text"]

# Trend Agent - Find trending food
def trend_agent():
    trending_foods = ["Tacos", "Sushi", "Pizza", "Burgers", "Pasta"]
    trending_food = random.choice(trending_foods)
    return f"{trending_food} is trending—push it!"

# Area Agent - Local boost deal
def area_agent(zip_code="10001"):
    zip_to_city = {"10001": "NYC", "90210": "LA", "60601": "Chicago"}
    city = zip_to_city.get(zip_code, "Your city")
    prompt = f"Create a lunch deal for {city}: "
    deal = writer(prompt, max_length=20, num_return_sequences=1, truncation=True)
    return f"{city} - {deal[0]['generated_text']}"

# Competitor Agent - Beat rival deals
def competitor_agent():
    rival_deal = "20% off"
    rival_discount = int(rival_deal.split("%")[0])
    our_discount = rival_discount + 5
    return f"Rival has {rival_deal}? We'll do {our_discount}% off!"

# Remote Agent - Set up deals (placeholder)
def remote_agent(deal=""):
    return f"Remote setup: Your deal '{deal}' is live!"

# Smart Bundle Agent - Create 2-3 combos
def smart_bundle_agent(menu):
    bundles = random.sample(menu, 3)
    combo = f"{bundles[0].split()[0]} + {bundles[1].split()[0]} + {bundles[2].split()[0]}"
    prompt = f"Price this combo: {combo} for "
    price = writer(prompt, max_length=15, num_return_sequences=1, truncation=True)
    return f"Combo: {combo} for {price[0]['generated_text']}"

# Test all agents
print("Promo Agent Deals:", promo_agent())
print("Lurer Agent Messages:", lurer_agent())
print("Menu Agent Picks:", menu_agent(menu_items))
print("Surge Agent Suggestion:", surge_agent())
print("Bumper Agent Add-Ons:", bumper_agent(menu_items))
print("Boost Agent Deal:", boost_agent())
print("Trend Agent Suggestion:", trend_agent())
print("Area Agent Deal:", area_agent())
print("Competitor Agent Counter:", competitor_agent())
print("Remote Agent Setup:", remote_agent("10% off today"))
print("Smart Bundle Agent Combo:", smart_bundle_agent(menu_items))