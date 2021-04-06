# Editing code

This directory contains all the files required for the virtual environment to work properly.
To activate the virtualenv, from the `backend` directory, run:

```
$ source bin/activate
```

(If using an alternative shell, scripts are available for fish and csh.
The standard script works for zsh as well as bash.)

When finished, run:

```
$ deactivate
```

# Running the API

Active the virtualenv as described above.
Then execute the following command:

```
$ python3 api.py --debug
```

The server should now be running on port 5000.
You can access it locally at `localhost:5000`.
When finished, type `Ctrl+C` to shut down the server and deactivate the virtualenv as described above.
