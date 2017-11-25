FROM node:6
WORKDIR /app/js
RUN ls
COPY js/package.json .
RUN npm install
COPY . .
CMD [ "npm", "start" ]