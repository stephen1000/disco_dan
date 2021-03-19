# BUILD: docker build -t disco_dan:latest --rm .
FROM python:3.9

ENV USER_ID 45566
ENV FFMPEG_EXECUTABLE /usr/bin/ffmpeg

RUN apt-get update -y && \
    apt-get install -y \
    postgresql \
    ffmpeg

ADD . /disco_dan

RUN pip3 install /disco_dan[postgres]
RUN mkdir /disco_dan/buffer

ENV AUDIO_BUFFER_PATH /disco_dan/buffer

WORKDIR /disco_dan
RUN chmod -R +x /disco_dan/scripts

ENTRYPOINT [ "/disco_dan/scripts/start.sh" ]
