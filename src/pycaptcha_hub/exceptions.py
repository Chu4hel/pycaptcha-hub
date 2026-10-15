"""Исключения библиотеки pycaptcha-hub."""

from __future__ import annotations


class PyCaptchaHubError(Exception):
    """Базовое исключение библиотеки pycaptcha-hub."""


class CaptchaError(PyCaptchaHubError):
    """Базовая ошибка при решении капчи."""


class CaptchaConfigurationError(PyCaptchaHubError):
    """Ошибка конфигурации или отсутствия необходимых параметров/зависимостей."""


class CaptchaTimeoutError(CaptchaError):
    """Ошибка: превышено время ожидания решения капчи."""


class CaptchaBalanceError(CaptchaError):
    """Ошибка: недостаточный баланс на аккаунте сервиса капчи."""


class CaptchaServiceError(CaptchaError):
    """Ошибка: сервис решения капчи вернул ошибку API (неверный ключ, плохие параметры)."""


__all__ = [
    "CaptchaBalanceError",
    "CaptchaConfigurationError",
    "CaptchaError",
    "CaptchaServiceError",
    "CaptchaTimeoutError",
    "PyCaptchaHubError",
]
