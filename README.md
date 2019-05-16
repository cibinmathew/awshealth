# AWS EC2 Get status

Features
--------

  - Get list of EC2 instances and running status of a particular AWS region.
  - Configurable support for ``AWS_ACCESS_KEY_ID`` and ``AWS_SECRET_ACCESS_KEY`` environment variables and region.


## Requirements
  
  - Python 3.x
  - Docker

## Configuring the account

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
  
#### Build the container
  
```sh

docker build -t flask-aws .

```

  
#### Run the container

```sh

docker run -d -p 5000:5000 flask-aws

```

#### Stop and remove the Container

```sh

docker container ls -a  # list of all active and inactive containers

docker stop <container_ID>

docker container rm <container_ID>

```

### logs

```sh

docker logs <container_ID>

```

  
## APIs

* GET **/awshealth**  *retrieve the list of ec2 instances with status and type*

Example

```sh
curl <base_url>/awshealth
```
Sample response

```json

[

{"id":"i-02b9e24c4c468df55","instance-state":"stopped","instance-type":"t2.micro"},

{"id":"i-07c9acc25cd94c15d","instance-state":"stopped","instance-type":"t2.micro"}

]

```


Links
-----
- Website: https://github.com/cibinmathew/awshealth
- Documentation: TODO
- Docker: https://docs.docker.com/engine/reference/commandline/docker
- Code: https://github.com/cibinmathew/awshealth
- Issue tracker: https://github.com/cibinmathew/awshealth/issues