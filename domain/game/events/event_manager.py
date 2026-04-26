from .event import Event

"""
	Esta clase es la implementacion del patron observer    
	
"""
class EventManager:

	def __init__(self):
		self.listeners = {}
    
	def subscribe(self, event_type, callback):
		if event_type not in self.listeners:
			self.listeners[event_type] = []
		self.listeners[event_type].append(callback)

	def unsubscribe(self, event_type, callback):
		if event_type in self.listeners:
			self.listeners[event_type].remove(callback)
			
			if not self.listeners[event_type]:
				del self.listeners[event_type]


	def emit(self, event: Event):
		event_type = type(event)

		if event_type in self.listeners:
			for callback in self.listeners[event_type]:
				callback(event)

		