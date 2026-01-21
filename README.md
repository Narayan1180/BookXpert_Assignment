# Recipe_ChatBoat – AI/ML Assignment

## Task 1: Name Matching System
- Uses Levenshtein similarity score
- Returns best match and ranked list

Run:
python task1_word_matching_search.py

## Task 2: Recipe Chatbot (Local LLM)
- Model: FLAN-T5 (google/flan-t5-small)
- Framework: FastAPI
- Input: Ingredients
- Output: Recipe Name

### Setup
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate   # Windows

pip install -r requirements.txt

### Train Model
python train_model.py

### Run Server
uvicorn app.main:app --reload

Open:
http://127.0.0.1:8000

### Example
Input: egg onion
Output: Egg Omelette

