#  How to run the project

- Install `Python` and `Flask`
```cmd
pip install flask
```

- Run the app
```cmd
python app.py
```

# The design choices made
- Home
```
http://127.0.0.1:5000
```
- For accessing Books
```url
http://127.0.0.1:5000/books
```
- For Members
```url
http://127.0.0.1:5000/members
```
- To Search a book
```url
http://127.0.0.1:5000/books?query=george
```
- Pagination
```url
http://127.0.0.1:5000//books?page=2&limit=5
```

# Limitations
- Lack of Database Integration.
- No Concurrency Handling
- Static Token-Based Authentication
- Pagination Inefficiency