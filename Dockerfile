FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    openjdk-21-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

WORKDIR /app

RUN pip install --no-cache-dir pyspark==3.5.0

COPY titanic.csv .

CMD ["python", "saprk_titanic.py"]