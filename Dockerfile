FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
WORKDIR /app
COPY requirements.txt /tmp/
RUN apt-get install libgomp1
RUN pip install --upgrade pip; \
	pip install -r /tmp/requirements.txt
COPY app/ /app/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]