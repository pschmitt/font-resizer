FROM alpine:3

RUN apk add --no-cache py3-fontforge fontforge

COPY ./resize.py /resize.py

ENTRYPOINT ["/resize.py"]
