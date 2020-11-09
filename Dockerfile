FROM continuumio/anaconda3
LABEL maintainer="Aaron Hong <cuong.hong.phu@hotmail.com>" \
    description="Docker image for League of legends webscraper. This container contains\
    web app that can be accessed using a REST API (created in Flask).."
WORKDIR /home/ec2-user/app
COPY . /home/ec2-user/app
RUN pip install -r requirements.txt 
EXPOSE 5000
CMD ["python", "app.py", "--ip='0.0.0.0'"]