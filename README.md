
## Comandos usados
```
docker-compose run riot-backend django-admin startproject backend-riot .
docker-compose run riot-backend django-admin startproject backendRiot .
sudo chown -R $USER:$USER backendRiot manage.py
ll
docker-compose up
docker-compose run riot-backend python manage.py makemigrations
docker-compose run riot-backend python manage.py migrate
docker-compose up
docker-compose run riot-backend python manage.py createsupersuer
docker-compose run riot-backend python manage.py createsuperuser
docker-compose up
docker-compose run riot-backend python manage.py startapp apiv1
ls
ll
sudo chown -R $USER:$USER apiv1
ll
docker-compose run riot-backend python manage.py makemigrations
docker-compose run riot-backend python manage.py migrate
docker-compose up
docker-compose up --build
docker-compose run riot-backend python manage.py makemigrations
docker-compose run riot-backend python manage.py migrate
docker-compose up --build
```