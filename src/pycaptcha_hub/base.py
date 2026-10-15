"""Базовые классы и утилиты для капча-солверов."""

from __future__ import annotations

import importlib.util
import os

from .exceptions import CaptchaConfigurationError


def resolve_secret(key_name: str) -> str | None:
    """Получает значение секрета из окружения или SecretManager (если установлен chutils).

    Args:
        key_name: Имя переменной или ключа секрета.

    Returns:
        Значение ключа или None, если ключ не найден.
    """
    if not key_name:
        return None

    # Сначала проверяем переменные окружения
    val = os.environ.get(key_name)
    if val:
        return val

    # Опциональная интеграция с chutils.secret_manager, если установлен
    try:
        from chutils.secret_manager import SecretManager

        sm = SecretManager("")
        res = sm.get_secret(key_name)
        return str(res) if res is not None else None
    except Exception:
        return None


def _ensure_httpx() -> None:
    """Проверяет наличие установленной библиотеки httpx."""
    if importlib.util.find_spec("httpx") is None:
        raise CaptchaConfigurationError(
            "Библиотека 'httpx' не установлена. Для работы pycaptcha-hub "
            "установите ее: pip install httpx"
        )


class BaseCaptchaSolver:
    """Базовый синхронный клиент для сервисов решения капч."""

    secret_key_name: str = ""

    def __init__(self, api_key: str | None = None) -> None:
        """Инициализирует BaseCaptchaSolver.

        Args:
            api_key: Явно переданный API-ключ. Если не передан, запрашивается из окружения.

        Raises:
            CaptchaConfigurationError: Если API-ключ не задан.
        """
        _ensure_httpx()
        self.api_key = api_key or self._get_secret_key()
        if not self.api_key:
            raise CaptchaConfigurationError(
                f"API-ключ для {self.__class__.__name__} не задан. "
                f"Передайте его явно или установите переменную окружения {self.secret_key_name}."
            )

    def _get_secret_key(self) -> str | None:
        """Получает API-ключ из окружения или хранилища секретов."""
        return resolve_secret(self.secret_key_name)


class BaseAsyncCaptchaSolver:
    """Базовый асинхронный клиент для сервисов решения капч."""

    secret_key_name: str = ""

    def __init__(self, api_key: str | None = None) -> None:
        """Инициализирует BaseAsyncCaptchaSolver.

        Args:
            api_key: Явно переданный API-ключ. Если не передан, запрашивается из окружения.

        Raises:
            CaptchaConfigurationError: Если API-ключ не задан.
        """
        _ensure_httpx()
        self.api_key = api_key or self._get_secret_key()
        if not self.api_key:
            raise CaptchaConfigurationError(
                f"API-ключ для {self.__class__.__name__} не задан. "
                f"Передайте его явно или установите переменную окружения {self.secret_key_name}."
            )

    def _get_secret_key(self) -> str | None:
        """Получает API-ключ из окружения или хранилища секретов."""
        return resolve_secret(self.secret_key_name)


__all__ = [
    "BaseAsyncCaptchaSolver",
    "BaseCaptchaSolver",
    "resolve_secret",
]
