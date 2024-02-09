from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .model.base import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
