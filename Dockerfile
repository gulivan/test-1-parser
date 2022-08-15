FROM ubuntu:20.04
ENV MODE dev
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install --no-install-recommends -yq \
      python3-dev \
      python3-pip \
      libpq-dev \
      gcc \
      gdal-bin \
      libgdal-dev \
      make \
      cron \
      nano \
    && rm -rf /var/lib/apt/lists/* \
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN cd app && pip3 install -r requirements.txt
COPY . .
COPY working_folder/etc/crontab /etc/crontab
RUN chmod 644 /etc/crontab
CMD sleep 30 && cd working_folder && python3 collect_weather.py  && python3 load_csv.py && cd /working_folder/app && uvicorn server:app --reload
# CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
