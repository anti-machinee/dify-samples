# app_factory.py
## create_flask_app_with_configs()
- Use flask to load config from dictionary
    - App.config.from_mapping()
- Configs are class attributes of the app
## initialize_extensions()
- Configure extensions to support the app. Each extension is initialized differently based on their SDK or how to integrate their services with the app