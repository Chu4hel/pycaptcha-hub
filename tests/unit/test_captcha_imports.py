from __future__ import annotations

from unittest.mock import patch

import pytest

from pycaptcha_hub.exceptions import CaptchaConfigurationError


def test_captcha_imports_without_httpx() -> None:
    """Проверяет, что базовый модуль импортируется корректно без httpx."""
    with patch("importlib.util.find_spec", return_value=None):
        import pycaptcha_hub

        assert pycaptcha_hub is not None


def test_captcha_solver_raises_dependency_error_when_missing_httpx() -> None:
    """Проверяет выброс CaptchaConfigurationError при инициализации клиента без httpx."""
    with patch("importlib.util.find_spec", return_value=None):
        import pycaptcha_hub

        with pytest.raises(CaptchaConfigurationError) as exc_info:
            pycaptcha_hub.RuCaptchaSolver(api_key="test")

        assert "httpx" in str(exc_info.value)
