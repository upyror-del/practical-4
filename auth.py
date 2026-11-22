"""Простий модуль авторизації (навчальний приклад для практичної №4).

Увага: SHA-256 без «солі» використано лише для демонстрації.
У реальних системах застосовують bcrypt / argon2.
"""
import hashlib
import hmac

# Навчальна «база даних» користувачів: логін -> SHA-256 хеш пароля
USERS = {
    "admin": hashlib.sha256("admin123".encode("utf-8")).hexdigest(),
}


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def login(username: str, password: str) -> bool:
    """Повертає True, якщо логін і пароль правильні."""
    stored = USERS.get(username)
    if stored is None:
        return False
    return hmac.compare_digest(stored, hash_password(password))


if __name__ == "__main__":
    print("admin / admin123 ->", login("admin", "admin123"))
    print("admin / wrong    ->", login("admin", "wrong"))
