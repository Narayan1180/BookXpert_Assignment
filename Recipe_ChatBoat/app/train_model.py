from datasets import load_dataset
from transformers import (
    T5Tokenizer,
    T5ForConditionalGeneration,
    Trainer,
    TrainingArguments
)

MODEL_NAME = "google/flan-t5-small"

# Load tokenizer and model
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)

# Load dataset (JSON with 'ingredients' and 'recipe')
dataset = load_dataset("json", data_files="recipe_data/recipe.json", split="train")

# Ingredient normalization function
def normalize_ingredients(ing_list):
    """
    Normalize ingredient list into a clean, sorted natural-language string.
    """
    normalized = []
    for ing in ing_list:
        if isinstance(ing, str):
            ing = ing.lower().strip()
            ing = " ".join(ing.split())  # remove extra spaces
            normalized.append(ing)

    normalized = sorted(set(normalized))
    return " ".join(normalized)

# Preprocess dataset
def preprocess(batch):
    # Join and normalize ingredients
    if isinstance(batch["ingredients"], list):
        batch["ingredients"] = [normalize_ingredients(ing) if isinstance(ing, list) else ing for ing in batch["ingredients"]]
    
    # Tokenize inputs and outputs
    inputs = tokenizer(
        batch["ingredients"],
        padding="max_length",
        truncation=True,
        max_length=64
    )
    outputs = tokenizer(
        batch["recipe"],
        padding="max_length",
        truncation=True,
        max_length=32
    )

    # Set labels for T5
    inputs["labels"] = outputs["input_ids"]
    return inputs

# Apply preprocessing
tokenized = dataset.map(preprocess, batched=True, remove_columns=["ingredients", "recipe"])

# Training configuration
training_args = TrainingArguments(
    output_dir="./recipe_model",
    per_device_train_batch_size=4,
    num_train_epochs=20,
    learning_rate=3e-4,
    logging_steps=10,
    save_strategy="epoch",
    report_to="none"
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized
)

# Train the model
trainer.train()

# Save trained model and tokenizer
model.save_pretrained("./recipe_model")
tokenizer.save_pretrained("./recipe_model")

print("Model trained and saved successfully.")
