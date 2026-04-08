from src.schemas.users import AdminPatchUserDTO
from src.services.base import BaseService


class AdminService(BaseService):
    async def get_all_users(self, page: int, page_size: int):
        return await self.db.users.get_all(page=page, page_size=page_size)

    async def change_user(self, user_data: AdminPatchUserDTO, user_id: int):
        await self.db.users.change(user_data, exclude_unset=True, id=user_id)
        await self.db.commit()

    async def delete_user(self, user_id: int):
        await self.db.users.delete(id=user_id)
        await self.db.commit()

    async def delete_review(self, review_id: int):
        await self.db.reviews.delete(id=review_id)
        await self.db.commit()

    async def delete_book(self, book_id: int):
        await self.db.books.delete(id=book_id)
        await self.db.commit()
