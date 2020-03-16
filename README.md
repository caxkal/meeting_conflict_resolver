# System for processing batches of booking requests.

From list of meeting requests filters out conflicting ones, 
used first comes first serves approach


#### Dependencies

Create virtualenv and install dependencies with:

```bash
make dependencies
```

This will:

1. Create a python3 virtualenv under `.venv`
2. Install the latest pip in the virtualenv
3. Install all dependencies from `development.txt`

##### Running tests

Run unit tests with

```bash
make unit
```

##### Running the application

```bash
make run
```
