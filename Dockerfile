FROM 119.3.170.97:5000/ubuntu:latest
MAINTAINER disen 610039018@qq.com
WORKDIR /usr/src
ADD . /usr/src/yuetu-api
VOLUME /usr/src/yuetu-api
WORKDIR /usr/src/yuetu-api
RUN pip install gunicorn -i https://mirros.aliyun.com/pypi/simple
RUN pip install -r requirements.txt -i https://mirros.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /usr/src/yuetu-api/run.sh


RUN git clone https://github.com/yuetu-zhibo/Yuetu_Project.git

VOLUME /usr/src/elm/elm/static
RUN pip install -r venv.txt -i http://mirros.aliyun.com/pypi/simple
RUN pip install gunicorn -i http://mirros.aliyun.com/pypi/simple

