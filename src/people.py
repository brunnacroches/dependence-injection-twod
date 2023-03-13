class Person:
    def __init__(self, behavior):
        self.behavior = behavior 
        
    def performAction(self):
        self.behavior.action()


# This means that when we instantiate a Person class, it will be 
# # dependent on a certain behavior.


# Isso quer dizer que quando a gente instanciar uma classe Pessoa, ela vai ser
# dependente de um certo comportamento.