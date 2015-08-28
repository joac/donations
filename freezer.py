from flask.ext.frozen import Freezer
from donations import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
