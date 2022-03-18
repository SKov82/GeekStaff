ECHO OFF
CLS
ECHO.
ECHO ...............................................
ECHO PRESS 1, 2 or 3 or 4 or 5 to select your task.
ECHO ...............................................
ECHO.
ECHO 1 - makemigrations
ECHO 2 - migrate
ECHO 3 - runserver
ECHO 4 - runserver 2
ECHO 5 - create superuser
ECHO.

SET /P M=Type 1, 2, 3 or 4 or 5 then press ENTER:
IF %M%==1 GOTO MAKEMIGRATIONS
IF %M%==2 GOTO MIGRATE
IF %M%==3 GOTO RUNSERVER
IF %M%==4 GOTO RUNSERVER_2
IF %M%==5 GOTO CREATE_SUPERUSER
GOTO END

:MAKEMIGRATIONS
python manage.py makemigrations
GOTO END

:MIGRATE
python manage.py migrate
GOTO END

:RUNSERVER
python manage.py runserver
GOTO END

:RUNSERVER_2
python manage.py runserver 127.0.0.1:5500
GOTO END

:CREATE_SUPERUSER
python manage.py createsuperuser
GOTO END

:END