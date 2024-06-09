import pygame 
import sys
from random import randrange

mainchar = pygame.image.load("AnimationSheet(idle).png")
 
pygame.init()  
pygame.font.init()

running = True

x = 0
y = 515
z = 0
p = 0
#print(pygame.font.get_fonts()) for full font list

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        else:
            screen = pygame.display.set_mode([1023, 765]) 

            pygame.display.set_caption('Save the Princess!')
            colour = (255,153,255)
            speaking = (0,0,0)

            screen.fill(colour)
            
            font1 = pygame.font.SysFont("comicsansms", 50, bold = True)
            font2 = pygame.font.SysFont("comicsansms", 32, bold = True)
            font3 = pygame.font.SysFont("comicsansms", 23)
            font4 = pygame.font.SysFont("comicsansms", 23)
            font5 = pygame.font.SysFont("comicsansms", 50)

            text1 = font1.render('Save the Princess!', True, "white", colour)
            textRect1 = text1.get_rect()
            textRect1.center = (510, 200)
            screen.blit(text1, textRect1)

            text2 = font1.render("Press Space To Play!", True, "White", colour)
            textRect2 = text2.get_rect()
            textRect2.center = (510, 400)
            screen.blit(text2, textRect2)

            text3 = font2.render("Disclaimer: When Starting, You Cannot Exit!", True, "White", colour)
            textRect3 = text3.get_rect()
            textRect3.center = (510, 600)
            screen.blit(text3, textRect3)

            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                change = True
                while(change):
                    image1 = pygame.image.load("155962.png")
                    screen.blit(image1, (0,0))
                    king = pygame.image.load("king_character.png") 
                    mainchar = pygame.transform.scale(mainchar, (300,400))
                    screen.blit(king, (450, 250))
                    screen.blit(mainchar, (200, 350))
                    pygame.display.flip()
                    kingtext1 = font3.render("Help!", True, "White", speaking)
                    kingtext2 = font3.render("My daughter has been kidnapped! Save her please!", True, "White", speaking)
                    
                    kingtextRect1 = kingtext1.get_rect()
                    kingtextRect1.center = (600, 300)
                    screen.blit(kingtext1, kingtextRect1)
                    pygame.display.update()
                    pygame.time.wait(2000)

                    kingtextRect2 = kingtext2.get_rect()
                    kingtextRect2.center = (600, 300)
                    screen.blit(kingtext2, kingtextRect2)
                    pygame.display.update()
                    pygame.time.wait(2000)

                    image1 = pygame.image.load("155962.png")
                    screen.blit(image1, (0,0))
                    king = pygame.image.load("king_character.png")
                    mainchar = pygame.image.load("AnimationSheet(idle).png")
                    mainchar = pygame.transform.scale(mainchar, (300,400))
                    screen.blit(king, (450, 250))
                    screen.blit(mainchar, (200, 350))
                    pygame.display.flip()

                    mainchartext1 = font3.render("Of course! She will be home, you have my word", True, "white", speaking)
                    mainchartextRect1 = mainchartext1.get_rect()
                    mainchartextRect1.center = (300, 400)
                    screen.blit(mainchartext1, mainchartextRect1)
                    pygame.display.update()
                    pygame.time.wait(2000)

                    image1 = pygame.image.load("155962.png")
                    screen.blit(image1, (0,0))
                    king = pygame.image.load("king_character.png")
                    mainchar = pygame.image.load("AnimationSheet(idle).png")
                    mainchar = pygame.transform.scale(mainchar, (300,400))
                    screen.blit(king, (450, 250))
                    screen.blit(mainchar, (200, 350))
                    pygame.display.flip()

                    while(change):
                        image2 = pygame.image.load("Background_01.png")
                        image2 = pygame.transform.scale(image2, (1023,765))
                        screen.blit(image2, (0,0))
                        wall_c = pygame.image.load("Wall_C_02.png")
                        roof_b4 = pygame.image.load("Roof_B_04.png")
                        roof_b5 = pygame.image.load("Roof_B_05.png")
                        door = pygame.image.load("Door_03.png")
                        screen.blit(wall_c, (200, 445))
                        screen.blit(wall_c, (500, 445))
                        screen.blit(roof_b5, (160, 310))
                        screen.blit(roof_b4, (510, 310))
                        screen.blit(door, (450, 515))
                        mainchar = pygame.image.load("AnimationSheet(idle).png")
                        mainchar = pygame.transform.scale(mainchar, (200,300))
                        screen.blit(mainchar, (0,515))
                        pygame.display.update()
                    
                        while(change):
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    image2 = pygame.image.load("Background_01.png")
                                    image2 = pygame.transform.scale(image2, (1023,765))
                                    screen.blit(image2, (0,0))
                                    wall_c = pygame.image.load("Wall_C_02.png")
                                    roof_b4 = pygame.image.load("Roof_B_04.png")
                                    roof_b5 = pygame.image.load("Roof_B_05.png")
                                    door = pygame.image.load("Door_03.png")
                                    screen.blit(wall_c, (200, 445))
                                    screen.blit(wall_c, (500, 445))
                                    screen.blit(roof_b5, (160, 310))
                                    screen.blit(roof_b4, (510, 310)) 
                                    screen.blit(door, (450, 515))
                                    pygame.display.flip()
                                    clue = font4.render("Go to the forest! -->", True, "white", speaking)
                                    clueRect1 = clue.get_rect()
                                    clueRect1.center = (511.5,200)
                                    screen.blit(clue, clueRect1)
                                    pygame.display.update() 
                                    if event.key == pygame.K_LEFT:
                                        x -= 30
                                        screen.blit(mainchar, (x,y))
                                    elif event.key == pygame.K_RIGHT:
                                        x += 30
                                        screen.blit(mainchar, (x,y))
                                    pygame.display.update()    
                                        
                                    while(x>=1000):
                                        y = 300
                                        image3 = pygame.image.load("game_background_2.png")
                                        image3 = pygame.transform.scale(image3, (1023,765))
                                        screen.blit(image3,(0,0))
                                        mainchar = pygame.image.load("AnimationSheet(idle).png")
                                        mainchar = pygame.transform.scale(mainchar, (200,300))
                                        screen.blit(mainchar, (0,y))
                                        scarf = pygame.image.load("SCARF.png")
                                        scarf = pygame.transform.scale(scarf, (70,170))
                                        screen.blit(scarf, (300,y))
                                        pygame.display.update()

                                        while(change):    
                                            for event in pygame.event.get():
                                                if event.type == pygame.KEYDOWN:
                                                    image3 = pygame.image.load("game_background_2.png")
                                                    image3 = pygame.transform.scale(image3, (1023,765))
                                                    screen.blit(image3,(0,0))
                                                    scarf = pygame.image.load("SCARF.png")
                                                    scarf = pygame.transform.scale(scarf, (70,170))
                                                    screen.blit(scarf, (300,y))
                                                    pygame.display.flip()
                                                    if event.key == pygame.K_LEFT:
                                                        z -= 30
                                                        screen.blit(mainchar, (z,y))
                                                        pygame.display.update() 
                                                    elif event.key == pygame.K_RIGHT:
                                                        z += 30
                                                        screen.blit(mainchar, (z,y))
                                                    pygame.display.update() 

                                                if z == 300:
                                                    clue2 = font4.render("The princess' scarf...she must be close!", True, "white", speaking)
                                                    clueRect2 = clue.get_rect()
                                                    clueRect2.center = (511.5,200)
                                                    screen.blit(clue2, clueRect2)
                                                    pygame.display.update() 

                                                while(z>=1000): #p is our x now
                                                    y = 220
                                                    image4 = pygame.image.load("game_background_4.png")
                                                    image4 = pygame.transform.scale(image4, (1023,765))
                                                    screen.blit(image4, (0,0))
                                                    wall_a = pygame.image.load("Wall_A_02.png")
                                                    screen.blit(wall_a, (900,140))
                                                    screen.blit(wall_a, (900,-15))
                                                    door = pygame.image.load("Door_03.png")
                                                    screen.blit(door, (900, 200))
                                                    mainchar = pygame.image.load("AnimationSheet(idle).png")
                                                    mainchar = pygame.transform.scale(mainchar, (200,300))
                                                    screen.blit(mainchar, (0,y))
                                                    pygame.display.update()
                                                    
                                                    while(change):
                                                        for event in pygame.event.get():
                                                            if event.type == pygame.KEYDOWN:
                                                                image4 = pygame.image.load("game_background_4.png")
                                                                image4 = pygame.transform.scale(image4, (1023,765))
                                                                screen.blit(image4, (0,0))
                                                                wall_a = pygame.image.load("Wall_A_02.png")
                                                                screen.blit(wall_a, (900,140))
                                                                screen.blit(wall_a, (900,-15))
                                                                door = pygame.image.load("Door_03.png")
                                                                screen.blit(door, (900, 200))
                                                                pygame.display.flip()
                                                                if event.key == pygame.K_LEFT:
                                                                    p -= 30
                                                                    screen.blit(mainchar, (p,y))
                                                                    pygame.display.update() 
                                                                elif event.key == pygame.K_RIGHT:
                                                                    p += 30
                                                                    screen.blit(mainchar, (p,y))
                                                                pygame.display.update() 
                                                            if p > 880:
                                                                clue3 = font4.render("HELP!", True, "white", speaking)
                                                                clueRect3 = clue3.get_rect()
                                                                clueRect3.center = (950, 140)
                                                                screen.blit(clue3, clueRect3)
                                                                pygame.display.update()
                                                                castle = pygame.image.load("game_background_3.png")
                                                                castle = pygame.transform.scale(castle, (1023,765))
                                                                pygame.time.wait(2000)
                                                                screen.blit(castle, (0,0))
                                                                pygame.display.update() 

                                                                while(change):
                                                                    castle = pygame.image.load("game_background_3.png")
                                                                    castle = pygame.transform.scale(castle, (1023,765))
                                                                    screen.blit(castle, (0,0))
                                                                    mainchar = pygame.image.load("AnimationSheet(idle).png")
                                                                    mainchar = pygame.transform.scale(mainchar, (200,300))
                                                                    screen.blit(mainchar, (30, 200))
                                                                    villain = pygame.image.load("VILLAIN.png")
                                                                    villain = pygame.transform.scale(villain, (200,300))
                                                                    screen.blit(villain, (600, 200))
                                                                    princess = pygame.image.load("PRINCESS.png")
                                                                    princess = pygame.transform.scale(princess, (200,300))
                                                                    screen.blit(princess, (800, 200))
                                                                    pygame.display.update()

                                                                    text4 = font3.render("If you want the princess back, you must roll the dice!", True, "white", speaking)
                                                                    text4Rect1 = text4.get_rect()
                                                                    text4Rect1.center = (600, 190)
                                                                    screen.blit(text4, text4Rect1)
                                                                    pygame.time.wait(2000)
                                                                    pygame.display.update()
                                                                    pygame.time.wait(4000)

                                                                    dice_roll = randrange(1,10)
                                                                    villain = randrange(1,10)

                                                                    if dice_roll > villain: 
                                                                        castle = pygame.image.load("game_background_3.png")
                                                                        castle = pygame.transform.scale(castle, (1023,765))
                                                                        screen.blit(castle, (0,0))
                                                                        mainchar = pygame.image.load("AnimationSheet(idle).png")
                                                                        mainchar = pygame.transform.scale(mainchar, (200,300))
                                                                        screen.blit(mainchar, (30, 200))
                                                                        villain = pygame.image.load("VILLAIN.png")
                                                                        villain = pygame.transform.scale(villain, (200,300))
                                                                        screen.blit(villain, (600, 200))
                                                                        princess = pygame.image.load("PRINCESS.png")
                                                                        princess = pygame.transform.scale(princess, (200,300))
                                                                        screen.blit(princess, (800, 200))
                                                                        win = font3.render("I see you have bettered me, I shall leave you both.", True, "white", speaking)
                                                                        winRect1 = win.get_rect()
                                                                        winRect1.center = (600,190)
                                                                        screen.blit(win,winRect1)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(2000)

                                                                        y = 220
                                                                        image4 = pygame.image.load("game_background_4.png")
                                                                        image4 = pygame.transform.scale(image4, (1023,765))
                                                                        screen.blit(image4, (0,0))
                                                                        wall_a = pygame.image.load("Wall_A_02.png")
                                                                        screen.blit(wall_a, (900,140))
                                                                        screen.blit(wall_a, (900,-15))
                                                                        door = pygame.image.load("Door_03.png")
                                                                        screen.blit(door, (900, 200))
                                                                        mainchar = pygame.image.load("AnimationSheet(idle).png")
                                                                        mainchar = pygame.transform.scale(mainchar, (200,300))
                                                                        screen.blit(mainchar, (100,y))
                                                                        princess = pygame.image.load("PRINCESS.png")
                                                                        princess = pygame.transform.scale(princess, (200,300))
                                                                        screen.blit(princess, (300, y))
                                                                        pygame.display.update()
                                                                        text5 = font3.render("Thank you!", True, "white", speaking)
                                                                        text5Rect1 = text5.get_rect()
                                                                        text5Rect1.center = (400, 240)
                                                                        screen.blit(text5,text5Rect1)
                                                                        pygame.time.wait(2000)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(2000)

                                                                        screen.fill("black")
                                                                        ending1 = font5.render("Winner!", True, "White", speaking)
                                                                        ending1Rect1 = ending1.get_rect()
                                                                        ending1Rect1.center = (511.5, 200)
                                                                        screen.blit(ending1,ending1Rect1)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(2000)

                                                                    else:
                                                                        castle = pygame.image.load("game_background_3.png")
                                                                        castle = pygame.transform.scale(castle, (1023,765))
                                                                        screen.blit(castle, (0,0))
                                                                        mainchar = pygame.image.load("AnimationSheet(idle).png")
                                                                        mainchar = pygame.transform.scale(mainchar, (200,300))
                                                                        screen.blit(mainchar, (30, 200))
                                                                        villain = pygame.image.load("VILLAIN.png")
                                                                        villain = pygame.transform.scale(villain, (200,300))
                                                                        screen.blit(villain, (600, 200))
                                                                        princess = pygame.image.load("PRINCESS.png")
                                                                        princess = pygame.transform.scale(princess, (200,300))
                                                                        screen.blit(princess, (800, 200))
                                                                        text6 = font3.render("Haha! I have won, you cannot stop me!", True, "White", speaking)
                                                                        text6Rect1 = text6.get_rect()
                                                                        text6Rect1.center = (600,190)
                                                                        screen.blit(text6,text6Rect1)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(2000)
                                                                        
                                                                        screen.fill("black")
                                                                        ending2 = font5.render("Loser!", True, "white", speaking)
                                                                        ending2Rect1 = ending2.get_rect()
                                                                        ending2Rect1.center = (511.5, 200)
                                                                        screen.blit(ending2,ending2Rect1)
                                                                        pygame.time.wait(2000)
                                                                        pygame.display.update()
                                                                        pygame.time.wait(2000)
                                                                    pygame.quit()