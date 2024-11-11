from flask import Flask
from cr_playwright.auth_settings.controller import update_auth_settings
app = Flask(__name__)
@app.route('/auth-settings', methods=['POST'])
def update():
    return update_auth_settings()
@app.route('/', methods=['GET'])
def index():
    return 'App is Working!'

@app.route('/', methods=['POST'])
def hi():
    return 'Post is Working!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
