#Install python
From python:3.7-alpine
#FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

#Working directory
WORKDIR /flask

#copy project files
#COPY ./ ./app


# Expose the port uWSGI will listen on
#EXPOSE 8000

#Copy requirements
COPY ./requirements.txt ./

#install dependecies
#RUN pip install -r requirements.txt

#Install all Dependencies for WSGI
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip --no-cache-dir install -r requirements.txt; \
	apk del .build-deps;

#copy other content
COPY ./ ./


#Startup command
CMD ["uwsgi","app.ini"]
#CMD ["python", "run.py"]
