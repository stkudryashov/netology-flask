import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLITE_URI = 'sqlite:///' + os.path.join(basedir, 'sqlite3.db')
