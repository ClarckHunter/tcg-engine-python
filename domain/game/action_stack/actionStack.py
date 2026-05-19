from .action import Action

class ActionStack:
    def __init__(self):
        self._stack = []

    def push(self, action:Action)->None:
        self._stack.append(action)

    def pop(self)->Action:
        return self._stack.pop()
    
    def peek(self)->Action:
        return self._stack[-1] if self._stack else None
    
    def empty(self)->bool:
         return len(self._stack) == 0
    
    def clear(self)->None:
        self._stack.clear()

    