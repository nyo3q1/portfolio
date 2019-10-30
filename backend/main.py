from . import settings
from .gcs import Content

from flask import Flask, render_template, jsonify, abort
from flask_cors import CORS

import logging
logger = logging.getLogger()

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist'
)
cors = CORS(app, resources={r"/api/*": {"origins": settings.CORS_ORIGINS}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@app.route('/api/<path:name>')
def contents(name):
    content = Content(name)
    if not content.exists():
        abort(404)

    if content.isdir():
        _name = name if name.endswith("/") else name + "/"
        index_md = Content(_name + "index.md")
        if index_md.exists():
            content = index_md

    return jsonify({
        'isdir': content.isdir(),
        'content': content.get()
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
