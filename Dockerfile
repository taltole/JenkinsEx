FROM python:3.6-jessie

WORKDIR /opt
ADD / /opt
RUN pip install -r requirements.txt
ENV URLS=$URLS


ENTRYPOINT python -u /opt/url.py $URLS