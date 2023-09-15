To get up and running with fake Product data:
```
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python manage.py migrate
(.venv) $ python manage.py generate_dummy_data
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
```

Go to 'http://localhost:8000/admin'