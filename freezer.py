from flask.ext.frozen import Freezer
from donations import app

freezer = Freezer(app)

app.config['FREEZER_RELATIVE_URLS']=True

if __name__ == '__main__':
    freezer.freeze()
