# Development

You will need to either configure the bot to work with your own credentials via
the `env` file, or ask me to add your pgp key to the repo (please see
git-secret.io)

I'm using `venv` as a stop-gap until I dockerize it. Running `make` is always a
good starting point tho.

Next, install dependencies with `make install`.

# Testing

To run the project, you need to first make sure all the required environment
variables have been set up. You can kick it off with my settings by running
`source env.zaliznychnyj`.

Now you should be ready to start the bot using `make run`.

# Deployment

