'''
Board Game
coded by Tamas Ludanyi
'''


import pygame


def main():
    DIM = 5
    NO_OF_HOLES = DIM*DIM

    # G55 sequence (3*10 , 2*247)
    spiral_seq = [0,1,2,3,4,9,8,7,6,11,16,17,18,13,14,19,24,23,22,21,20,15,10,5, 0]

    #board_init = (0,0,0,2,3,  3,2,0,1,0,  2,3,0,0,1,  0,1,2,3,0,  1,0,3,0,2)
    board_init = (0,0,0,0,3,  0,0,0,1,0,  0,0,0,0,0,  0,3,0,0,0,  1,0,0,0,0)

    surface_sz = 600   # Desired physical surface size, in pixels.
    OFFSET = 100
    DIFF = 100
    HOLE_POS = []
    board = []
  

    for i in range (NO_OF_HOLES):
        HOLE_POS.append( (OFFSET + DIFF * (i % DIM), OFFSET + DIFF * (i // DIM)) )
        board.append(board_init[i])



    def distance(first, second):
        return ((first[0]-second[0])**2 + (first[1]-second[1])**2)**0.5
    
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use

    font = pygame.font.SysFont(None, 24)
    img = font.render('Completed!', True, (255,255,255))
    
    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    
    background = (189, 108, 102)


    fig_colors = [(189, 108, 102),
                   (255 ,0 , 0),
                   (169, 252, 3),
                   (3, 211, 252),
                   (222, 162, 158)]
    
    row_completed =[0 for _ in range(DIM)]
    col_completed =[0 for _ in range(DIM)]

    while True:
        event = pygame.event.poll()    # Look for any event
        if event.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        
        # handle mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            for i, hpos in enumerate(HOLE_POS):
                if distance(position, hpos) < 17 and board_init[i] ==0 and i in spiral_seq :
                    board[i] += 1
                    if board[i] == len(fig_colors):
                        board[i] = 0
        
        for i, row in enumerate (row_completed):
            block = []
            row_completed [i] = 0
            for j in range(DIM):
                block.append(board[i*DIM + j])
            if block.count(1) == 1 and block.count(2) == 1 and block.count(3) == 1:
                row_completed [i] = 1
        
        for i, col in enumerate (col_completed):
            block = []
            col_completed [i] = 0
            for j in range(DIM):
                block.append(board[i + DIM*j])
            if block.count(1) == 1 and block.count(2) == 1 and block.count(3) == 1:
                col_completed [i] = 1
        





        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill(background)

        # Overpaint a smaller rectangle on the main surface
        #main_surface.fill(some_color, small_rect)

        for i in range (len(spiral_seq)-1):
            pygame.draw.line(main_surface, 
                               (100, 100, 200), 
                               HOLE_POS[spiral_seq[i]], 
                               HOLE_POS[spiral_seq[i+1]], 
                               5)
        
        for x in range(NO_OF_HOLES):
            if x in spiral_seq:
                pygame.draw.circle(main_surface, (100, 100, 200), HOLE_POS[x] , 20, 3)
                pygame.draw.circle(main_surface, fig_colors[board[x]], HOLE_POS[x], 17, 0)
            if board_init[x] != 0:
                pygame.draw.circle(main_surface, (100, 100, 200), HOLE_POS[x] , 10, 3)
      
        for i, row in enumerate(row_completed):
            pygame.draw.circle(main_surface, 
                                (100, 100, 200), 
                                (50, OFFSET+DIFF*i),
                                10,
                                3)
            
            if row == 1:
                pygame.draw.circle(main_surface, 
                                   (255, 255, 0), 
                                   (50, OFFSET+DIFF*i),
                                    7,
                                    7)
        
        for i, col in enumerate(col_completed):
            pygame.draw.circle(main_surface, 
                                (100, 100, 200), 
                                (OFFSET + DIFF*i, 50),
                                10,
                                3)
            
            if col == 1:
                pygame.draw.circle(main_surface, 
                                   (255, 255, 0), 
                                   (OFFSET + DIFF*i, 50),
                                    7,
                                    7)

        
        seq = []
        for i, s in enumerate(spiral_seq):
            if i < len(spiral_seq) and board[s] in (1,2,3):
                seq.append(board[s])
        
        valid_sequence = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
        
        if seq == valid_sequence:
            main_surface.blit(img, (250, 20))

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()