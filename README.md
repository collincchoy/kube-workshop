# Kubernetes + Containerization Workshop

## Dockerize

1. Add Dockerfile to for each service

## Docker-composify

1. Add Docker extension for vs code
2. CMD+Shift+P > Add Docker Compose Files to Workspace to auto generate a docker-compose.yml
3. Change the build context to be inside each individual folder
4. Update the CRONKITE_HOST env var for the webserver to use the network bridge that compose creates (Ignore .env files)
5. Add the host option by command override in docker-compose

```
docker-compose build
docker-compose up -d
docker-compose ps

# navigate to http://localhost:5000

docker-compose down
```
