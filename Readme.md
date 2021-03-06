# Django Blog App

This is a toy Django app which I use to throw in code to try out different concepts in Django, so it can be a bit messy here and there. Also it might contain code that is not used anymore. So you can say it's just a playground where I can throw anything in for testing.

Among other things it includes:

- pages app
- users app
- blog app
    - uses django markdown editor for blog posts
    - comments on post with django-contrib-comments
    - hooks into update of bosts with django-lifecycle
- custom user model (email instead of username)
- e-mail verification
- django debug toolbar (only in development)
- docker files for spinning up containers (python and postgresql)
- basic tests for pages and users
- different settings files for development and production

## Production and development settings

The setting file are split up in production and a development settings files. Also the project have one docker-compose.yml for production and one for development. Within the docker-compose files you can find the parameter for which settings file to use on the runserver command. To make it easier and less to type for each command, there is a Makefile with different common operations.

## Quick start

1. Clone this repository

` https://github.com/Joeriksson/django-template.git`

2. Install [Docker Desktop](https://www.docker.com/products/docker-desktop) to be able to use the docker environment.

3. Create an .env file in the root folder with the the following parameters:

```ENVIRONMENT='development'
SENDGRID_PASSWORD=<you sendgrid password>
SENDGRID_USERNAME=<your sendgrid username>
SECRET_KEY=<your secret key>
DEBUG=True
```

3. In the directory where you cloned the repository, run the following command:

`make dev_build`

4. The container should now be up and running. Run:

  `make dev_web_exec cmd='python -m pip install -r requirements.txt''`
  
  To install the dependencies. 
  
5. Restart the container and rebuild it:

  `make dev_build` 
  
  Then check in you browser that you see a start web page at `http://127.0.0.1:8080`

5. Run a migration to build the databases

  `make dev_web_exec cmd='python manage.py migrate'`

6. Create a Django super user to log in to the admin

  `make dev_web_exec cmd='python manage.py createsuperuser'`

7. Goto `http://127.0.0.1:8080/admin` and login with the super user account you just created.

8. Go on and build you app.

If you want to stop the container run:

  `make dev_down`


