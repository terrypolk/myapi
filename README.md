# myapi

Running with gunicorn:

```sh
gunicorn --access-logfile - --timeout 180 --threads 8 --bind 0.0.0.0:5555 "api.main:create_app()"
```

Example .env:

```sh
APP_URL = http://localhost:5555
DEBUG = true
```

Simple docker-compose.yml:

```yaml
version: '3'

services:
  api:
    build: ./myapi
    ports:
      - "5555:5555"

```
