from flask import Flask, render_template
from .db_model import db, User

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\bruno\\Desktop\\DSPT6-Twitoff\\twitoff\\twitoff.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())

    return app