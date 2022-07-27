This is [Ropomoda](https://www.ropomoda.com/) backend project 

![build](https://github.com/RopoModa/ropomodafront/actions/workflows/node.js.yml/badge.svg)

## Ropomoda Back-end project

First, migrate:

```bash
cd ./backend
python3 manage.py migrate
```

create a super user
```bash
python3 manage.py createsuperuser --mobile [phone number] --noinput
```

then , run development server
```bash
python3 manage.py runserver
```
Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.


## Deploy on Arvan

```bash
docker build -t registry.ropomoda.com/ropomoda-backend:[version] .
docker push registry.ropomoda.com/ropomoda-backend:[version]

arvan paas apply -f k8s/apps/backend/deployment.yaml
```

