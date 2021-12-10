from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    prompts = story.prompts

    return render_template('home.html', prompts=prompts)

@app.route('/story')
def story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)
     


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)