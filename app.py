from flask import Flask, render_template, jsonify
from flask_cors import CORS

# instantiate the app
app = Flask(__name__, static_folder='./dist/static',
            template_folder='./dist')
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
