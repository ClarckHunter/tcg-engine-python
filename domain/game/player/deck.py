from ...cards.card import Card

class Deck:

    def __init__(self, deck:list):

        self.deck = deck
        self.actual_deck = deck
    


    
    
    #permite robar la carta del tope del deck
    def draw(self):
        pass
        #roba la carta del tope del deck y la borra 
    

    #permite el mezclar el deck
    def shuffle():
        pass

    #permite robar una carta especifica del deck
    def search(card):
        pass

    #pregunta si el deck tiene la carta que buscas
    def has_card(card)->bool:
        return True

	#funcion llamada al iniciar partida
    def set_deck()->None:
        pass