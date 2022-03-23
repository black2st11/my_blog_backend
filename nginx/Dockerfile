FROM nginx:latest

COPY ./default.conf /etc/nginx/conf.d/default.conf

COPY wait-for-it.sh /wait-for-it.sh

COPY docker-entrypoint.production.sh /docker-entrypoint.production.sh
RUN chmod +x /docker-entrypoint.production.sh