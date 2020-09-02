#install nginx image
from nginx:alpine
#remove default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
#Copy our nginx.conf
COPY nginx.conf /etc/nginx/conf.d/