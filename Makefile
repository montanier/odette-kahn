build-dev:
	docker build -t dev -f Dockerfile.dev .

run-dev:
	export DB_PATH='/db/'
	export MODELS_PATH='/models'
	docker run -it -v `pwd`/db:/db -v `pwd`:/src -v `pwd`/models:/models -e DB_PATH -e MODELS_PATH -p 8000:8000 dev /bin/bash

test:
	export DB_PATH='/db/'
	export MODELS_PATH='/models'
	docker run -it -v `pwd`/db:/db -v `pwd`:/src -v `pwd`/models:/models -e DB_PATH -e MODELS_PATH dev pytest

build-prod:
	docker build -t prod .

run-prod:
	export DB_PATH='/db/'
	export MODELS_PATH='/models'
	docker run -v `pwd`/db:/db -v `pwd`/models:/models -e DB_PATH -e MODELS_PATH -p 8000:8000 prod

query:
	 curl -i -X GET -d "{\"name\": \"Louis Jadot 2012  Macon-Villages\"}" http://127.0.0.1:8000/wine -H 'Content-Type: application/json'
