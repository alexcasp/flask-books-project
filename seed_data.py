from app import app, db
from models import Genre, Book

with app.app_context():
    # Очистим старые данные (по желанию)
    db.drop_all()
    db.create_all()

    # Добавим жанры
    fiction = Genre(name='Художественная литература')
    nonfiction = Genre(name='Документальная литература')
    fantasy = Genre(name='Фэнтези')

    db.session.add_all([fiction, nonfiction, fantasy])
    db.session.commit()

    # Добавим книги
    books = [
        Book(title='Три товарища', genre_id=fiction.id),
        Book(title='1984', genre_id=fiction.id),
        Book(title='Фактологичность', genre_id=nonfiction.id),
        Book(title='Властелин колец', genre_id=fantasy.id),
        Book(title='Хоббит', genre_id=fantasy.id),
        Book(title='Чистый код', genre_id=nonfiction.id),
        Book(title='Преступление и наказание', genre_id=fiction.id),
        Book(title='Атлант расправил плечи', genre_id=fiction.id),
        Book(title='Сапиенс', genre_id=nonfiction.id),
        Book(title='Дюна', genre_id=fantasy.id),
        Book(title='О дивный новый мир', genre_id=fiction.id),
        Book(title='Пикник на обочине', genre_id=fantasy.id),
        Book(title='Мастер и Маргарита', genre_id=fiction.id),
        Book(title='Война и мир', genre_id=fiction.id),
        Book(title='Над пропастью во ржи', genre_id=fiction.id),
        Book(title='Звездные дневники Ийона Тихого', genre_id=fantasy.id)
    ]

    db.session.add_all(books)
    db.session.commit()

    # print("Данные успешно добавлены.")
