from src.services.auth import AuthService

auth_service = AuthService()


def get_auth_service() -> AuthService:
    return auth_service
