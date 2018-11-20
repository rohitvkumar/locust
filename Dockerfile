FROM python:3.7-alpine3.8

RUN apk --no-cache add --virtual=.build-dep build-base \
        && apk --no-cache add libzmq \
        && pip install --no-cache-dir locustio \
        && apk del .build-dep

RUN mkdir /locust
WORKDIR /locust
EXPOSE 5557 5558 8089

ENTRYPOINT ["/usr/local/bin/locust"]
