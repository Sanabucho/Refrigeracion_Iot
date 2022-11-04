
## Iniciar API
docker-compose run riot-backend python manage.py makemigrations
docker-compose run riot-backend python manage.py migrate
docker-compose run riot-backend python manage.py createsuperuser
docker-compose up

## Backup DB
# Crear Backup
docker exec refrigeracion_iot_riot-db_1 pg_dumpall -U postgres > /path/to/db/backup.sql
# Recuperar DB
docker exec refrigeracion_iot_riot-db_1 createdb -U postgres postgres
cat /path/to/db/backup.sql | docker exec -i refrigeracion_iot_riot-db_1 psql -U postgres