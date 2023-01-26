FROM mcr.microsoft.com/devcontainers/python:0-3.11

RUN apt-get update || true
RUN apt-get install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev \
    libsdl2-ttf-dev libfreetype6-dev libportmidi-dev libjpeg-dev \
    ffmpeg
# Necessary for running the sb3 example
RUN pip install torch stable_baselines3 tensorboard