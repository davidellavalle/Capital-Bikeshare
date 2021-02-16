# Flask-app

pickle library - pickled.dump() used to save the model to the local repository
-> model.pkl

index.html this file must be contained in a Templates folder because Heroku only understand it

model.py is the code of the model not written in ipynb

model.pkl -> created when I run the code the file where oickle.dump is

app.py
@app.route('/')
def home():
    return render_template("index.html") - this is returning to the home
    
    
Procfile
web: gunicorn app:app
python framework - integrate your web framework
web server interface for python - bridging the backend to the user interface
app:app -> if I call the App Davide it will be Davide:app

## Requirements
A list of Libraries used for the creation of the app and the gunicorn that connects.......

sample.ipynb is the anylzsis of the data, the data trasnforming etc  to the creation of the model

heroku understands finally just what is written in app.py
