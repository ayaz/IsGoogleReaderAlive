IsGoogleReaderAlive
===================

A small Flask-based application which checks whether Google Reader is still alive. 

In order to set up this Flask-based application, a Python environment must first
be created. Since the various Python third-party requirements are provided in
the pip readable requirements.txt file, the environment can easily be setup with
the following command:

`$ pip install -r requirements.txt`

The Flask application can be started with:

`$ python IsGoogleReaderAlive.py`

The `IsGoogleReaderAlive.py` must first be edited to provide GMAIL user,
password, and To email address information, since the script requires these to
send an email when it finds that Google Reader isn't alive anymore.
