# Быстрый старт

## Установка

Библиотека требует Python **3.11** или новее.

Установка через `pip`:

```bash
pip install pycaptcha-hub
```

Установка через `uv`:

```bash
uv add pycaptcha-hub
```

---

## Настройка ключей доступа

Вы можете передавать API-ключ непосредственно в конструктор решателя:

```python
from pycaptcha_hub import RuCaptchaSolver

solver = RuCaptchaSolver(api_key="your_api_key_here")
```

Или задать соответствующие переменные окружения, после чего создавать клиенты без аргументов:

```bash
export RUCAPTCHA_API_KEY="your_rucaptcha_key"
export ANTICAPTCHA_API_KEY="your_anticaptcha_key"
export CAPMONSTER_API_KEY="your_capmonster_key"
```

```python
solver = RuCaptchaSolver()  # Автоматически подхватит RUCAPTCHA_API_KEY
```

---

## Примеры использования

### Решение графической капчи (ImageToText)

```python
from pycaptcha_hub import RuCaptchaSolver, CaptchaError

solver = RuCaptchaSolver()

try:
    with open("captcha_image.png", "rb") as image_file:
        solution_text = solver.solve_image(
            image_file.read(),
            timeout=60.0,
            poll_interval=2.0,
        )
    print(f"Решение капчи: {solution_text}")
except CaptchaError as exc:
    print(f"Не удалось решить капчу: {exc}")
```

### Асинхронное решение reCAPTCHA v2

```python
import asyncio
from pycaptcha_hub import AsyncAntiCaptchaSolver

async def solve_token() -> str:
    solver = AsyncAntiCaptchaSolver()
    token = await solver.solve_recaptcha(
        sitekey="6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
        page_url="https://www.google.com/recaptcha/api2/demo",
        timeout=120.0,
    )
    return token

token = asyncio.run(solve_token())
print(f"g-recaptcha-response: {token}")
```
