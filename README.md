# pycaptcha-hub

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Унифицированная библиотека для решения капч с поддержкой популярных сервисов (RuCaptcha, 2Captcha, Anti-Captcha, CapMonster), а также сложных типов капч (GeeTest v4, reCAPTCHA Enterprise). Поддерживает синхронный и асинхронный (`asyncio`) режимы работы.

---

## Возможности

- **Единый абстрактный интерфейс** для различных провайдеров.
- **Поддержка синхронного и асинхронного режимов** для всех решателей.
- **Интеграция с провайдерами:**
  - **RuCaptcha / 2Captcha**
  - **Anti-Captcha**
  - **CapMonster Cloud**
- **Поддержка современных типов капч:**
  - **ImageToText**: распознавание текста по изображению.
  - **reCAPTCHA v2 / v3**.
  - **GeeTest v4 / v3** (`GeeTestSolver`, `AsyncGeeTestSolver`).
  - **reCAPTCHA Enterprise** (`ReCaptchaEnterpriseSolver`, `AsyncReCaptchaEnterpriseSolver`).
- **Строгая типизация** (Pydantic-модели валидации задач и результатов, `py.typed`).
- **Гибкая конфигурация API-ключей**: передача в конструктор, чтение из переменных окружения или опциональная интеграция с `chutils.secret_manager`.

---

## Установка

```bash
pip install pycaptcha-hub
```

Или с использованием `uv`:

```bash
uv add pycaptcha-hub
```

Требуется **Python >= 3.11**.

---

## Быстрый старт

### Решение текстовой капчи по изображению

```python
from pycaptcha_hub import RuCaptchaSolver, CaptchaError

try:
    # Ключ автоматически берется из переменной окружения RUCAPTCHA_API_KEY
    solver = RuCaptchaSolver()

    with open("captcha.png", "rb") as f:
        text = solver.solve_image(f.read(), timeout=60.0, poll_interval=3.0)
    print(f"Текст капчи: {text}")
except CaptchaError as e:
    print(f"Ошибка решения капчи: {e}")
```

### Асинхронное решение reCAPTCHA v2

```python
import asyncio
from pycaptcha_hub import AsyncAntiCaptchaSolver

async def main() -> None:
    # Ключ автоматически считывается из переменной ANTICAPTCHA_API_KEY
    solver = AsyncAntiCaptchaSolver()

    token = await solver.solve_recaptcha(
        sitekey="6LeOeSkUAAAAACl2pxhXLD37t3h7wJz16F8ySU73",
        page_url="https://example.com/login",
    )
    print(f"Токен reCAPTCHA: {token}")

asyncio.run(main())
```

### Решение GeeTest v4

```python
from pycaptcha_hub import GeeTestSolver

solver = GeeTestSolver(provider="rucaptcha")
result = solver.solve(
    captcha_id="your_geetest_captcha_id",
    page_url="https://example.com/login",
    risk_type="slide",
)

# Результат содержит lot_number, pass_token, gen_time, captcha_output
print(result.to_validation_payload())
```

### Решение reCAPTCHA Enterprise

```python
from pycaptcha_hub import ReCaptchaEnterpriseSolver

solver = ReCaptchaEnterpriseSolver(provider="capmonster")
token = solver.solve(
    site_key="6Lf_enterprise_site_key",
    page_url="https://example.com/checkout",
    action="checkout",
)
print(f"Токен: {token}")
```

---

## Переменные окружения для API-ключей

Если ключ не передан явно в конструктор, солвер автоматически проверяет соответствующие переменные окружения:

| Солвер | Переменные окружения |
|---|---|
| `RuCaptchaSolver` / `AsyncRuCaptchaSolver` | `RUCAPTCHA_API_KEY`, `TWOCAPTCHA_API_KEY` |
| `AntiCaptchaSolver` / `AsyncAntiCaptchaSolver` | `ANTICAPTCHA_API_KEY` |
| `CapMonsterSolver` / `AsyncCapMonsterSolver` | `CAPMONSTER_API_KEY` |
| `GeeTestSolver` / `ReCaptchaEnterpriseSolver` | В зависимости от провайдера (`RUCAPTCHA_API_KEY`, `TWOCAPTCHA_API_KEY`, `CAPMONSTER_API_KEY`) |

---

## Иерархия исключений

```text
PyCaptchaHubError
└── CaptchaConfigurationError
└── CaptchaError
    ├── CaptchaTimeoutError
    ├── CaptchaBalanceError
    └── CaptchaServiceError
```

---

## Лицензия

MIT License.
