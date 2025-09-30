from flask import Flask
from routes import nasz_blueprint
from views import my_blueprint

app = Flask(__name__)

app.register_blueprint(nasz_blueprint)
app.register_blueprint(my_blueprint)

if __name__ == "__main__":
    app.run(debug=True)