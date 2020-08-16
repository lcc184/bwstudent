from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from students import create_app,db
# 运行此代码功能
app = create_app()
manager = Manager(app)
Migrate(app,db)
manager.add_command("db",MigrateCommand)






if __name__ == "__main__":
    manager.run()