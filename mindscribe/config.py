```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REPLICATE_API_KEY = os.environ.get('REPLICATE_API_KEY')
    KROKI_API_KEY = os.environ.get('KROKI_API_KEY')
    KEOKI_API_KEY = os.environ.get('KEOKI_API_KEY')
    FACEBOOK_MUSICGEN_API_KEY = os.environ.get('FACEBOOK_MUSICGEN_API_KEY')
    DEFAULT_TOKENS = 5
```