# Crushmate

Crushmate is a campus matchmaking web application that recommends students to each other based on overlapping class schedules, so that a match is someone you can actually meet on campus. It was built by a team of four for the Database System Application course at National Taipei University of Technology (Taipei Tech) in spring 2025, and received the highest score in the class (95/100).

> Classmates by chance, crushmate by choice.

## How it works

1. A student signs up, uploads profile photos, writes a short bio with interests and department, and enters their weekly class schedule.
2. The home page shows profile cards of other students. Candidates are ranked by the number of class periods they share with the user, and students the user has already liked, matched or unmatched are filtered out.
3. The user swipes right (like) or left (pass) on each card. The swipe is sent to the server without reloading the page.
4. When two students like each other, a match is created, a pop-up appears, and the two can chat.

## Features

- Account registration, login and password reset with django-allauth, with custom validation for usernames
- Profile pages with multiple photos and a selectable main photo
- Bio page with interest tags and department
- Weekly class schedule stored as JSON
- Schedule-based recommendations on the home page
- Swipe interface with asynchronous like/pass requests and a match pop-up
- One-to-one chat between matched users
- Unmatch function
- REST API with JWT authentication, used by a companion Android app

## Tech stack

- Back end: Python, Django 5.0, SQLite
- Authentication: django-allauth (web), Django REST Framework with SimpleJWT (mobile API)
- Front end: Django templates, Tailwind CSS, vanilla JavaScript (fetch API, DOM events)
- Images: Pillow

## Project structure

```
Crushmate/
├── django_project/   Project settings and root URL configuration
├── accounts/         Sign-up and login forms, signup adapter, registration API
├── navigation/       Home page, recommendations, swipe interface
├── match/            Like, Match and UnmatchRecord models; swipe and unmatch endpoints
├── chat/             Chat room and conversation list
├── course/           Weekly class schedule (JSONField)
├── bio/              Bio, interests and department
├── profilepage/      Profile photos and profile API
├── settingsapp/      Settings page
├── templates/        Shared base template and account pages
├── static/           Static assets
└── media/            Uploaded profile photos (not tracked in Git)
```

## Data model

| Model | Purpose |
| --- | --- |
| User | Built-in Django user model for accounts and passwords |
| Profile | One-to-one profile for each user, created automatically on sign-up |
| ProfilePhoto | Photos uploaded by a user, one of which is marked as the main photo |
| UserBio | Bio text, interests and department |
| UserCourseSchedule | Weekly schedule stored as JSON, for example `{"Mon-1": "Math"}` |
| Like | Records whether one user liked or passed on another |
| Match | Created when two users like each other |
| UnmatchRecord | Records unmatches so the users are not recommended again |
| Message | Chat messages between two users |

## Getting started

Requirements: Python 3.12

```bash
git clone https://github.com/andrz93/Crushmate-final.git
cd Crushmate-final
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in a browser and register an account.

## Team and contributions

| Member | Main contributions |
| --- | --- |
| Andrew Cheng ([@andrz93](https://github.com/andrz93)) | UI design; accounts app (custom sign-up and login forms, signup adapter, login, sign-up and password reset pages); navigation app (home page, automatic profile creation); shared base template; swipe interaction and match pop-up in JavaScript; profile page avatar menu |
| Piko | Chat app, course app, bio app, recommendation logic |
| Alina | Profile page app, settings app, media handling, matching system |
| Harrison | Mobile compatibility, REST API and connection to the Android app |
