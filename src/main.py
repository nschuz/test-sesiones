from fastapi import FastAPI
from utils.serialize import sqlalchemy_to_dict
from manager.card import CardManager
from db.singleton import DatabaseSingleton
from sqlalchemy.orm import sessionmaker


app = FastAPI()

@app.get("/cards")
async def get_cards():
    
    
    #Primer Ejemplo Singleton
    
    # db = DatabaseSingleton('postgresql://postgres:postgres@localhost:5435/insights')
    # db2 = DatabaseSingleton('postgresql://postgres:postgres@localhost:5435/insights')
    
    # print(db is db2)
    # print(db.engine is db2.engine)
    # print(db.Session is db2.Session)
    
    # card_manager = CardManager(db.Session())
    # cards = card_manager.get_cards()
    
    
    
    
    # Segundo Ejemplo Singleton + Context Manager
    db2 = DatabaseSingleton('postgresql://postgres:postgres@localhost:5435/insights')
    card_manager = CardManager(db2)
    cards = card_manager.get_card_context_manager()
    

    
    # # Tercer Ejemplo Multiple Sessions
    # card_manager = CardManager()
    # cards = card_manager.get_card_multiple_sessions()
    
    

    
    
    #response = sqlalchemy_to_dict(cards, exclude_keys=["metadata"])    
    return cards
