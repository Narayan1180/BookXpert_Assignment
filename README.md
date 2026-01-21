# open file in vscode Recipe_ChatBoat

for Task 1 I have used Levenshtein similarty score  after that retrun output in descending order of matching  score 1 to 0

run 
python task1_word_matching_search.py

then enter any name like Gita on console

Hi there
Enter a name: Gita

# output 
Best Match: ('Gita', 1.0)
Other Matches: [('Gita', 1.0), ('Githa', 0.8888888888888888), ('Gitu', 0.75), ('Sita', 0.75), ('Rita', 0.75)]


#Task 2 Recipe ChatBoat 

# create virtual environment
python -m venv venv

# activate venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

# install all necessary dependencies 
pip install -r requirements.txt
# then Inside our app folder run train_model .py to train model that will used inside post api /predict 
python train_model.py # this will train the model and sav it in project folder without this don,t proceed
# to start server run below command in u r terminal or cmd
python uvicorn -m app.main:app --reload
# server will start at localhost
http://127.0.0.1:8000 # click on the link it will take u to our chatboat page 

# enter ingredient like egg onion it will predict recipe Omelette 

# inside recipe data we havee use recipe.json to train our model from there take test ingredient and match the output

# Inside our folder get and post api endpoints r written .

I have used a small open-source LLM (FLAN-T5) from Hugging Face because it is lightweight, instruction-tuned, runs locally, and works well for text-to-text tasks like mapping ingredients → recipe name.
The Transformers library is used because it provides production-ready implementations for loading, fine-tuning, and serving LLMs easily.

