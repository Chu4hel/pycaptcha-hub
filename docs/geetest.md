# GeeTest v4 / v3

Классы `GeeTestSolver` и `AsyncGeeTestSolver` поддерживают решение интерактивных капч GeeTest через различные провайдеры (`rucaptcha`, `2captcha`, `capmonster`).

---

## Конфигурация задачи

Для настройки задачи используется Pydantic-модель `GeeTestTaskConfig`:

| Поле | Тип | Описание |
|---|---|---|
| `captcha_id` | `str` | Идентификатор GeeTest v4 (обязательно) |
| `page_url` | `str` | URL целевой страницы (обязательно) |
| `challenge` | `str \| None` | Challenge для GeeTest v3 |
| `risk_type` | `str \| None` | Тип проверки (`slide`, `ai` и т.д.) |
| `api_server` | `str \| None` | Пользовательский сервер GeeTest |
| `user_agent` | `str \| None` | User-Agent браузера |
| `proxy` | `str \| None` | Прокси в формате `http://user:pass@host:port` |

---

## Пример решения

```python
from pycaptcha_hub import GeeTestSolver, GeeTestTaskConfig

solver = GeeTestSolver(provider="rucaptcha")

# Способ 1: через именованные аргументы
result = solver.solve(
    captcha_id="e392e1d7fd421dc6332e927ffab35f73",
    page_url="https://example.com/login",
    risk_type="slide",
)

# Способ 2: через объект конфигурации
config = GeeTestTaskConfig(
    captcha_id="e392e1d7fd421dc6332e927ffab35f73",
    page_url="https://example.com/login",
)
result = solver.solve(config)

print(result.lot_number)
print(result.pass_token)
print(result.gen_time)
print(result.captcha_output)

# Получение словаря для валидации на бэкенде:
payload = result.to_validation_payload()
```
