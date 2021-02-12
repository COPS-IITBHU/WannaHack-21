FROM node:14

WORKDIR /usr/src/web1

COPY package*.json ./

RUN npm ci

COPY . .

EXPOSE 1729

CMD ["node", "main.js"]
