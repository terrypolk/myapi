FROM python:3.8
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN groupadd -g 999 appuser && useradd -d /home/appuser -m -u 999 -g appuser appuser
USER appuser
WORKDIR /home/appuser/api
COPY --chown=appuser:appuser . .
CMD ["gunicorn", "--access-logfile", "-", "--timeout", "180", "--threads", "8", "--bind", "0.0.0.0:5555", "api.main:create_app()"]
