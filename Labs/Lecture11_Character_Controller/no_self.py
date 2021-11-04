class Star:

    type = 'Star'
    x = 100

    def change():
        x = 200
        print('x is ', x)

class Player:
    type = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

print('x IS ', Star.x) # OK
Star.change() # OK
print('x IS ', Star.x)

star = Star() # OK
print('x IS ', star.x) # OK
star.change() # Error

player = Player()
player.where()

# 클래스 변수 사용
print(Player.type)

# 클래스 함수 호출
Player.where() # error
Player.where(player) # OK, player.where()과 같음