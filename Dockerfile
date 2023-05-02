FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client build-base postgresql-dev \
                                musl-dev zlib zlib-dev linux-headers

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt

ENV PATH="/scripts:/py/bin:$PATH"

COPY ./app /app
RUN chmod -R +x /app

WORKDIR /app
EXPOSE 80

CMD ["/run_start.sh"]
