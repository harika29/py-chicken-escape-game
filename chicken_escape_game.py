import pygame
import random

pygame.init()
screen_width = 350
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Chicken crash by Harika")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 15)
score = 0
lives = 3


def display_lives(lives):
    lives_text = 'Lives: ' + str(lives)
    lives_img = font.render(lives_text, True, 'orange')
    screen.blit(lives_img, [280, 10])


def display_score(score):
    score_text = 'Score: ' + str(score)
    text_img = font.render(score_text, True, 'green')
    screen.blit(text_img, [20, 10])


def image_load(image_filename):
    return pygame.image.load(image_filename)


def random_offset():
    return -1 * random.randint(100, 1000)  # returning a random negative num to start chicken from above the screen


def update_chicken_pos(index, chicken_y):
    global score
    if chicken_y[index] > 600:
        chicken_y[index] = random_offset()
        score += 10
    else:
        chicken_y[index] += 5


def crashed(index, chicken_y, user_x):
    global lives
    chicken_y[index] = random_offset()
    lives = lives - 1


def display_message(message, color, x_coord, y_coord):
    message = font.render(message, True, color)
    screen.blit(message, [x_coord, y_coord])


def chicken_escape():
    global score, lives
    score = 0
    lives = 3
    screen_alive = True
    game_alive = True

    chicken_y = [random_offset(), random_offset(), random_offset()]
    user_x = 140

    while screen_alive:
        while not game_alive:
            screen.fill('white')
            display_message("Your Score: " + str(score), 'red', 120, 100)
            display_message("Press Q:Quit or R:Retry", 'red', 100, 120)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen_alive = False
                    game_alive = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        screen_alive = False
                        game_alive = True
                    if event.key == pygame.K_r:
                        chicken_escape()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_alive = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and user_x < 290:
                    user_x = user_x + 10
                if event.key == pygame.K_LEFT and user_x > 0:
                    user_x = user_x - 10

        update_chicken_pos(0, chicken_y)
        update_chicken_pos(1, chicken_y)
        update_chicken_pos(2, chicken_y)

        screen.blit(image_load('background.png'), [0, 0])  # load background on screen
        screen.blit(image_load('user1.png'), [user_x, 540])  # load user image on screen
        screen.blit(image_load('chicken.png'), [0, chicken_y[0]])  # load chicken image on screen
        screen.blit(image_load('chicken.png'), [135, chicken_y[1]])  # x-coord remain same throughout the game for chicken
        screen.blit(image_load('chicken.png'), [270, chicken_y[2]])

        if user_x < 80 and chicken_y[0] > 460:
            crashed(0, chicken_y, user_x)

        if 80 < user_x < 210 and chicken_y[1] > 460:
            crashed(1, chicken_y, user_x)

        if user_x > 210 and chicken_y[2] > 460:
            crashed(2, chicken_y, user_x)

        if lives <= 0:
            game_alive = False

        display_score(score)
        display_lives(lives)

        pygame.display.update()
        clock.tick(50)

    pygame.quit()


chicken_escape()
