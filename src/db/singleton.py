from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

class DatabaseSingleton:
    _instance = None

    def __new__(cls, connection_string):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.engine = create_engine(connection_string)
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
        return cls._instance
    
    
    ## SEGUNDO EJEMPLO
    def session_context(self) -> Session:
        return self.Session()