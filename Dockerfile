FROM alpine:latest as build-stage
WORKDIR /app
RUN apk add yarn && yarn -V
COPY ./frontend/package.json ./
COPY ./frontend/yarn.lock ./
RUN yarn install
COPY ./frontend .
RUN yarn run build

FROM python:3.7.5-alpine as production-stage
WORKDIR /app
COPY . .
COPY --from=build-stage /app/dist ./frontend/
RUN python -m pip install -r ./requirements.txt