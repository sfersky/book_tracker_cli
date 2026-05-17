from models import Book


def average_rating(books: list[Book]) -> float:
    if not books:
        return 0.0

    total = sum(book.rating for book in books)
    return total / len(books)


def author_statistics(books: list[Book]) -> dict[str, int]:
    stats: dict[str, int] = {}

    for book in books:
        if book.author not in stats:
            stats[book.author] = 0
        stats[book.author] += 1

    return stats
