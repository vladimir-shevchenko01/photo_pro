# PHOTOGRAPHER PROFILE

This is a portfolio site.

There is a slider on the main page showing the most interesting works, from where you can go to the gallery section containing photo shoots by category. You can familiarize yourself with each category separately. In addition, the "About me" and "Contacts" pages are available.

### Technologies used in this project:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
<img src ="https://img.shields.io/badge/postgres-%23316192.svg?&style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/docker%20-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white"/>
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
<img src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/>
<img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>
<img src="https://img.shields.io/badge/github%20actions%20-%232671E5.svg?&style=for-the-badge&logo=github%20actions&logoColor=white"/>
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)



### How to deploy a project locally:
1. Clone the repository:

```
git clone https://github.com/vladimir-shevchenko01/photo_pro.git
cd photo_pro
```


2. Create a `.env` file following the example of `.env.example` in the config folder and fill it out.

```
*DJANGO_SECRET_KEY can be generated as follows:
 python manage.py shell
 from django.core.management import utils
 utils.get_random_secret_key()
```


3. From the root directory, execute the following commands:

```
cd .docker
docker compose up -d
```

The site will be available at localhost:8000.

<h4 align="left">Vladimir Shevchenko <a href="https://github.com/vladimir-shevchenko01" target="_blank">
GitHub</a>  <a href="https://t.me/vsel_live" target="_blank">  🛒</a></h4>