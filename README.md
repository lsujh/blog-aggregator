# Blog-aggregator
https://blog-agregator.herokuapp.com/

Блог с возможностью пользователям lобавлять статьи, комментировать и ставить оценки(like).
Агрегатор для получения статей по RSS с сайтов заданных через админку.

## Cloning & Run:
git clone https://github.com/lsujh/blog-aggregator.git

cd blog-aggregator

pip install -r requirements.txt

python3 manage.py runserver

python3 manage.py migrate

python3 manage.py createsuperuser



