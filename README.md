# Python back-end for the weatherapp
* The aim of this project is to build a backend API for a personalised weather recommendation and severe weather warning system. The index.html in the templates directory will be removed in future releases: it is there to test the api until a proper frontend wrapper is developed.
## Installation
* Dependencies
  * Docker (Optional)
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
$ python -m .venv
```
* Install dependencies on requirements.txt:
<p>To enter the environtment:</p>

```sh 
$ source .venv/bin/activate
```
* Run the `main.py`:
```sh
$ python main.py
```
<p>By default you can access the api on <b>localhost:5000</b></p>
<p>You can access get a weather forecast using coarse location using <b> localhost:<port>/coarse </b> </p>

* Using front-end webapp: To use the front-end webapp serve the index.html on teplates directory.
