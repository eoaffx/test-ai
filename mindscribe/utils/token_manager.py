```python
from mindscribe.models import User
from mindscribe import db

class TokenManager:
    @staticmethod
    def update_tokens(user_id, tokens):
        user = User.query.get(user_id)
        if user:
            user.tokens = tokens
            db.session.commit()
            return True
        return False

    @staticmethod
    def check_tokens(user_id):
        user = User.query.get(user_id)
        if user and user.tokens > 0:
            return True
        return False

    @staticmethod
    def deduct_token(user_id):
        user = User.query.get(user_id)
        if user and user.tokens > 0:
            user.tokens -= 1
            db.session.commit()
            return True
        return False
```