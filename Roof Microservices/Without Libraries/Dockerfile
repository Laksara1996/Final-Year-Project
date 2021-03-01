
FROM python:3.6-alpine

RUN addgroup -S uwsgi && adduser -S -g uwsgi uwsgi

WORKDIR /project

COPY requirements.txt /project/


RUN set -e && \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	&& \
	pip install -r requirements.txt && \
	apk del .build-deps

COPY setup.py /project/
COPY setup.cfg /project/
COPY .coveragerc /project/
COPY tox.ini /project/
COPY pytest.ini /project/
COPY README.rst /project/
COPY docker-entrypoint.sh /usr/local/bin/

COPY ci_testing_python /project/ci_testing_python
COPY tests /project/tests/


EXPOSE 5000 9090 9191

CMD ["docker-entrypoint.sh"]