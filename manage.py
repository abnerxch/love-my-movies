from app import create_app
from flask_script import Manager,Server
from app import create_app,db
from app.models import User,Role

#creating app
app = create_app("production")

manager = Manager(app)
manager.add_command("server",Server)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


if __name__ == "__main__":
    manager.run()