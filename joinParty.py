class NaijaParty():

    def __init__(self, name):
        self.party = []
        self.name = name
        
    
    def membership(self, decamp):
        self.party.append(decamp)

member1 = NaijaParty('tunde')
member1.membership('pdp')
member2 = NaijaParty('kola')
member2.membership('pdp')

print(member1.name)
