from sqlalchemy.orm import registry
from connector import DB_ENGINE

REGISTRY = registry()
BASE = REGISTRY.generate_base()


def create_all():
	BASE.metadata.create_all(DB_ENGINE)


def wipe():
	REGISTRY.metadata.drop_all()
