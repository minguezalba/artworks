"""App configuration module."""
from flasgger import Swagger  # type: ignore
from flask import Flask
from flask_compress import Compress  # type: ignore

from artworks.routes.artworks import api


app = Flask(__name__, static_url_path='/', static_folder='docs/_build/')
app.register_blueprint(api)
app.url_map.strict_slashes = False

# Compress all responses with gzip
Compress(app)


app.config["SWAGGER"] = {
    "title": "Artworks",
    "uiversion": 3,
}

swag = Swagger(
    app,
    template={
        "swagger": "2.0",
        "info": {
            "title": "Artworks",
            "version": "1.0",
        },
        "consumes": [
            "application/json",
        ],
        "produces": [
            "application/json",
        ],
    },
)


@app.route('/docs', methods=['GET'])
@app.route('/docs/<path:path>', methods=['GET'])
def docs(path='index.html'):
    """Library documentation endpoint.
    ---
    tags:
        - Docs
    parameters:
        - name: path
          in: path
          description: Path to documentation
    responses:
        200:
            description: Documentation
    """
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run()
