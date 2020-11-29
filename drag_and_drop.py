import pygame

pygame.init()
screen = pygame.display.set_mode([400, 600])
pygame.display.set_caption("Drag n Drop")
clock = pygame.time.Clock()

rectangle = pygame.rect.Rect(176, 134, 17, 17)
rectangle_dragging = False

screen_alive = True

while screen_alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_alive = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle.collidepoint(event.pos):
                    rectangle_dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if rectangle_dragging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y

    screen.fill([50, 50, 50])

    pygame.draw.rect(screen, 'blue', rectangle)

    pygame.display.update()
    clock.tick(30)

print(screen_alive)
pygame.quit()
