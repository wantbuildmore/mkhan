# Installation

    make install
    make manage -e CMD="syncdb"
    make manage -e CMD="migrate"


## To sign in via Google

 1. Go to [Google API Console](https://code.google.com/apis/console#access)
 1. Create `Client ID for web applications`
 1. Put into `Client ID for web applications` url `http://127.0.0.1:8000`
 1. Put into `cityconf/cityconf/local_settings.py`:

    DEBUG = True
    ASSETS_DEBUG = True

    GOOGLE_OAUTH2_CLIENT_ID = '<generated client id>'
    GOOGLE_OAUTH2_CLIENT_SECRET = '<generated client secret>'

## To start

Execute `make run`


## Admin

Go to [127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
Login: `admin`, password: `admin`
