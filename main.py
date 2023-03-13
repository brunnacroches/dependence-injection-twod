from src.people import Person
from src.action.speak import StartTalk
from src.action.run import MakeRun

pessoa1 = Person(StartTalk())
pessoa1.performAction()

pessoa2 = Person(MakeRun())
pessoa2.performAction()