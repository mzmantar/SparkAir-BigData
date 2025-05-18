FROM bitnami/spark:3.3.2

USER root

# Installer Python et les packages nécessaires
RUN apt-get update && apt-get install -y python3-pip && \
    pip3 install --no-cache-dir pandas scikit-learn joblib py4j

USER 1001
WORKDIR /app
COPY App /app
