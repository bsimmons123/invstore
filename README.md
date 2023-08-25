# Catering
[![pipeline status](https://gitlab.com/sneakysquid05/invstore/badges/master/pipeline.svg)](https://gitlab.com/sneakysquid05/invstore/-/commits/master)
- View the demo [here](https://flask.sneakystuff.net)

#### Building with Docker:
```
$ docker build -t web:latest .
$ docker run -d --name simmons_portfolio -e "PORT=8765" -p 8007:8765 web:latest
```