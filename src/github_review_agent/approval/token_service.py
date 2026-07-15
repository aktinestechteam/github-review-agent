import secrets


class TokenService:
    """
    Generates secure approval tokens.
    """

    @staticmethod
    def generate() -> str:
        """
        Generate a cryptographically secure URL-safe token.
        """
        return secrets.token_urlsafe(32)