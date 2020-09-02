#install nginx image
FROM nginx:latest
#FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

#remove default nginx.conf
#RUN rm /etc/nginx/conf.d/default.conf

#Copy our nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
