import pygame
import random

def main():
    pygame.init()
    surfaceSizeX = 770
    surfaceSizeY = 250
    clock = pygame.time.Clock()
    mainSurface = pygame.display.set_mode((surfaceSizeX, surfaceSizeY))
    #source: https://salepubsm.live/product_details/47215072.html
    background = pygame.image.load("images/background.png")
    #source: https://github.com/topics/chrome-dino
    dino_char_select = pygame.image.load("images/char_select_dino.png")
    dino_char_select = pygame.transform.scale(dino_char_select, (100,100))
    #source: https://dinosaurgames.io/
    cactus1 = pygame.image.load("images/cactus1.png")
    cactus1 = pygame.transform.scale(cactus1, (25, 35))
    #source: https://deejaygraham.github.io/2020/07/14/trex-runner-in-scratch/
    cactus2 = pygame.image.load("images/cactus2.png")
    cactus2 = pygame.transform.scale(cactus2, (25, 35))
    #source: https://medium.com/@jmfleeno/how-to-code-your-dino-game-6f08bfe8bea7
    cactus3 = pygame.image.load("images/cactus3.png")
    cactus3 = pygame.transform.scale(cactus3, (38,48))
    #source: https://www.businessinsider.com/google-chrome-easter-egg-t-rex-mini-game-2014-9
    gameover = pygame.image.load("images/gameover.png")
    gameover = pygame.transform.scale(gameover, (172, 147))
    #source: 
    start_screen = pygame.image.load("images/start.jpg")
    start_screen = pygame.transform.scale(start_screen, (772, 250))
    #source: https://www.istockphoto.com/hk/%E5%90%91%E9%87%8F/wooden-game-play-button-vector-gm1440133517-480203570
    play_button = pygame.image.load("images/play.png")
    play_button = pygame.transform.scale(play_button, (125, 90))
    #source: https://www.magwest.org/2023-performers/2023/6/5/character-select 
    char_select = pygame.image.load("images/char_select.png")
    char_select = pygame.transform.scale(char_select, (125, 90))
    #source: https://dribbble.com/tags/character-select
    char_select_bg = pygame.image.load("images/char_select_bg.jpg")
    char_select_bg = pygame.transform.scale(char_select_bg, (772, 250))
    #source: https://gifer.com/en/gifs/sonic
    sonic = pygame.image.load("images/sonic.png")
    sonic_char_select = pygame.transform.scale(sonic, (100,100))
    back = pygame.image.load("images/backbutton.png")
    back = pygame.transform.scale(back, (50,50))
    spriteSheet = pygame.image.load("images/spriteSheetdino.png")
    #source: https://www.sonicgalaxy.net/sprites-gen-sonic/
    sonicspriteSheet = pygame.image.load("images/sonicspriteSheet.png")
    # https://pngtree.com/freepng/game-wood-and-gold-ui-menu_7425455.html
    difficultybutton = pygame.image.load("images/difficulty_button.png")
    difficultybutton = pygame.transform.scale(difficultybutton, (75,40))
    #source: https://pngtree.com/freepng/game-wood-and-gold-ui-menu_7425455.html
    easybutton = pygame.image.load("images/easybutton.png")
    easybutton = pygame.transform.scale(easybutton, (75,40))
    #source: https://pngtree.com/freepng/game-wood-and-gold-ui-menu_7425455.html
    mediumbutton = pygame.image.load("images/mediumbutton.png")
    mediumbutton = pygame.transform.scale(mediumbutton, (75,40))
    #source: https://pngtree.com/freepng/game-wood-and-gold-ui-menu_7425455.html
    hardbutton = pygame.image.load("images/hardbutton.png")
    hardbutton = pygame.transform.scale(hardbutton, (75,40))
    #source: https://en.wikipedia.org/wiki/File:Difficulty_level_selection.png
    difficultystatebg = pygame.image.load("images/difficultystatebg.png")
    difficultystatebg = pygame.transform.scale(difficultystatebg, (770, 250))
    #source: https://www.vecteezy.com/free-vector/wood-button
    helpbutton = pygame.image.load("images/helpbutton.png")
    helpbutton = pygame.transform.scale(helpbutton, (75,45))
    #source: https://www.vecteezy.com/free-vector/game-ui-background
    helpstatebg = pygame.image.load("images/helpstatebg.jpg")
    helpstatebg = pygame.transform.scale(helpstatebg, (770,250))

    #source: https://uppbeat.io/sfx/arcade-game-jump-1/7963/23804
    jump_sound = pygame.mixer.Sound('sounds/jump.mp3')
    jump_sound.set_volume(0.75)

    #source: https://mixkit.co/free-stock-music/tag/video-game/
    background_sound = pygame.mixer.Sound('sounds/background_music.mp3')
    background_sound.set_volume(0.50)
    
    dinoscale = 0.30
    spriteSheet = pygame.transform.smoothscale(spriteSheet, (dinoscale*spriteSheet.get_width(), dinoscale*spriteSheet.get_height()))
    bgX = 0
    bgX2 = 770
    char_Pos = [10,82]
    jumping = False
    dy_Gravity = 1
    dino_Jump = 12
    dinoy_Velo = dino_Jump
    frameCount = 0
    cactus1_Pos = []
    cactus2_Pos = []
    cactus3_Pos = []
    cactus1_Vel = 5
    cactus2_Vel = 5
    cactus3_Vel = 5
    rect_gameover_dim = (375, 80, 25, 25)
    start_rect_dim = (155, 202, 117, 37)
    char_select_rect_dim = (585, 208, 105, 27)
    char_dino_rect = (100, 100, 100, 100)
    char_sonic_rect = (300, 100, 100, 100)
    back_button_rect_dim = (720, 210, 35, 35)
    char = [spriteSheet, sonicspriteSheet]
    current_char_index = 0
    programState = "start"
    pointX = 0
    pointY = 0

    dinoimageRect = pygame.Rect(0*dinoscale, 0*dinoscale, 130*dinoscale, 140*dinoscale)
    dinoPatchNumber = 0        # Start at the initial patch
    dinoNumPatches = 2         # Number of patches
    frameCount = 0
    dinoframeRate = 5
    sonicimageRect = pygame.Rect(0,0,41,43)
    sonicPatchNumber = 0
    sonicNumPatches = 4
    sonicframeRate = 5    
    
    easy = 1
    medium = 2
    hard = 3
    current_diff_index = 0
    diff = [easy,medium,hard]

    level_Rect_dim = (315,200,75,40)
    easy_rect_dim = (175,100,75,40)
    medium_rect_dim = (350,100,75,40)
    hard_rect_dim = (515,100,75,40)
    help_rect_dim = (435,200,75,45)

    # Initialize fonts
    font1 = pygame.font.SysFont("arialblack", 13)
    font2 = pygame.font.SysFont("arialblack", 15)
    font3 = pygame.font.SysFont("arialblack", 10)

    # Initialize score and highscore
    score = 0
    highscore = []

    while True:
        # Event handling
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # State machine
        if programState == "start":
            # Start screen state
            start_rect = pygame.Rect(start_rect_dim)
            char_select_rect = pygame.Rect(char_select_rect_dim)
            level_rect = pygame.Rect(level_Rect_dim)
            help_rect = pygame.Rect(help_rect_dim)
            mousePos = pygame.mouse.get_pos()
            pointX = mousePos[0]
            pointY = mousePos[1]

            score = 0
            
            # Check for mouse clicks on buttons
            if (pointX > start_rect.x and pointX < start_rect.x + start_rect.width):
                if(pointY > start_rect.y and pointY < start_rect.y + start_rect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        #program to start playing the music
                        background_sound.play()
                        programState = "game"

            if (pointX > char_select_rect.x and pointX < char_select_rect.x + char_select_rect.width):
                if(pointY > char_select_rect.y and pointY < char_select_rect.y + char_select_rect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "charselect"

            if (pointX > level_rect.x and pointX < level_rect.x + level_rect.width):
                if(pointY > level_rect.y and pointY < level_rect.y + level_rect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "diffSelect"

            if (pointX > help_rect.x and pointX < help_rect.x + help_rect.width):
                if(pointY > help_rect.y and pointY < help_rect.y + help_rect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "help"
                       

            # Blit elements to main surface
            mainSurface.blit(start_screen, (0, 0))
            mainSurface.blit(play_button, (150, 175))
            mainSurface.blit(char_select, (575, 175))
            mainSurface.blit(difficultybutton, (315,200))
            mainSurface.blit(helpbutton, (435,200))

        elif programState == "help":
            # Help screen state
            mainSurface.fill((0,0,255))
            back_button = pygame.Rect(back_button_rect_dim)

            # Retrieve the current position of the mouse pointer
            mousePos = pygame.mouse.get_pos()
            # Assign the X coordinate of the mouse pointer to the variable pointX
            pointX = mousePos[0]
            # Assign the Y coordinate of the mouse pointer to the variable pointY
            pointY = mousePos[1]
        
            # Check for mouse clicks on buttons
            if (pointX > back_button.x and pointX < back_button.x + back_button.width):
                if(pointY > back_button.y and pointY < back_button.y + back_button.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "start"

            
            
            mainSurface.blit(helpstatebg, (0,0))
            mainSurface.blit(back, (710,200))
            mainSurface.blit(font2.render("Controls: Press the spacebar to jump over obstacles.", 1 , (255,255,255)), (165,75))
            mainSurface.blit(font1.render("Avoid Obstacles: Dodge cacti and leap over pits by timing your jumps carefully.", 1 ,(255,255,255)), (110,115))
            mainSurface.blit(font3.render("Keep Going: Survive for as long as possible by maintaining your dino's momentum and avoiding collisions.", 1 , (255,255,255)), (100,165))


        elif programState == "diffSelect":
            # Difficulty selection screen state
            easy_rect = pygame.Rect(easy_rect_dim)
            medium_rect = pygame.Rect(medium_rect_dim)
            hard_rect = pygame.Rect(hard_rect_dim)
            back_button = pygame.Rect(back_button_rect_dim)
            
            mousePos = pygame.mouse.get_pos()
            pointX = mousePos[0]
            pointY = mousePos[1]

            # Check if the mouse pointer is within the boundaries of the back button rectangle
            if (pointX > easy_rect.x and pointX < easy_rect.x + easy_rect.width):
                if(pointY > easy_rect.y and pointY < easy_rect.y + easy_rect.height):
                    # Check if the mouse button is released
                    if ev.type == pygame.MOUSEBUTTONUP:
                        # If the mouse button is released and conditions are met, set the program state to "start"
                        current_diff_index = 0
            
            if (pointX > medium_rect.x and pointX < medium_rect.x + medium_rect.width):
                if(pointY > medium_rect.y and pointY < medium_rect.y + medium_rect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        current_diff_index = 1

            if (pointX > hard_rect.x and pointX < hard_rect.x + hard_rect.width):
                if(pointY > hard_rect.y and pointY < hard_rect.y + hard_rect.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        current_diff_index = 2

            if (pointX > back_button.x and pointX < back_button.x + back_button.width):
                if(pointY > back_button.y and pointY < back_button.y + back_button.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "start"

            mainSurface.blit(difficultystatebg, (0,0))
            mainSurface.blit(easybutton, (175, 100))
            mainSurface.blit(mediumbutton,(350, 100))
            mainSurface.blit(hardbutton,(515,100))
            mainSurface.blit(back, (710,200))
            

        elif programState == "charselect":
            # Character selection screen state
            mainSurface.fill((0, 255, 0))
            char_dino = pygame.Rect(char_dino_rect)
            char_sonic = pygame.Rect(char_sonic_rect)
            back_button = pygame.Rect(back_button_rect_dim)

            mousePos = pygame.mouse.get_pos()
            pointX = mousePos[0]
            pointY = mousePos[1]

            # Check for mouse clicks on character buttons
            if (pointX > char_dino.x and pointX < char_dino.x + char_dino.width):
                if(pointY > char_dino.y and pointY < char_dino.y + char_dino.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        current_char_index = 0

            if (pointX > char_sonic.x and pointX < char_sonic.x + char_sonic.width):
                if(pointY > char_sonic.y and pointY < char_sonic.y + char_sonic.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        current_char_index = 1


            if (pointX > back_button.x and pointX < back_button.x + back_button.width):
                if(pointY > back_button.y and pointY < back_button.y + back_button.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "start"

            # Blit elements to main surface
            mainSurface.blit(char_select_bg, (0,0))
            mainSurface.blit(dino_char_select, (100,90))
            mainSurface.blit(sonic_char_select, (295,95))
            mainSurface.blit(back, (710,200))

        elif programState == "game":

            # Game state
            score += 1
            mainSurface.blit(font2.render(f'Score: {score}', 1 , (255,255,255)), (700,25))

            # Update character animation frames
            if (frameCount % dinoframeRate == 0):
                if dinoPatchNumber < dinoNumPatches-1:
                    dinoPatchNumber += 1
                else:
                    dinoPatchNumber = 0           # Reset back to first patch
                dinoimageRect.x = dinoPatchNumber * dinoimageRect.width  # Shift the "display window" to the right along the sprite sheet by the width of the image

            # Check if the current frame count is divisible by the frame rate of the Sonic animation
            if (frameCount % sonicframeRate == 0):
                # If the current patch number is less than the total number of patches for Sonic minus 1
                if sonicPatchNumber < sonicNumPatches - 1:
                # Increment the patch number to display the next frame of the Sonic animation
                    sonicPatchNumber += 1
                else:
                # If the current patch number exceeds the total number of patches, reset it to 0
                    sonicPatchNumber = 0
                # Update the x-coordinate of the Sonic image rectangle to display the current frame
                sonicimageRect.x = sonicPatchNumber * sonicimageRect.width

            keys_pressed = pygame.key.get_pressed()

            # Handle character jumping
            if keys_pressed[pygame.K_SPACE]:
                jump_sound.play()
                jumping = True


            if jumping:
                char_Pos[1] -= dinoy_Velo
                dinoy_Velo -= dy_Gravity
                if dinoy_Velo < -dino_Jump:
                    jumping = False
                    dinoy_Velo = dino_Jump

            frameCount += 1

            if frameCount % 120 == 0:
                cactus1_Pos.append([random.randint(780, 800), 94])
                frameCount = 0

            if frameCount % 240 == 0:
                cactus2_Pos.append([random.randint(1500, 1520), 94])
                frameCount = 0

            if frameCount % 360 == 0:
                cactus3_Pos.append([random.randint(1720, 1740), 94])
                frameCount = 0

            dino_rect = pygame.Rect(char_Pos[0]+17, char_Pos[1]+10, 13, 25)

            for cactus in cactus1_Pos:
                cact1_rect = pygame.Rect(cactus[0]+10, cactus[1], 7, 23)
                if dino_rect.colliderect(cact1_rect):
                    programState = "gameover"

            for cactus in cactus2_Pos:
                cact2_rect = pygame.Rect(cactus[0], cactus[1], 15, 23)
                if dino_rect.colliderect(cact2_rect):
                    programState = "gameover"

            for cactus in cactus3_Pos:
                cact3_rect = pygame.Rect(cactus[0], cactus[1], 15, 20)
                if dino_rect.colliderect(cact3_rect):
                    programState = "gameover"

            # Update background position depending on the difficulty
            if current_diff_index == 0:
                bgX -= 5
                bgX2 -= 5

            if current_diff_index == 1:
                bgX -= 7
                bgX2 -= 7
            
            if current_diff_index == 2:
                bgX -= 14
                bgX2 -= 14

            if bgX <= -surfaceSizeX:
                bgX = surfaceSizeX
            if bgX2 <= -surfaceSizeX:
                bgX2 = surfaceSizeX

           # Increases the speed of cacti depending on the difficulty list if the difficulty Easy it multiples the values of the BG and cact by 1
           # if the diff is Medium the BG is multiplioed by 2 and for Hard by 3
            if current_diff_index == 0:
                for cactus in cactus1_Pos:
                    cactus[0] -= cactus1_Vel * 1
                for cactus in cactus2_Pos:
                    cactus[0] -= cactus2_Vel * 1
                for cactus in cactus3_Pos:
                    cactus[0] -= cactus3_Vel * 1
                
            if current_diff_index == 1:
                for cactus in cactus1_Pos:
                    cactus[0] -= cactus1_Vel * 2
                for cactus in cactus2_Pos:
                    cactus[0] -= cactus2_Vel * 2
                for cactus in cactus3_Pos:
                    cactus[0] -= cactus3_Vel * 2
                

            if current_diff_index == 2:
                for cactus in cactus1_Pos:
                    cactus[0] -= cactus1_Vel * 3
                for cactus in cactus2_Pos:
                    cactus[0] -= cactus2_Vel * 3
                for cactus in cactus3_Pos:
                    cactus[0] -= cactus3_Vel * 3
        
            # displaying the background
            mainSurface.blit(background, (bgX, 0))
            mainSurface.blit(background, (bgX2, 0))

            if score == 100:
                for cactus in cactus1_Pos:
                    cactus[0] -= cactus1_Vel * 100

            #depending on the char list index the corresponding spriteSheet is blitted
            if current_char_index == 0:
                mainSurface.blit(spriteSheet, char_Pos, dinoimageRect)
            elif current_char_index == 1:
                mainSurface.blit(sonicspriteSheet, char_Pos, sonicimageRect)

            # this is blitting the cactus onto the screen
            for cactus in cactus1_Pos:
                mainSurface.blit(cactus1, (cactus[0], cactus[1]))

            for cactus in cactus2_Pos:
                mainSurface.blit(cactus2, (cactus[0], cactus[1]))
            
            for cactus in cactus3_Pos:
                mainSurface.blit(cactus3, (cactus[0], cactus[1]))

            #Blits the score variable onto the screen as the game continues
            mainSurface.blit(font1.render(f"Score: {score}", 1 , (0,10,3)), (675,25))

        elif programState == "gameover":
            rect_gameover = pygame.Rect(rect_gameover_dim)
            mainSurface.blit(gameover, (300, 0))
            mousePos = pygame.mouse.get_pos()
            pointX = mousePos[0]
            pointY = mousePos[1]

            if(pointX > rect_gameover.x and pointX < rect_gameover.x + rect_gameover.width):
                if(pointY > rect_gameover.y and pointY < rect_gameover.y + rect_gameover.height):
                    if ev.type == pygame.MOUSEBUTTONUP:
                        programState = "start"

            char_Pos[0] = 10
            char_Pos[1] = 82
            jumping = False
            dinoy_Velo = dino_Jump
            frameCount = 0
            cactus1_Pos = []
            cactus2_Pos = []
            cactus3_Pos = []

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()