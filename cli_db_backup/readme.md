docker compose up -d
docker network connect cli_db_backup_default $(head -1 /proc/self/cgroup|cut -d/ -f3)