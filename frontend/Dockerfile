# FROM node:20-alpine

# # Instalar dependencias necesarias para Chrome y Puppeteer
# RUN apk add --no-cache ca-certificates chromium freetype freetype-dev harfbuzz nodejs nss ttf-freefont yarn

# WORKDIR /app

# # Cambiado de package*.json a ./package*.json
# COPY package*.json ./

# RUN npm install

# # Cambiado de COPY . /app/ a COPY . .
# COPY . .

# ENV CHROME_BIN=/usr/bin/google-chrome-stable
# ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

# EXPOSE 4200


FROM node:21

WORKDIR /app

COPY package*.json ./

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list
RUN apt-get update && apt-get install --no-install-recommends -y google-chrome-stable

RUN npm install

RUN npm install puppeteer

COPY . .

ENV CHROME_BIN=/usr/bin/google-chrome-stable

EXPOSE 4200
