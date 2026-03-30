from pydantic import BaseModel
from sqlalchemy import select, insert, delete, update
from sqlalchemy.exc import NoResultFound

from src.exceptions import ObjectNotFound


class BaseRepository:
    model = None
    schema: BaseModel = None

    def __init__(self, session):
        self.session = session

    async def get_all(self, *filters, **filter_by):
        query = select(self.model).filter(*filters).filter_by(**filter_by)
        result = await self.session.execute(query)
        return [
            self.schema.model_validate(model, from_attributes=True)
            for model in result.scalars().all()
        ]

    async def get_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()

        if not model:
            return None

        return self.schema.model_validate(model, from_attributes=True)

    async def get_one(self, **filter_by):
        try:
            query = select(self.model).filter_by(**filter_by)
            result = await self.session.execute(query)
            model = result.scalars().one()
        except NoResultFound:
            raise ObjectNotFound

        return self.schema.model_validate(model, from_attributes=True)

    async def add(self, data: BaseModel):
        add_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(add_stmt)
        model = result.scalars().one()

        return self.schema.model_validate(model, from_attributes=True)

    async def add_bulk(self, data: list[BaseModel]):
        add_stmt = insert(self.model).values([item.model_dump() for item in data])
        await self.session.execute(add_stmt)

    async def delete(self, **filter_by):
        del_stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(del_stmt)

    async def change(self, data: BaseModel, exclude_unset: bool = False, **filter_by):
        update_stmt = (
            update(self.model)
            .filter_by(**filter_by)
            .values(data.model_dump(exclude_unset=exclude_unset))
        )
        await self.session.execute(update_stmt)
