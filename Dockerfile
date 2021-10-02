FROM python:latest

RUN mkdir /automation

COPY ./apitest /automation/apitest
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install