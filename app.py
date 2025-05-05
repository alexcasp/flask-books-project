from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Book, Genre

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    books = Book.query.order_by(Book.created_at.desc()).limit(15).all()
    return render_template('index.html', books=books)

@app.route('/genre/<int:genre_id>')
def genre_page(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template('genre.html', genre=genre, books=genre.books)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
