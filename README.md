# Messenger API Homework

Thanks for reviewing my homework! It's been built with FastAPI and RethinkDB. FastAPI comes with docs that allow you to test it. Quick note, you can request messages by the `sender_id` and/or the `recipient_id`. For ease of testing, the ids for both are integers between 1 and 10.

## Getting Started

- Clone the project
- Run Docker ([Install](https://docs.docker.com/get-docker/) if needed)
- In terminal, run `docker-compose up --build`
- When that completes, in a new terminal, run `docker exec -it messengerapi_fastapi_1 python create_db.py`, it will notify you that the database has been created
- Navigate your broswer to http://:0.0.0.0
- Enjoy! :)
