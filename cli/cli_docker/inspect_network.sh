# Get IP address
CONTAINER_NAME="docker-db-1"
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ${CONTAINER_NAME}
