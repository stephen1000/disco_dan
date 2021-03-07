# BUILD: docker build -t disco-dan:latest --rm .
FROM python:3.9

VOLUME /disco_dan
ENV USER_ID 45566
ENV FFMPEG_EXECUTABLE /usr/bin/ffmpeg

RUN apt-get update -y
RUN apt-get install -y \
    postgresql \
    ffmpeg

ADD --chown=${USER_ID}:${USER_ID} . /disco_dan

RUN pip3 install /disco_dan
RUN mkdir /disco_dan/buffer

ENV AUDIO_BUFFER_PATH /disco_dan/buffer
ENV DISCORD_TOKEN ${DISCORD_TOKEN}
ENV DISCORD_GUILD ${DISCORD_GUILD}

VOLUME [ "/sqlite" ]

WORKDIR /disco_dan
RUN chmod -R +x /disco_dan/scripts

ENTRYPOINT [ "/disco_dan/scripts/start.sh" ]
