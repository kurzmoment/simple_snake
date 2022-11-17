import pygame as pg


# INITIALIZATION
pg.init()
WIDTH, HEIGHT = 1024, 768
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
SCORE_FONT = pg.font.SysFont('Fixedsys Excelsior 3.01', 25)
pg.display.set_caption("Snake")


class Snake:
    COLOR = WHITE
    VEL = 20

    def __init__(self, x, y, height, width):
        self.x = self.starting_x = x
        self.y = self.starting_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pg.draw.rect(win, self.COLOR, (self.x, self.y,
                     self.height, self.width))

    def move(self, keys):
        pass

    def reset(self):
        self.x = self.starting_x
        self.y = self.starting_y


class Food:
    def __init__(self):
        pass

    def draw(self):
        pass


def draw(win, snake, score):
    win.fill(BLACK)
    snake.draw(win)
    game_title = SCORE_FONT.render(f"Score: {score}", 1, WHITE)
    win.blit(game_title, (WIDTH // 2 - game_title.get_width()//2, 20))
    pg.display.update()


def snake_movement(snake, keys):
    if keys[pg.K_UP]:
        pass
    if keys[pg.K_DOWN]:
        pass
    if keys[pg.K_LEFT]:
        pass
    if keys[pg.K_RIGHT]:
        pass


def main():
    going = True
    clock = pg.time.Clock()
    snake = Snake(WIDTH // 2, HEIGHT//2, 22, 22)
    score = 0
    print(snake)
    while going:
        clock.tick(FPS)
        draw(WINDOW, snake, score)
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False


if __name__ == "__main__":
    main()
