from flask import Flask

# função create_app aplicação do app
def create_app():
    app = Flask(__name__)

    return app