import json

with open("recipe_data/recipe.json") as f:
    recipes = json.load(f)

train_data = []

for item in recipes:
    ingredients = ", ".join(item["ingredients"])
    prompt = f"Suggest an Indian recipe using: {ingredients}"
    response = f"{item['recipe']}. {item['steps']}"

    train_data.append({
        "input": prompt,
        "output": response
    })

with open("recipe_data/train.json", "w") as f:
    json.dump(train_data, f, indent=2)

print("Training data prepared:", len(train_data))
