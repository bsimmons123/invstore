# Catering
[![CI Build](https://github.com/bsimmons123/invstore/actions/workflows/docker-image.yml/badge.svg)](https://github.com/bsimmons123/invstore/actions/workflows/docker-image.yml)
- View the demo [here](https://flask.sneakystuff.net)

#### Building with Docker:
```
$ docker build -t web:latest .
$ docker run -d --name simmons_portfolio -e "PORT=8765" -p 8007:8765 web:latest
```
