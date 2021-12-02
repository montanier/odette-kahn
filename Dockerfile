FROM ubuntu:focal
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN apt-get install -y python3 python3-pip
RUN pip install ipython pandas
RUN mkdir /db
