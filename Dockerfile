FROM python:3.12-alpine
WORKDIR /app
COPY scholar_loop.py .
CMD ["python","scholar_loop.py"]
