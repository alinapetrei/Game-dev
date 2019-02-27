import pygame

pygame.init()


class Game:
    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height
        self.window = pygame.display.set_mode((width, height))
        self.old_positions = []

    @staticmethod
    def set_title(title):
        pygame.display.set_caption(title)

    def run(self):
        x = 50
        y = 50
        width = 40
        height = 60
        speed = 20
        isJump = False
        jumpCount = 10

        run = True
        while run:
            pygame.time.delay(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and x > speed:
                x -= speed
            if keys[pygame.K_RIGHT] and x < self.window_width - width - speed:
                x += speed
            if not isJump:
                if keys[pygame.K_UP] and y > speed:
                    y -= speed
                if keys[pygame.K_DOWN] and y < self.window_height - height - speed:
                    y += speed
                if keys[pygame.K_SPACE]:
                    isJump = True
            else:
                if jumpCount >= -10:
                    neg = 1
                    if jumpCount < 0:
                        neg = -1
                    y -= (jumpCount ** 2) * 0.5 * neg
                    if -2 <= jumpCount <= 2:
                        jumpCount = -3
                    else:
                        jumpCount -= 1
                else:
                    isJump = False
                    jumpCount = 10

            self.window.fill((0, 0, 0))

            pygame.draw.rect(self.window, (255, 0, 0), (x, y, width, height))

            pygame.display.update()

            #self.old_positions = [x, y]


game = Game(500, 500)
game.set_title("My first game")
game.run()