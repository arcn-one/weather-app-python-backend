# Python back-end for the weatherapp
* The aim of this project is to build a backend API for a personalised weather recommendation and severe weather warning system. The index.html in the templates directory will be removed in future releases: it is there to test the api until a proper frontend wrapper is developed.
## Installation
* Dependencies
  * Docker
  * Python

* Clone the git repo
```sh
$ git clone https://github.com/phaeseval/weather-app-python-backend
```

### Docker

* To install in a docker container run: 
```sh
$ docker build -t <image-name> .
```

* Run the docker container with:
```sh
$ docker run -p 5000:5000 <image-name>
```

### Local Installation
* Create a python-env to avoid breaking your system:
```sh
$ python -m venv .
```
* Install dependencies on requirements.txt:
```sh 
$ .venv/bin/python -m pip install -r requirements.txt
```
* Run the `main.py`:
```sh
$ .venv/bin/python main.py
```
<p>By default you can access the web app by visiting the localohst:5000 on your web browser</p>
