FROM ubuntu
COPY ./requirements.txt /requirements.txt
RUN apt-get update
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw
RUN apt install -y libmagickwand-dev ghostscript python3.8 python3-pip python3.8-dev
RUN pip3 install -r /requirements.txt
COPY ./app /app
RUN mkdir ./app/tmp
RUN sed -i '/disable ghostscript format types/,+6d' /etc/ImageMagick-6/policy.xml
WORKDIR /app
CMD python3 main.py