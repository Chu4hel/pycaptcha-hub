# Провайдеры и решатели

Библиотека `pycaptcha-hub` включает специализированные классы для основных капча-сервисов.

---

## 1. RuCaptcha / 2Captcha

Сервисы `RuCaptcha` и `2Captcha` работают по общему API.

- Синхронный класс: `RuCaptchaSolver`
- Асинхронный класс: `AsyncRuCaptchaSolver`
- Переменные окружения: `RUCAPTCHA_API_KEY`, `TWOCAPTCHA_API_KEY`
- URL сервиса по умолчанию: `https://rucaptcha.com` (можно переопределить через параметр `host="https://2captcha.com"`).

```python
from pycaptcha_hub import RuCaptchaSolver

solver = RuCaptchaSolver(host="https://2captcha.com")
token = solver.solve_recaptcha(sitekey="...", page_url="...")
```

---

## 2. Anti-Captcha

- Синхронный класс: `AntiCaptchaSolver`
- Асинхронный класс: `AsyncAntiCaptchaSolver`
- Переменные окружения: `ANTICAPTCHA_API_KEY`
- URL сервиса по умолчанию: `https://api.anti-captcha.com`

```python
from pycaptcha_hub import AntiCaptchaSolver

solver = AntiCaptchaSolver()
token = solver.solve_recaptcha(sitekey="...", page_url="...")
```

---

## 3. CapMonster Cloud

- Синхронный класс: `CapMonsterSolver`
- Асинхронный класс: `AsyncCapMonsterSolver`
- Переменные окружения: `CAPMONSTER_API_KEY`
- URL сервиса по умолчанию: `https://api.capmonster.cloud`

```python
from pycaptcha_hub import CapMonsterSolver

solver = CapMonsterSolver()
token = solver.solve_recaptcha(sitekey="...", page_url="...")
```
