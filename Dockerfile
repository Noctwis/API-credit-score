FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
WORKDIR /app
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
COPY app/ /app/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]