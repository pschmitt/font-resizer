FROM alpine:3

RUN apk add --no-cache py3-fontforge fontforge

COPY ./font-resize.py /font-resize.py

ENTRYPOINT ["/font-resize.py"]
