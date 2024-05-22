# User Search Gis

## Provides api to do following:

- Add new user
- List all users
- Retrive user (when authenticated)
- Delete user (when authenticated)
- Update user details and user profile detail (when authenticated)
- Seach user within 10 KM radius using their home address
- Return geoJSON of line vector from user's home address to office address
- Wishes users Happy birthday on their birthday automatically

## 🚀Setting up

```
python -m venv venv
```

For  Linux :
```
source ./venv/Script/activate
```

```
pip install -r requirements.txt
```

## 🏁Run

```
python manage.py runserver
```

```
celery -A user_search_gis worker -B
```

