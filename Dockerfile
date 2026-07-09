FROM python:3.11-slim
RUN apt-get update && apt-get install -y git curl ffmpeg && rm -rf /var/lib/apt/lists/*
RUN pip3 install -U pip
RUN python3 -m pip install --upgrade pip
COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD ["bash","start.sh"]
