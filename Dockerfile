FROM alpine:3

RUN apk add --no-cache py3-fontforge fontforge

COPY ./font_resizer.py /font-resizer.py

ENTRYPOINT ["/font-resizer.py"]

VOLUME ["/fonts"]
WORKDIR /fonts
