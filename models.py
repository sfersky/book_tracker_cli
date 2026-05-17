from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    author: str
    title: str
    rating: int
    read_date: str

    def __post_init__(self) -> None:
        self.author = self.author.strip()
        self.title = self.title.strip()
        self.read_date = self.read_date.strip()

        if not self.author:
            raise ValueError("Автор не может быть пустым.")

        if not self.title:
            raise ValueError("Название не может быть пустым.")

        if not isinstance(self.rating, int):
            raise ValueError("Оценка должна быть целым числом.")

        if self.rating < 1 or self.rating > 5:
            raise ValueError("Оценка должна быть от 1 до 5.")

        try:
            datetime.strptime(self.read_date, "%Y-%m-%d")
        except ValueError as exc:
            raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД, например 2026-05-15.") from exc

    def to_dict(self) -> dict:
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "read_date": self.read_date,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(
            author=str(data.get("author", "")),
            title=str(data.get("title", "")),
            rating=int(data.get("rating", 0)),
            read_date=str(data.get("read_date", "")),
        )
