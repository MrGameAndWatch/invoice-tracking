FROM node:12.2.0-alpine
RUN mkdir /employee-fronted

ENV PATH /employee-frontend/node_modules/.bin:$PATH

COPY . /employee-frontend/
WORKDIR /employee-frontend
RUN yarn install
CMD ["yarn", "serve"]