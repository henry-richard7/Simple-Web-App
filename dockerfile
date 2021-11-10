FROM python:3.7
WORKDIR /Simple-Web-App
COPY . .
RUN apt-get -y update
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python","./TMDB app.py" ]
