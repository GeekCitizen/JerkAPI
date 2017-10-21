FROM library/nginx:stable
LABEL maintainer="ludovic.desfontaines@gmail.com"

RUN set -x \
  && apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y python-dev python-pip virtualenv uwsgi uwsgi-plugin-python \
  && apt-get autoremove -y --purge \
  && apt-get clean -y \
  && mkdir -p /opt/JerkAPI/app \
  && cd /opt/JerkAPI/app \
  && virtualenv JerkAPIenv

COPY code/JerkAPI.py /opt/JerkAPI/app
COPY Configurations/uwsgi/JerkAPI.ini /opt/JerkAPI/app
COPY Docker/start.sh /opt/JerkAPI
COPY Configurations/nginx/JerkAPI-site.conf /etc/nginx/conf.d/default.conf

RUN chmod 755 /opt/JerkAPI/start.sh

CMD ["/opt/JerkAPI/start.sh"]
