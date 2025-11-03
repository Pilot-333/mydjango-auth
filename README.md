Django authentication and authorization
=======================================

Example project with default django authentication and authorization via vk.com by using django-allauth package.

Install
-------
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
```

Run
---

```bash
python manage.py runserver 0.0.0.0:80
```

Open in browser: [http://localhost](http://localhost)

Note.<br/>
`sudo` maybe needed to run on 80 port: `sudo python manage.py runserver 0.0.0.0:80`.

If there are troubles running on 80 port, run on port 8000:
```bash
python manage.py runserver 0.0.0.0:8000
```
and open in browser: [http://localhost:8000](http://localhost:8000)

But in that case some of oauth providers may not work.
