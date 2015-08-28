from flask import Flask, render_template
from flask.ext.babel import Babel, refresh

import markdown

app = Flask(__name__)
DEBUG = True
BABEL_DEFAULT_LOCALE = 'es'
app.config.from_object(__name__)
babel = Babel(app)

@app.route("/")
def index_es():
    app.config['BABEL_DEFAULT_LOCALE'] = 'es'
    refresh()
    with open('sources/descripcion.md') as fh:
        description = markdown.markdown(fh.read())
    return render_template('index.html', description=description)

@app.route("/en/")
def index_en():
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    refresh()
    with open('sources/descripcion_en.md') as fh:
        description = markdown.markdown(fh.read())
    return render_template('index.html', description=description)

if __name__ == "__main__":
    app.run()
