import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
game = "ready"
game_type = "ready"
icon = pygame.image.load("ping-pong.png")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, 12)
pygame.display.set_caption("pong")
pygame.display.set_icon(icon)
music = pygame.mixer.music.load("Retro-style-synth-music-loop.mp3")
pygame.mixer.music.play(-1)

ball = pygame.Rect(685, 355, 30, 30)
player = pygame.Rect(6, 300, 20, 183)
oponent = pygame.Rect(1340, 300, 20, 203)
line = (705, 0)
endpose = (705, 800)

color = (255, 255, 255)
play = "on"
plays = "run"

position = (655, 20)


def ball_position():
    global ball_speedY, ball_speedX, score_timer, position
    ball.x = 685
    ball.y = 355

    current_timer = pygame.time.get_ticks()
    if current_timer - score_timer < 700:
        three = player_font.render("3", True, black)
        screen.blit(three, position)
    if 700 < current_timer - score_timer < 1400:
        two = player_font.render("2", True, black)
        screen.blit(two, position)
    if 1400 < current_timer - score_timer < 2100:
        one = player_font.render("1", True, black)
        screen.blit(one, position)

    if current_timer - score_timer < 2100:
        ball_speedX = 0
        ball_speedY = 0
    else:
        ball_speedX = 9 * random.choice((1, -1))
        ball_speedY = 9 * random.choice((1, -1))
        score_timer = None


ball_speedX = -9
ball_speedY = 9
playerY_change = 0

opponentY_change = int(10.8)

player_score = 0
player_font = pygame.font.Font("Cartoon cookies.ttf", 100)
player_fontX = 350
player_fontY = 20
black = (255, 255, 255)

oponent_score = 0
oponent_font = pygame.font.Font("Cartoon cookies.ttf", 100)
oponent_fontX = 990
oponent_fontY = 20

game_font = pygame.font.Font("Cartoon cookies.ttf", 230)
game_fontX = 460
game_fontY = -1200

game_font2 = pygame.font.Font("Cartoon cookies.ttf", 100)
game_fontX2 = 460
game_fontY2 = -1200

game_font3 = pygame.font.Font("Cartoon cookies.ttf", 50)
game_fontX3 = 460
game_fontY3 = -1200

won_font = pygame.font.Font("Cartoon cookies.ttf", 230)
won_fontX = 460
won_fontY = -1200

lost_font = pygame.font.Font("Cartoon cookies.ttf", 230)
lost_fontX = 460
lost_fontY = -1200

sound = pygame.mixer.Sound("ping_pong_8bit_plop.ogg")


def game_start(x, y):
    gaming = game_font.render("PONG", True, black)
    screen.blit(gaming, (x, y))


def game_start2(x, y):
    gaming2 = game_font2.render("START", True, black)
    screen.blit(gaming2, (x, y))


def game_won(x, y):
    gaming_won = won_font.render(" YOU WON ", True, black)
    screen.blit(gaming_won, (x, y))


def game_lost(x, y):
    gaming_lost = lost_font.render("YOU LOST ", True, black)
    screen.blit(gaming_lost, (x, y))


def game_start3(x, y):
    gaming3 = game_font3.render("click 'SPACE' key to ", True, black)
    screen.blit(gaming3, (x, y))


def score_1(x, y):
    scoring = player_font.render(str(player_score), True, black)
    screen.blit(scoring, (x, y))


def score_2(x, y):
    scoring2 = oponent_font.render(str(oponent_score), True, black)
    screen.blit(scoring2, (x, y))


background = (65, 65, 155)

score_timer = None

while True:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerY_change += 10
            if event.key == pygame.K_UP:
                playerY_change -= 10
            if event.key == pygame.K_SPACE:
                if play == "off":
                    ball.x, ball.y = 700, 355
                    player.x, player.y = 6, 300
                    oponent.x, oponent.y = 1340, 300
                    line = (705, 0)
                    endpose = (705, 800)
                    play = "running"
                    player_fontX, player_fontY = 350, 20
                    oponent_fontX, oponent_fontY = 990, 20
                    ball_speedX = 9 * random.choice((1, -1))
                    ball_speedY = 9 * random.choice((1, -1))
                    game_fontY, game_fontX = -1200, 460
                    game_fontY2, game_fontX2 = -1200, 460
                    game_fontY3, game_fontX3 = -1200, 460
            if plays == "won":
                if event.key == pygame.K_SPACE:
                    won_fontX, won_fontY = 100, -900
                    game_fontY, game_fontX = -1200, 460
                    game_fontY2, game_fontX2 = -1200, 460
                    game_fontY3, game_fontX3 = -1200, 460
                    ball.x, ball.y = 700, 355
                    player.x, player.y = 6, 300
                    oponent.x, oponent.y = 1340, 300
                    line = (705, 0)
                    endpose = (705, 800)
                    player_fontX, player_fontY = 350, 20
                    oponent_fontX, oponent_fontY = 990, 20
                    ball_speedX = 9 * random.choice((1, -1))
                    ball_speedY = 9 * random.choice((1, -1))
                    oponent_score = 0
                    player_score = 0
            if plays == "lost":
                if event.key == pygame.K_SPACE:
                    lost_fontX, lost_fontY = 100, -900
                    game_fontY, game_fontX = -1200, 460
                    game_fontY2, game_fontX2 = -1200, 460
                    game_fontY3, game_fontX3 = -1200, 460
                    ball.x, ball.y = 700, 355
                    player.x, player.y = 6, 300
                    oponent.x, oponent.y = 1340, 300
                    line = (705, 0)
                    endpose = (705, 800)
                    player_fontX, player_fontY = 350, 20
                    oponent_fontX, oponent_fontY = 990, 20
                    ball_speedX = 9 * random.choice((1, -1))
                    ball_speedY = 9 * random.choice((1, -1))
                    oponent_score = 0
                    player_score = 0
            if event.key == pygame.K_9:
                background = (0, 65, 0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerY_change -= 10
            if event.key == pygame.K_UP:
                playerY_change += 10
            if event.key == pygame.K_9:
                background = (0, 65, 0)
            if event.key == pygame.K_8:
                background = (0, 0, 65)
            if event.key == pygame.K_0:
                background = (65, 65, 155)
            if event.key == pygame.K_1:
                background = (205, 92, 92)
            if event.key == pygame.K_2:
                background = (255, 165, 0)
            if event.key == pygame.K_3:
                background = (205, 205, 0)
            if event.key == pygame.K_4:
                background = (0, 0, 0)
            if event.key == pygame.K_5:
                background = (255, 255, 255)
                color = (0, 0, 0)
                black = (0, 0, 0)
            else:
                color = (255, 255, 255)
                black = (255, 255, 255)
            if event.key == pygame.K_6:
                background = (128, 128, 128)
            if event.key == pygame.K_7:
                background = (0, 255, 127)

    # ball AI
    ball.x += ball_speedX
    ball.y += ball_speedY

    if ball.colliderect(player) or ball.colliderect(oponent):
        pygame.mixer.Sound.play(sound)
        ball_speedX *= -1
        ball_speedY *= 1

    if ball.left <= 0:
        score_timer = pygame.time.get_ticks()
        pygame.mixer.Sound.play(sound)
        oponent_score += 1

    if ball.right >= 1360:
        score_timer = pygame.time.get_ticks()
        pygame.mixer.Sound.play(sound)
        player_score += 1

    if ball.top <= 0 or ball.bottom >= 765:
        ball_speedY *= -1
        pygame.mixer.Sound.play(sound)

    # player AI
    if player.top <= 5:
        player.y = 5
    if player.bottom >= 765:
        player.y = 585
    player.y += playerY_change

    # opponent AI
    if oponent.top >= ball.y:
        oponent.y -= opponentY_change
    if oponent.bottom <= ball.y:
        oponent.y += opponentY_change

    if oponent.top <= 25:
        oponent.y = 25
    if oponent.bottom >= 765:
        oponent.y = 590

    if score_timer:
        ball_position()

    if player_score == 0 and game_type == "ready":
        ball.x, ball.y = 600, 240
        player.x, player.y = -100, 0
        oponent.x, oponent.y = -1000, 0
        line, endpose = (-50, -1000), (-50, 800)
        player_fontX, player_fontY = 700, -10000
        oponent_fontX, oponent_fontY = 700, -10000
        pygame.mixer.music.play(-1)
        game_fontX = 440
        game_fontY = 120
        game_fontX2 = 770
        game_fontY2 = 600
        game_fontX3 = 345
        game_fontY3 = 633
        ball_speedX = 0
        ball_speedY = 0
        won_fontX = 0
        won_fontY = -1000
        game_type = " not ready"
        play = "off"

    if player_score == 5:
        ball.x, ball.y = 300, -10000
        player.x, player.y = -100, 0
        oponent.x, oponent.y = -100, 0
        line, endpose = (-50, -1000), (-50, 800)
        player_fontX, player_fontY = 700, -10000
        oponent_fontX, oponent_fontY = 700, -10000
        ball_speedX = 0
        ball_speedY = 0
        won_fontX = 240
        won_fontY = 120
        game_fontY, game_fontX = -1200, 460
        position = (655, 20)
        game_fontX2 = 770
        game_fontY2 = 600
        game_fontX3 = 345
        game_fontY3 = 633
        game_type = " not ready"
        plays = "won"
        play = "off"

    if oponent_score == 5:
        ball.x, ball.y = 300, -10000
        player.x, player.y = -100, 0
        oponent.x, oponent.y = -100, 0
        line, endpose = (-50, -1000), (-50, 800)
        player_fontX, player_fontY = 700, -10000
        oponent_fontX, oponent_fontY = 700, -10000
        ball_speedX = 0
        ball_speedY = 0
        lost_fontX = 240
        lost_fontY = 120
        game_fontX2 = 770
        game_fontY2 = 600
        game_fontX3 = 345
        game_fontY3 = 633
        game_fontY, game_fontX = -1200, 460
        position = (655, 20)
        game_type = " not ready"
        play = "off"
        plays = "lost"

    # animation

    pygame.draw.rect(screen, color, player)
    pygame.draw.rect(screen, color, oponent)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.aaline(screen, color, line, endpose)

    # score function
    score_1(player_fontX, player_fontY)
    score_2(oponent_fontX, oponent_fontY)
    game_start(game_fontX, game_fontY)
    game_start2(game_fontX2, game_fontY2)
    game_start3(game_fontX3, game_fontY3)
    game_won(won_fontX, won_fontY)
    game_lost(lost_fontX, lost_fontY)
    pygame.display.flip()
    clock.tick(100)
