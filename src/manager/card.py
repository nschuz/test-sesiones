from models.card import CardModel
from db.session_decorator import db_session

class CardManager:
    
    def __init__(self, session=None):
        self.session = session
    
    def __close_session(self):
        self.session.close()
    
    #first example
    def get_cards(self):
        cards = self.session.query(CardModel).limit(50).all()
        return cards
        
     
    
    #second example
    def get_card_context_manager(self):
        with self.session.session_context() as session:
            try:
                return session.query(CardModel).limit(50).all()

            except Exception as e:
                print(f"Error: {e}")

        
    #last example
    @db_session
    def get_card_multiple_sessions(self):
        return self.session.query(CardModel).limit(50).all()
        

            