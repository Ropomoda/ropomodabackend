FROM python:3.8.2-slim-buster

COPY . /app
WORKDIR /app
RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install --default-timeout=100 pip --upgrade && \
    /opt/venv/bin/pip install --default-timeout=100 -r requirements.txt && \
    chmod +x entrypoint.sh


CMD ["/app/entrypoint.sh"]