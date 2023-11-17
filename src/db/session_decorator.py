from db.multiple import session_scope


def db_session(method):
    def wrapper(self, *args, **kwargs):
        with session_scope() as session:
            self.session = session
            return method(self, *args, **kwargs)
    return wrapper
