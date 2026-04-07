from fastapi import Depends

from src.dependencies.dependencies import get_current_user
from src.exceptions import NotEnoughPermissionsHTTPException
from src.models.users import UserRole
from src.schemas.users import UserDTO


class RoleChecker:
    def __init__(self, allowed_roles: list[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: UserDTO = Depends(get_current_user)):
        if user.role not in self.allowed_roles:
            raise NotEnoughPermissionsHTTPException
        return True


require_author_or_admin = Depends(RoleChecker([UserRole.AUTHOR, UserRole.ADMIN]))
require_admin = Depends(RoleChecker([UserRole.ADMIN]))
