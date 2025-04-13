FROM python:3.9-slim
WORKDIR /api
# SETUP CHROME FOR SELENIUM
RUN apt-get update && apt-get install -y chromium chromium-driver
# INSTALL FLASK DEPENDENCIES
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /api

# RUN FLASK
ARG FLASK_PORT
ENV FLASK_PORT=$FLASK_PORT
EXPOSE $FLASK_PORT
CMD ["flask", "run", "--host=0.0.0.0", "$FLASK_PORT"]
