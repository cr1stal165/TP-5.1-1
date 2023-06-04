FROM python:alpine
WORKDIR /app
COPY WikiWorld/requirements.txt /app/
RUN apk add libpq-dev && \
	apk add build-base && \
    apk add pkgconf && \
    apk add cairo-dev && \
    pip install -r requirements.txt
COPY WikiWorld /app/
RUN chmod +x manage.py
