# words_counter

A web tool developed in HTML, Ajax and CSS which is responsible to return the total words of a given text. The tool consumes an endpoint from a REST API developed in Python/Flask.

## Introduction

The tool is separated by the front-end and back-end parts:
- The front-end part consists in a simple HTML with jQuery Ajax and CSS. 
- The back-end part was developed in Python using Flask framework for the endpoints.

The tool shows up the value returned by the API without reloading the entire page. If there is no word in the text area, an error should occur saying that at least a word is necessary. 

## Requirements

 - [docker](https://docs.docker.com/)
 - [Python3](https://www.python.org/)

## Infrastructure

 - API - Application developed in Python and Flask;
 - Front-end - A web page with a simple text area to submit a text developed in HTML/Ajax/CSS;
 - Docker - A container to build the application.

## Configuration

After cloning the repository, build the image with the command below:
```
$ docker image build -t words_counter .
```
After successfully building the image, run an instance of the application with the following command:  
```
$ docker run -p 8000:8000 -d words_counter
```

## Getting Started

After the instance runs, the application will be available through the URL:

``http://localhost:8080/``

**Endpoint**

 - Return the total words of a given text using a JSON request with the message field, for example: {"message": "One Two"}
```
POST localhost:8080/counter/words
```

**Tests**

 - Run the tests developed with Pytest using the command below:
```
$ docker exec words_counter python -m pytest tests/
```

## App live in Cloud

The application is up and running in the Back4app accessing the URL below:
- [https://wordscounter-jpaulojpc.b4a.run/](https://wordscounter-jpaulojpc.b4a.run/)

