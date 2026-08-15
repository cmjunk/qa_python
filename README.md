# qa_python
1. Метод add_new_book, get_books_genre; test_add_new_book_add_two_books — успешное добавление двух книг
2. Метод add_new_book; test_add_new_book_valid_name_added — книга с валидным именем добавляется с пустым жанром
3. Метод add_new_book; test_add_new_book_invalid_name_not_added — книги с пустым именем и с именем длиннее 40 символов не добавляются
4. Методы set_book_genre, get book genre; test_set_book_genre_valid_genre_is_set —  жанр устанавливается, если он есть в списке
4. Методы set_book_genre, get_book_genre; test_set_book_genre_invalid_genre_not_set — жанр не устанавливается, если его нет в списке
5. Метод get_book_genre; test_get_book_genre_returns_none_for_nonexistent_book — для книги, которой нет в коллекции, возвращается None
6. Метод get_books_with_specific_genre; test_get_books_with_specific_genre_returns_matching_books — из нескольких книг с разными жанрами возвращаются только книги запрошенного жанра
7. Метод get_books_for_children; test_get_books_for_children — книга с безопасным жанром попадает в список для детей, книга с жанром возрастного рейтинга не попадает
8. Методы add_book_in_favorites, get_list_of_favorites_books; test_add_book_in_favorites_adds_existing_book — книга из коллекции успешно добавляется в избранное
9. Метод add_book_in_favorites; test_add_book_in_favorites_does_not_add_nonexistent_book — книга, которой нет в коллекции, не добавляется в избранное 
10. Метод delete_book_from_favorites; test_delete_book_from_favorites_removes_book — книга удаляется из списка избранного 
