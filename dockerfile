FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

# Копируем только нужные файлы
COPY --from=builder /root/.local /root/.local
COPY . .

# Убедимся, что скрипты в PATH
ENV PATH=/root/.local/bin:$PATH

# Установка в режиме разработки (если нужно)
RUN pip install --no-cache-dir -e .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]