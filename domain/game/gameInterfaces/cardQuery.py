from ...cards import CardSpace

class CardQuery:
    def __init__(self, cards_spaces:list[CardSpace], include_empty=False):
        if include_empty:
            self._cards_spaces = cards_spaces
        else:
            self._cards_spaces = [s for s in cards_spaces if s.has_card()]

        self._include_empty = include_empty
        

	#factory
    @classmethod
    def from_spaces(cls, spaces):
        obj = cls([])
        obj._cards_spaces = spaces
        return obj


	#helpers
    def _compare(self, a:int, b:int, op):
        match op:
            case '==': return a == b
            case '<': return a < b
            case '>': return a > b
            case '<=': return a <= b
            case '>=': return a >= b
            case _: raise ValueError(f"Invalid operator {op}")

    def _filter(self, predicate):
        return CardQuery.from_spaces(
            [
                s for s in self._cards_spaces 
                if s.card is not None and predicate(s.card)
            ],
            include_empty = self._include_empty
        )
    
    def no_empty_check(self)->None:
        if self._include_empty: 
            raise ValueError("cannot call count if include_empty = True")

    #filters

    def name(self, name:str):
        return self._filter(lambda c: c.name_id == name)
    
    
    #results
    
    def exists(self):
        return len(self._cards_spaces) > 0
    
    
    
    def count(self):
        return len(self._cards_spaces)
    
    def al_least(self, n:int):
        return (self.count() >= n) 
    
    def cards(self):
        result = []

        for card in self._cards_spaces:
            result.append(card.get_card())
        return result