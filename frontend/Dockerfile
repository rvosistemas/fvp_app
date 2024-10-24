FROM node:20-alpine

WORKDIR /${ANGULAR_WORKDIR}/

COPY package*.json /${ANGULAR_WORKDIR}/

# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list
# RUN apt-get update && apt-get install --no-install-recommends -y google-chrome-stable

RUN npm install

RUN npm install puppeteer

COPY . /${ANGULAR_WORKDIR}/

ENV CHROME_BIN=/usr/bin/google-chrome-stable

EXPOSE ${ANGULAR_PORT}
