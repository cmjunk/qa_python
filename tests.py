import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_add_new_book_valid_name_added(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_books_genre() == {'Гарри Поттер': ''}

    @pytest.mark.parametrize('name', ['','a' * 41])
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_set_book_genre_valid_genre_is_set(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')

        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')

        collector.set_book_genre('Оно', 'Мелодрама')

        assert collector.get_book_genre('Оно') == ''  

    def test_get_book_genre_returns_none_for_nonexistent_book(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Нет такой книги') is None

    def test_get_books_with_specific_genre_returns_matching_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Ужасы')
        collector.set_book_genre('Книга 2', 'Комедии')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Книга 1']

    @pytest.mark.parametrize('genre, expected_books', [('Комедии', ['Книга']), ('Ужасы', [])])
    def test_get_books_for_children(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)

        assert collector.get_books_for_children() == expected_books

    def test_add_book_in_favorites_adds_existing_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')

        collector.add_book_in_favorites('Книга')

        assert collector.get_list_of_favorites_books() == ['Книга']

    def test_add_book_in_favorites_does_not_add_nonexistent_book(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Нет такой книги')

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')

        collector.delete_book_from_favorites('Книга')

        assert collector.get_list_of_favorites_books() == []

