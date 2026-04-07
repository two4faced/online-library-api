from src.services.base import BaseService


class AdminService(BaseService):
    async def get_all_users(self, page: int, page_size: int):
        return await self.db.users.get_all(page=page, page_size=page_size)

    async def delete_user(self, user_id: int):
        await self.db.users.delete(id=user_id)
        await self.db.commit()