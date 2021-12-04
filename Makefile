build-dev:
	docker-compose -f docker-compose.dev.yml build odette_kahn_dev

run-dev:
	export DB_PATH='/db/'
	export MODELS_PATH='/models'
	docker-compose run --service-ports --rm odette_kahn_dev bash

test:
	export DB_PATH='/db/'
	export MODELS_PATH='/models'
	docker-compose run --rm odette_kahn_dev pytest

build-prod:
	#docker build -t prod .
	docker-compose -f docker-compose.dev.yml build odette_kahn_prod

run-prod:
	export DB_PATH='/db/'
	export MODELS_PATH='/models'
	docker-compose run --service-ports --rm odette_kahn_prod

query-name:
	 curl -i -X GET -d "{\"name\": \"Louis Jadot 2012  Macon-Villages\"}" http://127.0.0.1:8000/wine -H 'Content-Type: application/json'

query-predict:
	 curl -i -X GET -d \
	 "{\"alcohol\":"11.0",\"chlorides\":"0.067",\"citric_acid\":"0.47",\"density\":"0.99549",\"fixed_acidity\":"6.0",\"free_sulfur_dioxide\":"18.0",\"ph\":"3.39",\"residual_sugar\":"3.6",\"sulphates\":"0.66",\"total_sulfur_dioxide\":"42.0",\"volatile_acidity\":"0.31"}" \
	 http://127.0.0.1:8000/prediction -H 'Content-Type: application/json'
