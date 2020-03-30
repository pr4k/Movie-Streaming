# Movie Streaming App Created for Assessment Task (Apli.ai)

## Task
>You have to create a Movie streaming web app using the Django Framework. The app will have
>two types of users, an admin (only one) & some general users (multiple)
>Once a general user is successfully logged in, he’ll be redirected to the All Movies page. All the
>movies available on the platform will appear on this All Movies page in a grid format. Once the
>user selects a movie he’ll be redirected to the Movie Detail page. On the Movie Detail page,
>the user can play the movie and post public comments. All the comments on the movie must be
>visible to all the users

# Description

So the app contains 
- Login Page
- Signup Page
- All Movies Page
- Particular Movie Page
- Add Movie Form
- Update Movie Form
- A Comment Section
  
For images of each Section go to

[images/](images/readme.md)

For starting the project:
```bash
# Create a Virtual Environment
python3 -m venv .env

# Source Env
source .env/bin/activate

# Install django
pip3 install django

# Clone the project
git clone https://github.com/pr4k/Movie-Streaming

# Install Requirements
pip3 install -r requirements.txt

# Start App
python3 manage.py runserver

# Done
```

# Dependencies

- [Crsipy forms](https://github.com/django-crispy-forms/django-crispy-forms)
- [django video embed](https://github.com/jazzband/django-embed-video)
  
