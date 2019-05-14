
  

# AWS EC2 Get status

  

## Requirements

  

* Python 3.x

* Docker

  

## User Configurations

Change the below settings in *main.py*

```sh

AWS_ACCESS_KEY_ID = 'xxxx'

AWS_SECRET_ACCESS_KEY = 'xxxx'

region_name = 'us-east-2'

```

## How to run

  

```sh

$ ./run.sh

```

  

### Alternatively

  

#### build the container

  

```sh

$ docker build -t flask-aws .

```

  

#### Run the Docker Container

  

```sh

$ docker run -d -p 5000:5000 flask-aws

```

#### Stop and remove the Docker Container

  

```sh

$ # list of all active and inactive containers

$ docker container ls -a

$ docker stop <container_ID>

$ docker container rm <container_ID>

```

### logs

```sh

$ docker logs <container_ID>

```

  

## APIs

  

* GET **/awshealth**  *retrieve the list of ec2 instances with status and type*

  

Response Sample

```json

[

{"id":"i-02b9e24c4c468df55","instance-state":"stopped","instance-type":"t2.micro"},

{"id":"i-07c9acc25cd94c15d","instance-state":"stopped","instance-type":"t2.micro"}

]

```