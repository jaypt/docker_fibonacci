FROM python:2-onbuild

MAINTAINER jaypt

ENTRYPOINT ["python2.7", "./fib.py"]

