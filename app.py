from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger configuration
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Library Management API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# In-memory storage for books
books = []

# Add books (single or multiple)
@app.route('/books', methods=['POST'])
def add_books():
    data = request.get_json()
    if isinstance(data, list):
        books.extend(data)
    else:
        books.append(data)
    return jsonify({"status": "Books successfully added"}), 201

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# Search books by author, published year, or genre
@app.route('/books/search', methods=['GET'])
def search_books():
    author = request.args.get('author')
    year = request.args.get('published_year')
    genre = request.args.get('genre')
    filtered_books = books
    if author:
        filtered_books = [book for book in filtered_books if book['author'] == author]
    if year:
        filtered_books = [book for book in filtered_books if book['published_year'] == int(year)]
    if genre:
        filtered_books = [book for book in filtered_books if book['genre'] == genre]
    return jsonify(filtered_books), 200

# Update a book by ISBN
@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.get_json()
    for book in books:
        if book['isbn'] == isbn:
            book.update(data)
            return jsonify({"status": "Book updated successfully", "book": book}), 200
    return jsonify({"status": "Book not found"}), 404

# Delete a book by ISBN
@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    global books
    books = [book for book in books if book['isbn'] != isbn]
    return jsonify({"status": "Book deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
