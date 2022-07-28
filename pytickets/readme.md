Docker DB
---

* connect to docker-compose network from docker dev env
docker network connect pytickets_default $(head -1 /proc/self/cgroup|cut -d/ -f3)

* db url 
docker exec -i pytickets_postgres_1 psql postgres -U postgres -c "CREATE DATABASE tickets;"
docker exec -i pytickets_postgres_1 psql postgres -U postgres -c "CREATE ROLE tickets SUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'pass';"
postgresql://tickets:pass@postgres:5432/tickets  

* password
put in .env file   (need dotenv python module)
"export DB_PASS=pass"

* init
flask db init   
flask db migrate   
flask db upgrade   