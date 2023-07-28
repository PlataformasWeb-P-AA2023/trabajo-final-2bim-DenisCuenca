![imagen](https://github.com/PlataformasWeb-P-AA2023/trabajo-final-2bim-DenisCuenca/assets/73245532/7fb7c4e7-38a1-4047-a003-6b7f9d8cbfae)

# Proceso para despliege de un proyecto de Django usando nginx con unicorn

- 1. Instalar dependencias necesarias:
     ```
     sudo apt update
     sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
     ```
  2. Configuración de postgres:
     ```
     sudo -u postgres psql
     CREATE DATABASE myproject;
     CREATE USER myprojectuser WITH PASSWORD 'password';
     ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
     ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
     ALTER ROLE myprojectuser SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
     \q
     ```
      ```
      pip install django gunicorn psycopg2-binary
      ```

      ## El proyecto a desplegar:
     dentro del archivo settings.py
      ```
     nano ~/myprojectdir/myproject/settings.py
       ```
      incluir las siguientes lineas tambien en el mismo archivo:
     
     ![imagen](https://github.com/PlataformasWeb-P-AA2023/trabajo-final-2bim-DenisCuenca/assets/73245532/07cd5f5b-7b85-43ed-8c91-6ebc3a254156)

### toques finales
```
~/myprojectdir/manage.py makemigrations
~/myprojectdir/manage.py migrate
~/myprojectdir/manage.py createsuperuser
~/myprojectdir/manage.py collectstatic
```

## Prueba con gunicorn
```
cd ~/myprojectdir
gunicorn --bind 0.0.0.0:8000 myproject.wsgi
```

## Nginx:
### Crear un socket
```
sudo nano /etc/systemd/system/gunicorn.socket
```

contenido del archivo:

![imagen](https://github.com/PlataformasWeb-P-AA2023/trabajo-final-2bim-DenisCuenca/assets/73245532/e6fc52dd-13dd-4830-8c1b-98ec23f24a19)


### Crear un servicio:
```
sudo nano /etc/systemd/system/gunicorn.service
```

contenido del archivo:

![imagen](https://github.com/PlataformasWeb-P-AA2023/trabajo-final-2bim-DenisCuenca/assets/73245532/ffd72017-4f25-483f-a130-c9c94c38a1ed)


Se habilita las nuevas funcionalidades con:
```
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

## Registrar los sitios con la configuración de Nginx:
```
sudo nano /etc/nginx/sites-available/myproject
```
contenido:

![imagen](https://github.com/PlataformasWeb-P-AA2023/trabajo-final-2bim-DenisCuenca/assets/73245532/3d46efe4-72d4-4cde-b0e0-c967b646bb22)

#### Registrar la configuación:
```
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```
Con esto se puede acceder a la aplicación desde el navegador:

![imagen](https://github.com/PlataformasWeb-P-AA2023/trabajo-final-2bim-DenisCuenca/assets/73245532/ceefec33-3a3f-4af3-8c71-164db125ad88)

Gracias muchas✨💋
