FROM python:3.10.4
WORKDIR /web
COPY . /web
RUN pip3 install -r /web/requrements.txt
RUN python3 manage.py migrate

EXPOSE 8000
CMD ["python3", "manage.py" , "runserver"]