
# AWS EC2 Get status

## How to run

```sh
$ sh run.sh
```

## Requirements

* python

* docker

## Alternatively

### build the container

```sh
$ docker build -t flask-aws .
```

### Run the Docker Container

```sh
$ docker run -d -p 5000:5000 flask-aws
```

## APIs

* GET   **/awshealth**   *retrieve the list of ec2 instances with status and type*

Response Sample
```json
[
	{"id":"i-02b9e24c4c468df55","instance-state":"stopped","instance-type":"t2.micro"},
	{"id":"i-07c9acc25cd94c15d","instance-state":"stopped","instance-type":"t2.micro"}
]
```