from models import Book
from stats import author_statistics, average_rating
from storage import add_book, delete_book, load_books


def print_menu() -> None:
    print()
    print("=== Трекер прочитанных книг ===")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")


def input_rating() -> int:
    while True:
        value = input("Оценка от 1 до 5: ").strip()

        try:
            rating = int(value)
        except ValueError:
            print("Ошибка: оценка должна быть целым числом.")
            continue

        if 1 <= rating <= 5:
            return rating

        print("Ошибка: оценка должна быть от 1 до 5.")


def input_book() -> Book:
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    rating = input_rating()
    read_date = input("Дата прочтения в формате ГГГГ-ММ-ДД: ").strip()

    return Book(author=author, title=title, rating=rating, read_date=read_date)


def show_books() -> None:
    books = load_books()

    if not books:
        print("Список книг пуст.")
        return

    print()
    print("Список прочитанных книг:")

    for number, book in enumerate(books, start=1):
        print(
            f"{number}. {book.author} — {book.title}; "
            f"оценка: {book.rating}; дата: {book.read_date}"
        )


def show_average_rating() -> None:
    books = load_books()

    if not books:
        print("Пока нет книг для расчёта средней оценки.")
        return

    result = average_rating(books)
    print(f"Средняя оценка: {result:.2f}")


def show_author_statistics() -> None:
    books = load_books()

    if not books:
        print("Пока нет книг для статистики.")
        return

    stats = author_statistics(books)

    print()
    print("Статистика по авторам:")
    for author, count in stats.items():
        print(f"{author}: {count}")


def add_book_from_input() -> None:
    try:
        book = input_book()
    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    was_added = add_book(book)

    if was_added:
        print("Книга добавлена.")
    else:
        print("Такая книга уже есть в списке.")


def delete_book_from_input() -> None:
    show_books()

    try:
        number = int(input("Введите номер книги для удаления: ").strip())
    except ValueError:
        print("Ошибка: нужно ввести номер книги.")
        return

    was_deleted = delete_book(number)

    if was_deleted:
        print("Книга удалена.")
    else:
        print("Книга с таким номером не найдена.")


def main() -> None:
    while True:
        print_menu()
        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            add_book_from_input()
        elif choice == "2":
            show_books()
        elif choice == "3":
            show_average_rating()
        elif choice == "4":
            show_author_statistics()
        elif choice == "5":
            delete_book_from_input()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Ошибка: выберите пункт от 1 до 6.")


if __name__ == "__main__":
    main()
