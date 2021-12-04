# Odette-kahn

Serving of model trained on "Wine Quality Data Set" (https://archive.ics.uci.edu/ml/datasets/wine+quality) through a REST Full API

## Installing
Make shre that Docker and Docker-compose are installed.

## Running

Start the API with the following command:
```
make run-prod
```
If the command is run for the first time. It will automatically build the docker. This shouldn't take too long.

Once the api has started you can try to query it with the two following commands:

The first option will query the API with a known wine name. We will get in return the wine properties, known quality and predicted quality:
```
make query-name
```

The second option will query the API with a list of wine properties. We will get in return the predicted quality of the wine:
```
make query-predict
```
