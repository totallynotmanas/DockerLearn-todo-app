FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN addgroup --system app && adduser --system --ingroup app app
RUN chown -R app:app /app
USER app

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

CMD ["python", "app.py"]