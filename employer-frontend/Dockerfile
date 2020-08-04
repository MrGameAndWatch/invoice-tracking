FROM node:12.2.0-alpine
RUN mkdir /employer-fronted

ENV PATH /employer-frontend/node_modules/.bin:$PATH

COPY . /employer-frontend/
WORKDIR /employer-frontend
RUN yarn install
CMD ["yarn", "serve"]