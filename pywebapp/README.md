# Set environment 
FLASK_ENV = development
FLASK_APP = .                     #where to look for files

flask run --host=0.0.0.0 --port=3000

docker compose up -d

#find docker container id
head -1 /proc/self/cgroup|cut -d/ -f3

#connect to network 
docker network connect pywebapp_default $(head -1 /proc/self/cgroup|cut -d/ -f3)

docker exec -i pywebapp_postgres_1 psql postgres -U postgres -c "CREATE DATABASE notes;"

CREATE DATABASE notes;"
CREATE ROLE notes SUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'pass';

#create db related scripts (.migration)
flask db init

#createupgrade script (.migrations/versions)
flask db migrate

flask db upgrade
