from juego.game import Game

game = Game()

while True:
    game.all_events()
    game.update()
    game.draw()
