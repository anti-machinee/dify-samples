from configs.app_config import DifyConfig
from dify_app import DifyApp
from extensions import (
    ext_database,
    ext_migrate,
    ext_redis,
    ext_storage
)


def setup_app_real():
    dify_app = DifyApp(__name__)
    dify_config = DifyConfig(_env_file="dify/api/.env")
    dify_app.config.from_mapping(dify_config.model_dump())
    ext_database.init_app(dify_app)
    ext_migrate.init_app(dify_app)
    ext_redis.init_app(dify_app)
    ext_storage.init_app(dify_app)
    return dify_app
