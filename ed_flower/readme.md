install dulu requirement nya dengan cara

pip install -r requirement.txt

jangan lupa setup database nya, disini menggunakan mysql dibantu dengan xampp

dengan nama db test_flower


migrate db:

py manage.py makemigrations flower
py manage.py migrate