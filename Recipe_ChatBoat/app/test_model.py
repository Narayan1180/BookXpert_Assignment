from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load trained model and tokenizer
MODEL_PATH = "./recipe_model"
tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)

def predict_recipe(ingredients):
    """
    ingredients: list of strings or single string
    returns: predicted recipe name
    """
    # Convert list to space-separated string
    if isinstance(ingredients, list):
        input_text = " ".join(ingredients)
    else:
        input_text = str(ingredients)

    # Tokenize input
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=64
    )

    # Generate prediction
    outputs = model.generate(
        **inputs,
        max_length=32,
        num_beams=3,
        early_stopping=True
    )

    # Decode prediction
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return recipe

if __name__ == "__main__":
    print("Enter ingredients (comma or space separated). Type 'exit' to quit.")
    while True:
        user_input = input("Ingredients: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        # Split input into list
        if "," in user_input:
            ingredients = [x.strip() for x in user_input.split(",")]
        else:
            ingredients = user_input.split()

        recipe = predict_recipe(ingredients)
        print("Predicted Recipe:", recipe)
        print("-" * 40)
