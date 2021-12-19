FROM python:3.9.6

WORKDIR /home/

RUN git clone https://github.com/ethanKim93/PinterestClone.git

WORKDIR /home/PinterestClone/

RUN pip install -r requirments.txt

RUN echo "SECRET_KEY=django-insecure-u+(230nr#&w=2x4+9)1_sv+$76nkh^o7vsdox3z%!j^*6am-7s" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000 "]