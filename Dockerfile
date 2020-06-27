FROM django

ADD . /mypass

WORKDIR /mypass

RUN pip install --upgrade django

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
