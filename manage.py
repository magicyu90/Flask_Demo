# -*- coding: utf-8 -*-
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.main import create_app
from app.db import db

app = create_app()
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('runserver', Server(host='0.0.0.0', port=5002, use_debugger=True))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
