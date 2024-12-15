## Library Management API

This API provides the following features:
1. Add books (single or multiple entries).
2. Retrieve all books in the library.
3. Search for books by author, published year, or genre.
4. Delete a book using its ISBN.

## Prerequisites
- Python 3.6 or higher
- Flask
- Flask-Swagger-UI (for Swagger integration)

## Setup Instructions

### 1. Install Dependencies
1. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Ensure you have a `requirements.txt` file with the following content:
   ```
   Flask==2.0.2
   Flask-Swagger-UI==3.36.0
   ```
   Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
   The server should display:
   ```
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   * Debugger is active!
   ```

## API Endpoints

### 1. **POST /books**
   Adds single or multiple books to the library.

   **Example: Adding a single book**
   ```json
   {
     "isbn": "1234567890",
     "title": "Learn Flask",
     "author": "John Doe",
     "published_year": 2024,
     "genre": "Programming"
   }
   ```

   **Example: Adding multiple books**
   ```json
   [
     {
       "isbn": "1234567890",
       "title": "Learn Flask",
       "author": "John Doe",
       "published_year": 2024,
       "genre": "Programming"
     },
     {
       "isbn": "9876543210",
       "title": "Master Python",
       "author": "Jane Smith",
       "published_year": 2023,
       "genre": "Programming"
     }
   ]
   ```

   **Response:**
   ```json
   {
     "status": "Books successfully added"
   }
   ```

### 2. **GET /books**
   Retrieves the list of all books in the library.

### 3. **GET /books/search**
   Searches for books by author, published year, or genre. Use query parameters such as `author`, `published_year`, or `genre` to filter results.

### 4. **PUT /books/<isbn>**
   Updates the details of an existing book by its ISBN.

   **Example Request Body:**
   ```json
   {
     "title": "Learn Flask - Updated"
   }
   ```

   **Response:**
   ```json
   {
     "status": "Book updated successfully",
     "book": {
       "isbn": "1234567890",
       "title": "Learn Flask - Updated",
       "author": "John Doe",
       "published_year": 2024,
       "genre": "Programming"
     }
   }
   ```

### 5. **DELETE /books/<isbn>**
   Deletes a book from the library using its ISBN.

## Swagger Documentation
Access the API documentation via Swagger UI at:
http://127.0.0.1:5000/docs

## Troubleshooting
- Ensure the Flask server is running on `http://127.0.0.1:5000`.
- If you encounter "Could not get any response," verify the endpoint URL and ensure the Flask app is running.
- Install dependencies correctly using:
  ```bash
  pip install -r requirements.txt
  ```

