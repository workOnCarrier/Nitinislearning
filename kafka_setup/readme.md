# setting up and testing kafka
https://www.baeldung.com/ops/kafka-docker-setup
## setup 
docker-compose -f docker-compose.yml up -d




https://www.linkedin.com/learning/apache-kafka-essential-training-getting-started-22398044/getting-started-with-apache-kafka

## setup
commandline / configs to setup on the network
```
docker-compose -f kafka-single-node.yml up -d
```

```
docker run --rm --network=dev-network --name my-db postgres
```

docker compose setup
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
