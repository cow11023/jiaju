FROM python:3.9-slim as base
RUN mkdir /jiaju/
WORKDIR /jiaju/
COPY ./jiaju_start.sh /jiaju/jiaju_start.sh
RUN sed -i s/deb.debian.org/mirrors.163.com/g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update --fix-missing && apt-get upgrade -y
RUN apt-get install build-essential -y
RUN apt-get install default-libmysqlclient-dev -y
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple/
RUN pip3 config set install.trusted-host mirrors.aliyun.com
RUN python3 -m pip install --upgrade pip
RUN pip3 install Django==4.1.4
RUN pip3 install mysqlclient
RUN chmod +x /jiaju/jiaju_start.sh
CMD ["/jiaju/jiaju_start.sh"]
EXPOSE 9100