# Исключения и ошибки

Библиотека `pycaptcha-hub` предоставляет структурированную иерархию исключений.

---

## Дерево исключений

```mermaid
classDiagram
    Exception <|-- PyCaptchaHubError
    PyCaptchaHubError <|-- CaptchaConfigurationError
    PyCaptchaHubError <|-- CaptchaError
    CaptchaError <|-- CaptchaTimeoutError
    CaptchaError <|-- CaptchaBalanceError
    CaptchaError <|-- CaptchaServiceError
    
    class PyCaptchaHubError {
        Базовое исключение библиотеки
    }
    class CaptchaConfigurationError {
        Не задан API-ключ или отсутствуют зависимости
    }
    class CaptchaError {
        Базовая ошибка процесса решения капчи
    }
    class CaptchaTimeoutError {
        Превышен лимит времени ожидания решения
    }
    class CaptchaBalanceError {
        Нулевой или недостаточный баланс аккаунта
    }
    class CaptchaServiceError {
        API сервиса вернул ошибку выполнения
    }
```

---

## Рекомендованный паттерн обработки

```python
from pycaptcha_hub import (
    RuCaptchaSolver,
    CaptchaTimeoutError,
    CaptchaBalanceError,
    CaptchaServiceError,
    CaptchaConfigurationError,
)

try:
    solver = RuCaptchaSolver()
    token = solver.solve_recaptcha(sitekey="...", page_url="...")
except CaptchaConfigurationError as e:
    print(f"Ошибка настройки: {e}")
except CaptchaBalanceError:
    print("Необходимо пополнить баланс аккаунта!")
except CaptchaTimeoutError:
    print("Капча не успела решиться за отведенный таймаут")
except CaptchaServiceError as e:
    print(f"Сервис капчи отклонил запрос: {e}")
```
