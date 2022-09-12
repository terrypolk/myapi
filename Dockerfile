FROM python:3.8
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--access-logfile", "-", "--timeout", "180", "--threads", "8", "--bind", "0.0.0.0:5555", "api.main:create_app()"]
