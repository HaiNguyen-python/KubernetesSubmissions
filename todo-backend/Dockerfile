FROM python:3.10-alpine
# Install system dependencies for database drivers
RUN apk add --no-cache postgresql-dev gcc musl-dev
RUN pip install psycopg2-binary
WORKDIR /app
COPY main.py .
CMD ["python", "-u", "main.py"]
