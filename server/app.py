import connexion
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

connex_app = connexion.App(__name__, specification_dir='./')
connex_app.add_api('swagger.yml', arguments={'title': 'API toystore'}, pythonic_params=True)
app = connex_app.app
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
application = app

import src.entities
if __name__ == '__main__':
    connex_app.run(host='0.0.0.0', port=8080, debug=False)
