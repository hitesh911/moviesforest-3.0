FROM node
COPY app.js .
EXPOSE 3333
CMD [ "node", "app.js" ]
