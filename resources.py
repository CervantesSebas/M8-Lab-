#Sebastian Cervantes 
#November 12, 2024 

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses
    def get_model(self):
        return self.nickname
    def get_year(self):
        return self.weapons
    def get_color(self):
        return self. weaknesses
    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
    
#End of class, beginning of test code    
player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['paper', 'idea', 'rope']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

Sebas = character("Sebas",['rope','pen','paper','idea'],['slow','confusion'])
print (f"my weapons are {Sebas.weapons}")
