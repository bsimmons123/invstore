# build
FROM node:15.7.0-alpine3.10 as build-vue
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./client/package*.json ./
RUN npm install
COPY ./client .
RUN npm run build

# production
FROM python:3.8-slim-buster as production

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY --from=build-vue /dist ./dist
COPY requirements.txt .
COPY app.py .
COPY .env .
COPY application.py .
COPY main/ ./main

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]