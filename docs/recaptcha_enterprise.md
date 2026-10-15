# reCAPTCHA Enterprise

Корпоративная версия reCAPTCHA требует поддержки дополнительных параметров (`action`, `s_token`, `enterprise_payload`, `min_score`).

Для ее решения предназначены классы `ReCaptchaEnterpriseSolver` и `AsyncReCaptchaEnterpriseSolver`.

---

## Конфигурация задачи

Модель `ReCaptchaEnterpriseConfig` описывает параметры:

| Поле | Тип | Описание |
|---|---|---|
| `site_key` | `str` | Ключ сайта reCAPTCHA Enterprise (обязательно) |
| `page_url` | `str` | URL страницы с капчей (обязательно) |
| `action` | `str \| None` | Защищаемое действие (например, `login`, `checkout`) |
| `enterprise_payload` | `dict \| None` | Дополнительный JSON-payload предприятия |
| `s_token` | `str \| None` | Дополнительный токен сессии (data-s) |
| `user_agent` | `str \| None` | User-Agent клиентского браузера |
| `proxy` | `str \| None` | Прокси-сервер |
| `min_score` | `float \| None` | Минимальный требуемый скор (0.1 - 0.9) |

---

## Пример использования

```python
import asyncio
from pycaptcha_hub import AsyncReCaptchaEnterpriseSolver, ReCaptchaEnterpriseConfig

async def solve_enterprise() -> str:
    solver = AsyncReCaptchaEnterpriseSolver(provider="capmonster")
    
    token = await solver.solve(
        site_key="6LfW_EnterpriseKeyMock123",
        page_url="https://example.com/checkout",
        action="payment",
        min_score=0.7,
    )
    return token

token = asyncio.run(solve_enterprise())
print(f"Enterprise token: {token}")
```
