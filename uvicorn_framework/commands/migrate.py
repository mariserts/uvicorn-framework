def migrate(settings):
    settings.DB_MODEL_CLASS.metadata.create_all(settings.DB_ENGINE.engine)
