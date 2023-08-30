from flask import Flask
import environ

app = Flask(__name__)

# Initializing environment variables
env = environ.Env()
environ.Env.read_env()

@app.route('/test', methods=['GET', 'POST'])
def test_page():
    return env('TEST')

