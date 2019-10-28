from env import env
from gcs import Content

from flask import Flask, render_template, jsonify, abort
from flask_cors import CORS

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist'
)
cors = CORS(app, resources={r"/api/*": {"origins": env.CORS_ORIGINS}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@app.route('/api/<path:name>')
def contents(name):
    content = Content(name)
    if not content.exists():
        abort(404)

    obj = {
        'isdir': content.isdir(),
        'content': content.get()
    }

    return jsonify(obj)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
