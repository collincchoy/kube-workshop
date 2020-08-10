# Web Service (Made w/ Flask)

## Setup
```
pip install -r requirements.txt
```

### Set Host URL to Cronkite Service
The application reads this from env var `CRONKITE_HOST`. The Flask
application is configured with `dotenv` so simply add a `.env` file
like so to set the variable locally.
```
# Example
echo "CRONKITE_HOST=http://localhost:8000" > .env
```

## Run Server
```
flask run
# With reloading
flask run --reload
# With reloading + Dev mode (Or add var to `.env`)
FLASK_ENV=development flask run --reload
```
