#Install python
From python:alpine
#Working directory
WORKDIR /app
#Copy contents
COPY ./ ./app
#install dependecies
RUN pip install - r requirements.txt
#Startup command
CMD ["uwsgi","app.ini"]