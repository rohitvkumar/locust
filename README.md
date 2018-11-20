# Set up a load test with locust swarm.
1. Build the locust container:

`$ docker build -t locustio .`

2. Run the container

`$ docker run --rm -it -v .:/locust -p 8089:8089 --name $NAME locustio --host=$HOST`
