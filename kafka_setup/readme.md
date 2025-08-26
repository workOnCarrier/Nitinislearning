# setting up and testing kafka
https://www.baeldung.com/ops/kafka-docker-setup
## setup 
docker-compose -f docker-compose.yml up -d




https://www.linkedin.com/learning/apache-kafka-essential-training-getting-started-22398044/getting-started-with-apache-kafka

## setup
commandline / configs to setup on the network

* Create the docker network
```
docker network create dev-network
```

* use docker-compose to bring up kafka and kafka-ui to support diagnostics
```
docker-compose -f kafka-single-node.yml up -d
```

* -- if you want to launch a specific container e.g. postgres to be connected to the same docker network
```
docker run --rm --network=dev-network --name my-db postgres
```

* example docker compose setup -- check file `kafka-single-node.yml`
```
services:
  app:
    image: my-app
    networks:
      - dev-network
  db:
    image: postgres
    networks:
      - dev-network
networks:
  dev-network:
    external: true
```

launching docker containers in `kafka-single-node.yml` results in :
1. kafka instance
2. kafka-ui -- available on http://localhost:8080 ... this allows for checking the status of kafka cluster in browser

