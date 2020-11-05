# Messenger API Homework

Thanks for reviewing my homework! It's been built with FastAPI and RethinkDB. FastAPI comes with docs that allow you to test it. Quick note, you can request messages by the `sender_id` and/or the `recepient_id`. For ease of testing, the ids for both are integers between 1 and 10.

## Getting Started

- Clone the project
- Install [RethinkDB](https://rethinkdb.com/docs/install)
- In terminal, run `pipenv install` to install dependencies into Python virtual environment
- In a new terminal, run `rethinkdb` to start up RethinkDB
- Back in the 1st terminal, run `pipenv shell` to start virtual environment
- Once in shell, run `python create_db.py` to get database up and running with seeded data
- Start the server with `uvicorn api.app:app`
- Navigate to http://127.0.0.1:8000, the docs for the API will allow you to test it
- Enjoy! :)
