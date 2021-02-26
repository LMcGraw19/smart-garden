import os
import sys
import logging
#from flask import Flask

logging.basicConfig(filename='/tmp/flask.log',level=logging.INFO)
logging.debug(os.getcwd())
sys.path.insert(0,"/usr/local/env/lionsgate/")

python_home = '/usr/local/env/lionsgate/vlionsgate/'
#activate_this = python_home + '/bin/activate_this.py'
#exec(open(activate_this).read())

from app import create_app
#from app.lionsgate import app as application

#config_name = os.getenv('FLASK_ENV')
#application = create_app(config_name)
application = create_app()
logging.debug(os.path.dirname(application.root_path))

if __name__ == '__main__':
    application.run()
