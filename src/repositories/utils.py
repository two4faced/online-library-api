from sqlalchemy import select, or_, and_, Select

from src.models import UsersORM


def get_author_ids_for_books(author: str) -> Select:
    parts = author.split()

    if len(parts) == 2:
        name, surname = parts

        query = select(UsersORM.id).where(
            and_(
                UsersORM.name.ilike(f'%{name}%'),
                UsersORM.surname.ilike(f'%{surname}%'),
            )
        )
    else:
        query = select(UsersORM.id).where(
            or_(
                UsersORM.name.ilike(f'%{author}%'),
                UsersORM.surname.ilike(f'%{author}%'),
            )
        )

    return query
