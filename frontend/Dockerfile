FROM node:20-alpine

WORKDIR /app

# Cambiado de package*.json a ./package*.json
COPY package*.json ./

RUN npm install && npm install puppeteer

# Cambiado de COPY . /app/ a COPY . .
COPY . .

ENV CHROME_BIN=/usr/bin/google-chrome-stable

EXPOSE 4200
