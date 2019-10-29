import os

EXEC_MODE = os.environ.get("EXEC_MODE", "development")
if EXEC_MODE == "development":
    from .development import *
elif EXEC_MODE == "production":
    from .production import *