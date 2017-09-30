import pygame

pygame.init()

#setting up the window

gameDisplay = pygame.display.set_mode((800,600))

#game title

pygame.display.set_caption('Endless Game')


#Game clock

clock = pygame.time.Clock()


#Game Loop(ends and continues the game)

dies = False

while not dies:

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            dies = True

            print(event)

#Update display, update(can update 1 parameter, or all)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
