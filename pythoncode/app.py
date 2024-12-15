from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

swagger_url = '/docs'
api_url = '/static/api-docs.json'

swagger_ui = get_swaggerui_blueprint(
    swagger_url,
    api_url,
    config={'app_name': "Library API"}
)

app.register_blueprint(swagger_ui, url_prefix=swagger_url)

library = []

@app.route('/books', methods=['POST'])
def create_books():
    book_data = request.get_json()
    if isinstance(book_data, list):
        library.extend(book_data)
    else:
        library.append(book_data)
    return jsonify({"status": "Books successfully added"}), 201

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(library)

@app.route('/books/search', methods=['GET'])
def find_books():
    search_params = {
        'author': request.args.get('author'),
        'published_year': request.args.get('published_year'),
        'genre': request.args.get('genre')
    }

    filtered_books = library
    for key, value in search_params.items():
        if value:
            if key == 'published_year':
                value = int(value)
            filtered_books = [book for book in filtered_books if book.get(key) == value]

    return jsonify(filtered_books)

@app.route('/books/<isbn>', methods=['DELETE'])
def remove_book(isbn):
    global library
    library = [book for book in library if book.get('isbn') != isbn]
    return jsonify({"status": "Book removed"}), 200

@app.route('/books/<isbn>', methods=['PUT'])
def modify_book(isbn):
    updated_data = request.get_json()
    for book in library:
        if book.get('isbn') == isbn:
            book.update(updated_data)
            return jsonify({"status": "Book updated", "book": book}), 200
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
