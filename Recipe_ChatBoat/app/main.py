from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from transformers import T5Tokenizer, T5ForConditionalGeneration
import uvicorn
from fastapi.templating import Jinja2Templates



app = FastAPI()

# Mount static folder for JS/CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Load trained model
MODEL_DIR = "./recipe_model"
tokenizer = T5Tokenizer.from_pretrained(MODEL_DIR)
model = T5ForConditionalGeneration.from_pretrained(MODEL_DIR)

# Ingredient normalization function (same as training)
def normalize_ingredients(ing_str):
    """
    Normalize ingredient input into clean natural-language format.
    """
    # Replace commas with space
    ing_str = ing_str.lower().replace(",", " ")

    # Split on whitespace
    ingredients = ing_str.split()

    # Remove duplicates & sort
    ingredients = sorted(set(ingredients))

    return " ".join(ingredients)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )



@app.post("/predict")
async def predict(ingredient: str = Form(...)):
    # Normalize input like in training
    ingredient_input = normalize_ingredients(ingredient)
    
    # Tokenize and generate
    inputs = tokenizer(ingredient_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50)
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return {"recipe": recipe}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
