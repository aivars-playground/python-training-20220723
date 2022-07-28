# Set environment 
FLASK_ENV = development
FLASK_APP = .                     #where to look for files

flask run --host=0.0.0.0 --port=3000

docker compose up -d

#find docker container id
head -1 /proc/self/cgroup|cut -d/ -f3

#connect to network 
docker network connect pywebapp_default $(head -1 /proc/self/cgroup|cut -d/ -f3)

sudo docker exec -i postgres psql postgres -U demo -c "CREATE DATABASE notes;"