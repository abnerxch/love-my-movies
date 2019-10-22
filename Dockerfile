FROM python:3-alpine
MAINTAINER Abner Xocop Chacach <axocop@ufm.edu>
ADD /app home
ADD requirements.txt home
WORKDIR /home
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["./start.sh"]