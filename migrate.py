from flask_migrate import Migrate

import models
import app


application = app.app
migrate = Migrate(application, app.db)
