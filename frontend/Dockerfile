FROM node:14

WORKDIR /app

COPY package*.json ./

RUN apt-get update && apt-get install -y nodejs npm

RUN npm install

COPY . .

CMD [ "npm", "start" ]
