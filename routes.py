from flask import request, jsonify
from models import books, members
from utils import paginate
from auth import validate_token

def register_routes(app):
    # Home route
    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the Library Management System!"})

    # Get all books with pagination and search
    @app.route("/books", methods=["GET"])
    def get_books():
        query = request.args.get("query", "").lower()  # Search query
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))
        
        # Filter books by title or author if a query is provided
        filtered_books = [
            book for book in books
            if query in book["title"].lower() or query in book["author"].lower()
        ] if query else books

        # Paginate results
        paginated_books = paginate(filtered_books, page, limit)
        return jsonify({
            "books": paginated_books,
            "page": page,
            "limit": limit,
            "total": len(filtered_books)
        })

    # Add a new book (token-protected)
    @app.route("/books", methods=["POST"])
    @validate_token
    def add_book():
        data = request.json
        books.append(data)
        return jsonify({"message": "Book added successfully!"}), 201

    # Get all members
    @app.route("/members", methods=["GET"])
    def get_members():
        return jsonify(members)

    # Add a new member (token-protected)
    @app.route("/members", methods=["POST"])
    @validate_token
    def add_member():
        data = request.json
        members.append(data)
        return jsonify({"message": "Member added successfully!"}), 201
