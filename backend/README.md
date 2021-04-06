# First-time setup

From the repository's root directory, run the following commands:

```
$ sudo apt install python3 python3-venv pip3  # if not already installed

$ python3 -m venv backend

$ cd backend

$ source bin/activate

$ pip3 install flask

$ deactivate
```

This application was developed using Python 3.8, which is the default on Ubuntu 20.04 and newer.

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
