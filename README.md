# Issue Tracker

Small issue tracker assignment by using Django REST framework.

## Features

- Create a bug. A bug should have a title, a body, and a status (resolved/unresolved).
- Edit a bug.
- Delete a bug.
- View all bugs.
- View a specific bug.
- Add a comment to a bug. A comment should have a title, and a body.
- Delete a comment from a bug.
- Mark a bug as "resolved".
- Mark a bug as "unresolved".
- View all bugs marked as "resolved".
- Assign the bug to a user. A user is identified by its ID.

## Installation

Issue Tracker requires either [Python](https://www.python.org) v3.6 and [Django](https://www.djangoproject.com/) or Docker CE to run.

Install the dependencies and start the server.
### Using docker
```sh
cd issue_tracker_api_demo
docker-compose build
docker-compose up
```
### Without docker
```sh
cd issue_tracker_api_demo
1) Create venv -> virtualenv -p python3.6 .venv
2) Enable virtualenv -> source .venv/bin/activate
3) Install requirements -> pip install requirements.txt
4) Run django -> python manage.py runserver 0.0.0.0:8000
```

> Note: `db.sqlite3` is added intentionally. To avoid migrations and user creation. You can use below admin user if required.
`username: admin`
`password: admin`


You can test by navigating to your server address in your preferred browser.
```sh
127.0.0.1:8000
```

## Solutions

Create a bug. A bug should have a title, a body, and a status (resolved/unresolved).:

```sh
curl -X POST \
  http://localhost:8000/api/v1/bug/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "title": "Fix footer logo",
    "body": "Logo is not in good quality ",
    "status": "unresolved",
    "comment_bug": []
}'
```

Edit a bug:

```sh
curl -X PATCH \
  http://localhost:8000/api/v1/bug/1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "body": "Fix logo resolution"
}'
```

Delete a bug:

```sh
curl -X DELETE \
  http://localhost:8000/api/v1/bug/1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json'
```

View all bugs:

```sh
curl -X GET \
  http://localhost:8000/api/v1/bug/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json'
```

View a specific bug:

```sh
curl -X GET \
  http://localhost:8000/api/v1/bug/1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json'
```

Add a comment to a bug. A comment should have a title, and a body (You can add multiple comments if you want):

```sh
curl -X PATCH \
  http://localhost:8000/api/v1/bug/1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "comment_bug": [{"title": "Can you provide below details?", "body": "I need SMTP details."}]
}'
```

Delete a comment from a bug:

```sh
curl -X PATCH \
  http://localhost:8000/api/v1/bug/1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "comment_bug": []
}'
```

Mark a bug as "resolved" or "unresolved":

```sh
------------------------------------
Approach #1: (developed new endpoints)
------------------------------------
curl -X PATCH \
  'http://localhost:8000/api/v1/bug/status/1/?status=unresolved' \
  -H 'cache-control: no-cache' \
------------------------------------
Approach #2: (By using existing PATCH)
------------------------------------
curl -X PATCH \
  http://localhost:8000/api/v1/bug/1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "status": "resolved"
}'
```

View all bugs marked as "resolved" or "unresolved":

```sh
curl -X GET \
  'http://localhost:8000/api/v1/bug/?status=resolved' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
```

Assign the bug to a user. A user is identified by its ID.:

```sh
curl -X PATCH \
  http://localhost:8000/api/v1/bug/1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "assignee": 1
}'
```


