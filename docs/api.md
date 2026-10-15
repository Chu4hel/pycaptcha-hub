# Справочник API

В этом разделе приведены основные классы и функции библиотеки `pycaptcha-hub`.

---

## Провайдеры

### `RuCaptchaSolver` / `AsyncRuCaptchaSolver`

```python
class RuCaptchaSolver(BaseCaptchaSolver):
    def __init__(self, api_key: str | None = None, host: str = "https://rucaptcha.com") -> None: ...
    def solve_image(self, image_data: bytes | str, timeout: float = 60.0, poll_interval: float = 5.0, **kwargs: Any) -> str: ...
    def solve_recaptcha(self, sitekey: str, page_url: str, timeout: float = 120.0, poll_interval: float = 5.0, **kwargs: Any) -> str: ...
```

### `AntiCaptchaSolver` / `AsyncAntiCaptchaSolver`

```python
class AntiCaptchaSolver(BaseCaptchaSolver):
    def __init__(self, api_key: str | None = None, host: str = "https://api.anti-captcha.com") -> None: ...
    def solve_image(self, image_data: bytes | str, timeout: float = 60.0, poll_interval: float = 5.0, **kwargs: Any) -> str: ...
    def solve_recaptcha(self, sitekey: str, page_url: str, timeout: float = 120.0, poll_interval: float = 5.0, **kwargs: Any) -> str: ...
```

### `CapMonsterSolver` / `AsyncCapMonsterSolver`

```python
class CapMonsterSolver(BaseCaptchaSolver):
    def __init__(self, api_key: str | None = None, host: str = "https://api.capmonster.cloud") -> None: ...
    def solve_image(self, image_data: bytes | str, timeout: float = 60.0, poll_interval: float = 5.0, **kwargs: Any) -> str: ...
    def solve_recaptcha(self, sitekey: str, page_url: str, timeout: float = 120.0, poll_interval: float = 5.0, **kwargs: Any) -> str: ...
```

---

## Продвинутые решатели

### `GeeTestSolver` / `AsyncGeeTestSolver`

```python
class GeeTestSolver(BaseCaptchaSolver):
    def __init__(self, api_key: str | None = None, provider: str = "rucaptcha", host: str | None = None) -> None: ...
    def solve(self, config: GeeTestTaskConfig | None = None, *, captcha_id: str | None = None, page_url: str | None = None, challenge: str | None = None, risk_type: str | None = None, api_server: str | None = None, user_agent: str | None = None, proxy: str | None = None, timeout: float = 60.0, poll_interval: float = 3.0) -> GeeTestResult: ...
```

### `ReCaptchaEnterpriseSolver` / `AsyncReCaptchaEnterpriseSolver`

```python
class ReCaptchaEnterpriseSolver(BaseCaptchaSolver):
    def __init__(self, api_key: str | None = None, provider: str = "rucaptcha", host: str | None = None) -> None: ...
    def solve(self, config: ReCaptchaEnterpriseConfig | None = None, *, site_key: str | None = None, page_url: str | None = None, action: str | None = None, enterprise_payload: dict[str, Any] | None = None, s_token: str | None = None, user_agent: str | None = None, proxy: str | None = None, min_score: float | None = None, timeout: float = 60.0, poll_interval: float = 3.0) -> str: ...
```

---

## Модели данных

### `GeeTestTaskConfig`
Модель конфигурации решения GeeTest v4 / v3.

### `GeeTestResult`
Модель результата GeeTest. Метод `to_validation_payload() -> dict[str, Any]` формирует словарь для верификации.

### `ReCaptchaEnterpriseConfig`
Модель конфигурации задачи reCAPTCHA Enterprise.

---

## Утилиты

### `resolve_secret(key_name: str) -> str | None`
Разрешает секрет, проверяя в первую очередь `os.environ[key_name]`, а затем опционально запрашивая `chutils.secret_manager.SecretManager` при его наличии в окружении.
