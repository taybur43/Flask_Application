FROM centos:latest
MAINTAINER Taybur Rahaman "taybur.rahaman@bjitgroup.com"
RUN yum update -y
RUN yum install install -y python-pip python-dev build-essential
ADD . /FlaskApp
WORKDIR /FlaskApp
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["routes.py"]
