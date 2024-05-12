from dataclasses import dataclass
import uuid
from typing import Optional
from datetime import datetime


def format_datetime(dt_str: str):
    dt_obj = datetime.strptime(dt_str + '00', '%Y-%m-%d %H:%M:%S.%f%z')
    tz_info = dt_obj.strftime('%z')
    return f'{dt_obj.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]} {tz_info}'


@dataclass
class Filmwork:
    id: uuid.UUID
    title: str
    description: Optional[str]
    creation_date: Optional[str]
    file_path: Optional[str]
    rating: float
    type: str
    created_at: str
    updated_at: str

    def transform(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'creation_date': self.creation_date,
            'rating': self.rating,
            'type': self.type,
            'created': format_datetime(self.created_at) if self.created_at else 'NOW()',
            'modified': format_datetime(self.updated_at) if self.updated_at else None
        }


@dataclass
class Genre:
    id: uuid.UUID
    name: str
    description: Optional[str]
    created_at: str
    updated_at: str

    def transform(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created': format_datetime(self.created_at) if self.created_at else 'NOW()',
            'modified': format_datetime(self.updated_at) if self.updated_at else None
        }


@dataclass
class Person:
    id: uuid.UUID
    full_name: str
    created_at: str
    updated_at: str

    def transform(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'created': format_datetime(self.created_at) if self.created_at else 'NOW()',
            'modified': format_datetime(self.updated_at) if self.updated_at else None
        }


@dataclass
class GenreFilmwork:
    id: uuid.UUID
    genre_id: uuid.UUID
    film_work_id: uuid.UUID
    created_at: str

    def transform(self):
        return {
            'id': self.id,
            'genre_id': self.genre_id,
            'film_work_id': self.film_work_id,
            'created': format_datetime(self.created_at) if self.created_at else 'NOW()',
        }


@dataclass
class PersonFilmwork:
    id: uuid.UUID
    person_id: uuid.UUID
    film_work_id: uuid.UUID
    role: str
    created_at: str

    def transform(self):
        return {
            'id': self.id,
            'person_id': self.person_id,
            'film_work_id': self.film_work_id,
            'role': self.role,
            'created': format_datetime(self.created_at) if self.created_at else 'NOW()',
        }
