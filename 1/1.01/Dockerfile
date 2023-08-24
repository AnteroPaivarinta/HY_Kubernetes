FROM node:alpine

WORKDIR ./

COPY package* ./

RUN npm install

COPY . .

CMD ["npm", "start"]
