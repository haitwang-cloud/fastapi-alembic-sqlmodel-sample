set -e
image="sample-app"
tag=$image:latest
docker build -t $tag .
#docker push $tag

