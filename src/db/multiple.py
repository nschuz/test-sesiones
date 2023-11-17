from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import NullPool
from contextlib import contextmanager


@contextmanager
def session_scope():
    engine = create_engine("postgresql://postgres:postgres@localhost:5435/insights", poolclass=NullPool, pool_pre_ping=True)
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    some_session = Session()
    some_session.expire_on_commit = False
    """Provide a transactional scope around a series of operations."""
    try:
        yield some_session
        some_session.commit()
    except Exception as e:
        some_session.rollback()
        raise e
    finally:
        some_session.expunge_all()
        some_session.close()
