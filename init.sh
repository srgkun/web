sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf

pip django install==1.8

sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/nginx restart


sudo /etc/init.d/mysql restart

mysql -u root -e
create database mydb;
./manage.py migrate
