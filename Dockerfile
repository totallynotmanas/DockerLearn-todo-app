FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt* ./

RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi
COPY . .

RUN addgroup -S app && adduser -S -G app app
RUN chown -R app:app /app
USER app

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

CMD ["python", "app.py"]