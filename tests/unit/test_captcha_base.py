from __future__ import annotations

from unittest.mock import patch

import pytest

from pycaptcha_hub.base import BaseAsyncCaptchaSolver, BaseCaptchaSolver
from pycaptcha_hub.exceptions import CaptchaConfigurationError


class DummySolver(BaseCaptchaSolver):
    secret_key_name = "DUMMY_API_KEY"


class DummyAsyncSolver(BaseAsyncCaptchaSolver):
    secret_key_name = "DUMMY_API_KEY"


def test_solver_uses_explicit_api_key() -> None:
    """Проверяет, что если API-ключ передан явно, он используется."""
    solver = DummySolver(api_key="explicit_key_123")
    assert solver.api_key == "explicit_key_123"

    async_solver = DummyAsyncSolver(api_key="explicit_key_456")
    assert async_solver.api_key == "explicit_key_456"


def test_solver_retrieves_key_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Проверяет получение API-ключа из переменных окружения."""
    monkeypatch.setenv("DUMMY_API_KEY", "env_secret_key_123")
    solver = DummySolver()
    assert solver.api_key == "env_secret_key_123"

    async_solver = DummyAsyncSolver()
    assert async_solver.api_key == "env_secret_key_123"


def test_solver_retrieves_key_from_secret_manager(monkeypatch: pytest.MonkeyPatch) -> None:
    """Проверяет получение API-ключа из SecretManager (если доступен), если не задан в окружении."""
    monkeypatch.delenv("DUMMY_API_KEY", raising=False)
    with patch("pycaptcha_hub.base.resolve_secret", return_value="manager_key_777"):
        solver = DummySolver()
        assert solver.api_key == "manager_key_777"


def test_solver_raises_configuration_error_when_key_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Проверяет, что при отсутствии ключа выбрасывается CaptchaConfigurationError."""
    monkeypatch.delenv("DUMMY_API_KEY", raising=False)
    with patch("pycaptcha_hub.base.resolve_secret", return_value=None):
        with pytest.raises(CaptchaConfigurationError) as exc_info:
            DummySolver()
        assert "API-ключ для DummySolver не задан" in str(exc_info.value)
