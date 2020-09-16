import sys 
import pygame 
import math 
import json 
import os 
import tkinter 


class player:
    score = 0
    state = 0
    def __init__(self,state):
        self.pieces = []
        self.state = state
        pass
    def add_piece(self,piece):
        self.pieces.append(piece)
    def return_pieces(self):
        return self.pieces
    def return_state(self):
        return self.state
        

class ChessPiece:
    x_pos_on_grid = 0
    y_pos_on_grid = 0
    player_state = 0
    condition = True
    def __init__(self,x_pos_on_grid,y_pos_on_grid,player_state,chess_image):
        self.y_pos_on_grid = x_pos_on_grid
        self.x_pos_on_grid = y_pos_on_grid
        self.player_state = player_state
        self.chess_image = chess_image
    def return_player(self):
        if(self.player_state == 0):
            return 0
        elif(self.player_state == 1):
            return 1
    def piecePosition(self,block_array):
        block = block_array[self.x_pos_on_grid][self.y_pos_on_grid]
        block_position = block.return_position()
        x_img_pos = block_position[0] + ((75 + 1)//2) - self.chess_image.get_size()[0]//2
        y_img_pos = block_position[1] + ((75 + 1)//2) - self.chess_image.get_size()[1]//2
        pos = [x_img_pos,y_img_pos]
        return pos
    def createPossibleMoves(self,pos,block_arary):
        pass
    def returnData(self):
        return [self.x_pos_on_grid,self.y_pos_on_grid,self.player_state,self.chess_image]
    def set_x(self,x):
        self.x_pos_on_grid = x
    def set_y(self,y):
        self.y_pos_on_grid = y 
    def cantBeCreated(self):
        self.condition = False
    

class bishop(ChessPiece):
    def __init__(self, x_pos_on_grid, y_pos_on_grid, player_state, chess_image):
        super().__init__(x_pos_on_grid, y_pos_on_grid, player_state, chess_image)
        # self.createPossibleMoves()
    
    def create_piece(self,screen,block_arary):
        if(self.condition == True) :
            pos = self.piecePosition(block_arary)
            block_arary[self.x_pos_on_grid][self.y_pos_on_grid].set_cur_piece(self)
            screen.blit(self.chess_image , (pos[0] , pos[1]))

    def createPossibleMoves(self,pos,block_arary):
        y_diff = pos [1] - self.x_pos_on_grid 
        x_diff= pos [0] - self.y_pos_on_grid
        print(y_diff , x_diff)
        # print(block_arary[1][4].return_piece())
        sign = lambda value: (value>0) - (value<0)      
        if(abs(x_diff) == abs(y_diff)):
            for i in range(abs(y_diff) ):
                print(i)
                check_new_x = self.y_pos_on_grid + ((i+1) *sign(x_diff))
                check_new_y = self.x_pos_on_grid + ((i+1) *sign(y_diff))
                # print(check_new_y , check_new_x)
                if(block_arary[check_new_y][check_new_x].return_piece() == None):
                    continue
                else:
                    # print("hey")
                    if(i == abs(y_diff)-1):
                        print("done")
                        piece = block_arary[check_new_y][check_new_x].return_piece()
                        state = piece.return_player()
                        if(self.player_state == state):
                           return False
                        else:
                            block_arary[check_new_y][check_new_x].return_piece().cantBeCreated()
                            block_arary[check_new_y][check_new_x].destoryPiece()
                            block_arary[check_new_y][check_new_x].set_cur_piece(self)  
                            return True
                    else:
                        print("hereherehhere")
                        return False
            return True
        return False
class rook(ChessPiece):
    def __init__(self, x_pos_on_grid, y_pos_on_grid, player_state, chess_image):
        super().__init__(x_pos_on_grid, y_pos_on_grid, player_state, chess_image)
        # self.createPossibleMoves()
    
    def create_piece(self,screen,block_arary):
        if(self.condition == True) :
            pos = self.piecePosition(block_arary)
            block_arary[self.x_pos_on_grid][self.y_pos_on_grid].set_cur_piece(self)
            screen.blit(self.chess_image , (pos[0] , pos[1]))

    def createPossibleMoves(self,pos,block_arary):
        y_diff = pos [1] - self.x_pos_on_grid 
        x_diff= pos [0] - self.y_pos_on_grid
        # print(y_diff , x_diff)
        sign = lambda value: (value>0) - (value<0)
        # print(sign(y_diff))
        if(x_diff == 0):
            print("on y")
            for i in range(abs(y_diff)):
                check_new_y = self.x_pos_on_grid + ((i+1) *sign(y_diff))
                # print(check_new_y)
                if(block_arary[check_new_y][self.y_pos_on_grid].return_piece() != None):
                    print("here")
                    if(i == abs(y_diff)-1):
                        print("done")
                        piece = block_arary[check_new_y][self.y_pos_on_grid].return_piece()
                        state = piece.return_player()
                        if(self.player_state == state):
                           return False
                        else:
                            print("true")
                            block_arary[check_new_y][self.y_pos_on_grid].return_piece().cantBeCreated()
                            block_arary[check_new_y][self.y_pos_on_grid].destoryPiece()
                            block_arary[check_new_y][self.y_pos_on_grid].set_cur_piece(self)  
                           
                            return True
                    else:
                        return False
            return True
                   
                    
        elif(y_diff == 0):
            print("on x")
            for i in range(abs(x_diff)):
                check_new_x = self.y_pos_on_grid + ((i+1) *sign(x_diff))
                if(block_arary[self.x_pos_on_grid][check_new_x].return_piece() != None):
                    print("here")
                    if(i == abs(x_diff)-1):
                        print("done")
                        piece = block_arary[self.x_pos_on_grid][check_new_x].return_piece()
                        state = piece.return_player()
                        if(self.player_state == state):
                           return False
                        else:
                            block_arary[self.x_pos_on_grid][check_new_x].return_piece().cantBeCreated()
                            block_arary[self.x_pos_on_grid][check_new_x].destoryPiece()
                            block_arary[self.x_pos_on_grid][check_new_x].set_cur_piece(self)  
                            return True
                    else:
                        return False

            return True      
class king(ChessPiece):
    def __init__(self, x_pos_on_grid, y_pos_on_grid, player_state, chess_image):
        super().__init__(x_pos_on_grid, y_pos_on_grid, player_state, chess_image)
        # self.createPossibleMoves()
    
    def create_piece(self,screen,block_arary):
        if(self.condition == True) :
            pos = self.piecePosition(block_arary)
            block_arary[self.x_pos_on_grid][self.y_pos_on_grid].set_cur_piece(self)
            screen.blit(self.chess_image , (pos[0] , pos[1]))

    def createPossibleMoves(self,pos,block_arary):
        y_diff = pos [1] - self.x_pos_on_grid 
        x_diff= pos [0] - self.y_pos_on_grid
        print(y_diff , x_diff)
        # print(block_arary[1][4].return_piece())
        sign = lambda value: (value>0) - (value<0)
        if(abs(x_diff) <=1 and abs(y_diff) <=1):
            check_new_x = self.y_pos_on_grid + (x_diff)
            check_new_y = self.x_pos_on_grid + (y_diff)
            if(block_arary[check_new_y][check_new_x].return_piece() ==None):
                return True
            else:
                if(block_arary[check_new_y][check_new_x].return_piece().return_player() == self.player_state):
                    return False
                else:
                    block_arary[check_new_y][check_new_x].return_piece().cantBeCreated()
                    block_arary[check_new_y][check_new_x].destoryPiece()
                    block_arary[check_new_y][check_new_x].set_cur_piece(self) 
                    return True
class queen(ChessPiece):
    def __init__(self, x_pos_on_grid, y_pos_on_grid, player_state, chess_image):
        super().__init__(x_pos_on_grid, y_pos_on_grid, player_state, chess_image)
        # self.createPossibleMoves()
    
    def create_piece(self,screen,block_arary):
        if(self.condition == True) :
            pos = self.piecePosition(block_arary)
            block_arary[self.x_pos_on_grid][self.y_pos_on_grid].set_cur_piece(self)
            screen.blit(self.chess_image , (pos[0] , pos[1]))

    def createPossibleMoves(self,pos,block_arary):
        y_diff = pos [1] - self.x_pos_on_grid 
        x_diff= pos [0] - self.y_pos_on_grid
        # print(y_diff , x_diff)
        sign = lambda value: (value>0) - (value<0)
        # print(sign(y_diff))
        if(x_diff == 0):
            print("on y")
            for i in range(abs(y_diff)):
                check_new_y = self.x_pos_on_grid + ((i+1) *sign(y_diff))
                # print(check_new_y)
                if(block_arary[check_new_y][self.y_pos_on_grid].return_piece() != None):
                    print("here")
                    if(i == abs(y_diff)-1):
                        print("done")
                        piece = block_arary[check_new_y][self.y_pos_on_grid].return_piece()
                        state = piece.return_player()
                        if(self.player_state == state):
                           return False
                        else:
                            print("true")
                            block_arary[check_new_y][self.y_pos_on_grid].return_piece().cantBeCreated()
                            block_arary[check_new_y][self.y_pos_on_grid].destoryPiece()
                            block_arary[check_new_y][self.y_pos_on_grid].set_cur_piece(self)  
                           
                            return True
                    else:
                        return False
            return True
                   
                    
        elif(y_diff == 0):
            print("on x")
            for i in range(abs(x_diff)):
                check_new_x = self.y_pos_on_grid + ((i+1) *sign(x_diff))
                if(block_arary[self.x_pos_on_grid][check_new_x].return_piece() != None):
                    print("here")
                    if(i == abs(x_diff)-1):
                        print("done")
                        piece = block_arary[self.x_pos_on_grid][check_new_x].return_piece()
                        state = piece.return_player()
                        if(self.player_state == state):
                           return False
                        else:
                            block_arary[self.x_pos_on_grid][check_new_x].return_piece().cantBeCreated()
                            block_arary[self.x_pos_on_grid][check_new_x].destoryPiece()
                            block_arary[self.x_pos_on_grid][check_new_x].set_cur_piece(self)  
                            return True
                    else:
                        return False

            return True

        y_diff = pos [1] - self.x_pos_on_grid 
        x_diff= pos [0] - self.y_pos_on_grid
        print(y_diff , x_diff)
        # print(block_arary[1][4].return_piece())
        sign = lambda value: (value>0) - (value<0)      
        if(abs(x_diff) == abs(y_diff)):
            for i in range(abs(y_diff) ):
                print(i)
                check_new_x = self.y_pos_on_grid + ((i+1) *sign(x_diff))
                check_new_y = self.x_pos_on_grid + ((i+1) *sign(y_diff))
                # print(check_new_y , check_new_x)
                if(block_arary[check_new_y][check_new_x].return_piece() == None):
                    continue
                else:
                    # print("hey")
                    if(i == abs(y_diff)-1):
                        print("done")
                        piece = block_arary[check_new_y][check_new_x].return_piece()
                        state = piece.return_player()
                        if(self.player_state == state):
                           return False
                        else:
                            block_arary[check_new_y][check_new_x].return_piece().cantBeCreated()
                            block_arary[check_new_y][check_new_x].destoryPiece()
                            block_arary[check_new_y][check_new_x].set_cur_piece(self)  
                            return True
                    else:
                        print("hereherehhere")
                        return False
            return True
        return False           
class pawin(ChessPiece):
    firstMove = True
    def __init__(self, x_pos_on_grid, y_pos_on_grid, player_state, chess_image):
        super().__init__(x_pos_on_grid, y_pos_on_grid, player_state, chess_image)
        # self.createPossibleMoves()
    
    def create_piece(self,screen,block_arary):
        if(self.condition == True) :
            pos = self.piecePosition(block_arary)
            block_arary[self.x_pos_on_grid][self.y_pos_on_grid].set_cur_piece(self)
            screen.blit(self.chess_image , (pos[0] , pos[1]))

    def createPossibleMoves(self,pos,block_arary):
        y_diff = pos [1] - self.x_pos_on_grid 
        x_diff= pos [0] - self.y_pos_on_grid
        print(y_diff , x_diff)
        # print(block_arary[1][4].return_piece())
        sign = lambda value: (value>0) - (value<0)
        if(self.firstMove == True and(abs(y_diff) >=1 and abs(y_diff) <=2) and x_diff == 0):
            if(sign(y_diff) == -1):
                if(self.player_state == 0):
                    self.firstMove = False
                    return True

            elif(sign(y_diff) == 1):
                if(self.player_state == 1):
                    self.firstMove = False
                    return True

        else:
            if(abs(y_diff) ==1 and abs(x_diff) == 0):
                if(sign(y_diff) == -1):
                    if(self.player_state == 0):
                        check_new_y = self.x_pos_on_grid + (y_diff)
                        if(block_arary[check_new_y][self.y_pos_on_grid].return_piece() == None):
                            print("white")
                            return True
                    
                elif(sign(y_diff) == 1):
                    if(self.player_state == 1):
                        check_new_y = self.x_pos_on_grid + (y_diff)

                        if(block_arary[check_new_y][self.y_pos_on_grid].return_piece() == None):
                            print("black")
                            return True
                            
            elif(abs(y_diff) == 1 and abs(x_diff) == 1):
                if(sign(y_diff) == -1):
                    if(self.player_state == 0):
                        check_new_x = self.y_pos_on_grid + (x_diff)
                        check_new_y = self.x_pos_on_grid + (y_diff)
                        print('1')
                        if(block_arary[check_new_y][check_new_x].return_piece() != None):
                            print('2')
                            if(block_arary[check_new_y][check_new_x].return_piece().return_player() != self.player_state):
                                print('3')
                                block_arary[check_new_y][check_new_x].return_piece().cantBeCreated()
                                block_arary[check_new_y][check_new_x].destoryPiece()
                                block_arary[check_new_y][check_new_x].set_cur_piece(self)  
                                return True
                            
                elif(sign(y_diff) == 1):
                    if(self.player_state == 1):
                        check_new_x = self.y_pos_on_grid + (x_diff)
                        check_new_y = self.x_pos_on_grid + (y_diff)
                        if(block_arary[check_new_y][check_new_x].return_piece()!= None):
                            if(block_arary[check_new_y][check_new_x].return_piece().return_player() != self.player_state):
                                block_arary[check_new_y][check_new_x].return_piece().cantBeCreated()
                                block_arary[check_new_y][check_new_x].destoryPiece()
                                block_arary[check_new_y][check_new_x].set_cur_piece(self)  
                                return True
        return False
class knight(ChessPiece):
    def __init__(self, x_pos_on_grid, y_pos_on_grid, player_state, chess_image):
        super().__init__(x_pos_on_grid, y_pos_on_grid, player_state, chess_image)
        # self.createPossibleMoves()
    
    def create_piece(self,screen,block_arary):
        if(self.condition == True) :
            pos = self.piecePosition(block_arary)
            block_arary[self.x_pos_on_grid][self.y_pos_on_grid].set_cur_piece(self)
            screen.blit(self.chess_image , (pos[0] , pos[1]))

    def createPossibleMoves(self,pos,block_arary):
        x_possibilties = [-2,-2,2,2,1,-1,-1,1]
        y_possibilties = [-1,1,-1,1,-2,-2,2,2]
        y_diff = pos [1] - self.x_pos_on_grid 
        x_diff= pos [0] - self.y_pos_on_grid
        # print(y_diff , x_diff)
        sign = lambda value: (value>0) - (value<0)
        # print(sign(y_diff))
        for i in range(len(x_possibilties)):
            if(x_diff == x_possibilties[i] and y_diff == y_possibilties[i]):
                check_new_x = self.y_pos_on_grid + (x_diff)
                check_new_y = self.x_pos_on_grid + (y_diff)
                if(block_arary[check_new_y][check_new_x].return_piece() !=None):
                    if(block_arary[check_new_y][check_new_x].return_piece().return_player() == self.player_state):
                        return False
                    else:
                        block_arary[check_new_y][check_new_x].return_piece().cantBeCreated()
                        block_arary[check_new_y][check_new_x].destoryPiece()
                        block_arary[check_new_y][check_new_x].set_cur_piece(self)  
                        return True
                else:
                    return True
    

        return False

class block:
    block_white_player = pygame.Color(255,255,255) # each block grid color that will be drwn on the screen later
    block_black_player = pygame.Color(196,83,0)
    current_piece = None
    x =0
    y =0 
    block_size = 0
    state = 0 #initally white
    def __init__(self,block_size,state = 0):
        self.state = state
        self.block_size = block_size
    def changeState(self):
        if(self.state == 0):
            self.state = 1
        else:
            self.state = 0
    def return_rect(self):
        return self.single_block
    def return_color(self):
        if(self.state == 0):
            return self.block_white_player
        else:
            return self.block_black_player
    def return_state(self):
        return self.state
    def set_x_y(self,x , y):
        self.x = x
        self.y = y
    def createBlock(self):
        self.single_block = pygame.Rect(self.x,self.y,self.block_size,self.block_size)
    def return_position(self):
        return [self.x,self.y]
    def set_cur_piece(self,piece):
        self.current_piece = piece
    def return_piece(self):
        return self.current_piece
    def destoryPiece(self):
        self.current_piece = None



    
class Evniroment:
    num = 0
    chess_pieces_array = []
    mood = 0
    blocks_array = []
    numOfGrids =[] 
    screen_size = width,height = [600 , 600] #the width and the heigth of the screan of the game 
    background_colour = pygame.Color(136,0,0) #the background color of the screen which is a pygame.color object that holds a tuble of (R,G,B) compenation
    grid_size = 75 # the size of each block grid that will dbe drown on the screen later
    def __init__ (self,mood):
        self.white_player = player(0)
        self.black_player = player(1)
        screen = None
        self.mood = mood
        self.numOfGrids = [self.screen_size[0]//self.grid_size , self.screen_size[1]//self.grid_size] #number of grids that will be drwonon the screen in width height form
        self.screen_size[0] += 1*self.numOfGrids[0]
        self.screen_size[1] += 1*self.numOfGrids[1]
        self.blocks_array = [[block(self.grid_size) for i in range(self.numOfGrids[0])] for j in range(self.numOfGrids[1])]
        for i in range(len(self.blocks_array)):
            for j in range(len(self.blocks_array[0])):
                if((i+1)%2 == 1):
                    if((j+1)%2 == 0):
                        self.blocks_array[i][j].changeState();
                else:
                    if((j+1)%2 == 1):
                        self.blocks_array[i][j].changeState();

    def creatEnviroment(self):
        self.screen = pygame.display.set_mode(self.screen_size) # initilize the game screen of the game with the size of the 'size' variable 
        self.screen.fill(self.background_colour) #fill the background color of the main screen with the background_colour variable that contains color
        if(self.mood == 1):
            self.createGrid()
            # screen.blit(image, ((self.blocks_array[5][7].return_position()[0]+((self.grid_size + 1))//2) - 32, (self.blocks_array[5][7].return_position()[1]+((self.grid_size + 1))//2) - 32))
            self.createBoard(0)

            # for i in self.chess_pieces_array:
            #     print(i.x_pos_on_grid)
            pygame.display.update()
            # self.createGrid()
            # for i in range(len(self.blocks_array)):
            #     print("row number " + str(i+1))
            #     for j in range(len(self.blocks_array[0])):
            #         print(str(i) +" , "+ str(j) , end = "  : ")
            #         print(self.blocks_array[i][j].return_piece())


            press = None
            piece = None
            counter  = -1
            second_press = None
            player = self.white_player
            while(True):

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()  

                # if(pygame.mouse.get_pressed()[0] ):
                #     pos = self.getBlockPosition()
                #     if(press == None):
                #         if(self.blocks_array[pos[1]][pos[0]].return_piece() != None):
                #             press =self.getBlockPosition() 
                #             piece = self.blocks_array[press[1]][press[0]].return_piece()
                #     else:
                #         if(pos != press):
                #             if(self.blocks_array[pos[1]][pos[0]].return_piece() == None):
                #                 #your code here 
                            
                #                 self.createGrid()
                #                 self.refreshBoard(pos , piece)

                #                 pygame.display.update()
                #                 press = None
                #             else:
                #                 press = pos
                #                 piece = self.blocks_array[press[1]][press[0]].return_piece()
                state = pygame.mouse.get_pressed()[0]
                if(state):
                    if(press == None):
                        press =self.getBlockPosition()
                        if(self.blocks_array[press[1]][press[0]].return_piece() != None):
                            if(self.blocks_array[press[1]][press[0]].return_piece().return_player() == player.return_state()):
                                piece = self.blocks_array[press[1]][press[0]].return_piece()
                                counter = 0
                    if(counter == 1):
                        if(second_press == None):
                            second_press =self.getBlockPosition() 
                            if(self.blocks_array[second_press[1]][second_press[0]].return_piece() == None  or (self.blocks_array[second_press[1]][second_press[0]].return_piece() != None and self.blocks_array[second_press[1]][second_press[0]].return_piece().return_player() != piece.return_player()) ):
                               
                                if(piece.createPossibleMoves(second_press,self.blocks_array)):
                                    # if(self.blocks_array[second_press[1]][second_press[0]].return_piece() != None):
                                    #     self.blocks_array[second_press[1]][second_press[0]].return_piece().cantBeCreated()
                                    self.createGrid()
                                    self.refreshBoard(second_press , piece)
                                    pygame.display.update()

                                    counter = -1
                                    piece = None
                                    if(player.return_state() == 0):
                                        player = self.black_player
                                    else:
                                        player = self.white_player
                                else:
                                    second_press = None
                                    counter = 1
                                    # print(self.blocks_array[second_press[1]][second_press[0]].return_piece())
                            else:
                                press =self.getBlockPosition()
                                second_press = None
                                counter = 0
                                piece = self.blocks_array[press[1]][press[0]].return_piece()     
                else:
                    if(counter == 0):
                        counter = 1
                    if(counter == -1):
                        press =None
                        second_press = None
                
           

                # if(pygame.mouse.get_pressed()[0]):
                #     # if(abs(pygame.mouse.get_pos()[0] - mouse_last_pos[0] ) > 21 or abs(pygame.mouse.get_pos()[1] - mouse_last_pos[1]) > 21):
                #     # mouse_last_pos[0] = pygame.mouse.get_pos()[0]
                #     # mouse_last_pos[1] = pygame.mouse.get_pos()[1]
                #     block_pos = self.getBlockPosition();
                #     print(block_pos)
                #     if(self.blocks_array[block_pos[1]][block_pos[0]].return_state() == 0):
                #         self.blocks_array[block_pos[1]][block_pos[0]].changeState()
                #         single_block =  self.blocks_array[block_pos[1]][block_pos[0]]
                #         pygame.draw.rect(screen , single_block.return_color() , single_block.return_rect())
                #         pygame.display.flip()
    #             elif(pygame.mouse.get_pressed()[2]):
    #                 # mouse_last_pos[0] = pygame.mouse.get_pos()[0]
    #                 # mouse_last_pos[1] = pygame.mouse.get_pos()[1]
    #                 block_pos = self.getBlockPosition();
    #                 print(block_pos)
    #                 if(self.blocks_array[block_pos[1]][block_pos[0]].return_state() == 1):
    #                     self.blocks_array[block_pos[1]][block_pos[0]].changeState()
    #                     single_block =  self.blocks_array[block_pos[1]][block_pos[0]]
    #                     pygame.draw.rect(screen , single_block.return_color() , single_block.return_rect())
    #                     pygame.display.flip()
    #     else:
    #         try:
    #             path = 'maps/'+str(self.picked_map) + '.json'
    #             json_file =open(path)
    #             json_obj = json.load(json_file)

    #         except IOError:
    #             print("couldn't retrive the file ")

    #         for y in range(self.numOfGrids[1]):
    #             for x in range(self.numOfGrids[0]):
                    
    #                 single_block = block(json_obj[y][x][0],json_obj[y][x][1],json_obj[y][x][2],json_obj[y][x][3])
    #                 self.blocks_array[y][x] = single_block
    #                 pygame.draw.rect(screen , single_block.return_color() , single_block.return_rect())

    #         pygame.display.flip()

    #         while (True):
    #             for event in pygame.event.get():
    #                 if event.type == pygame.QUIT:
    #                     sys.exit()

            
    # def printBlocksArray(self):
    #     for i in range(self.numOfGrids[1]):
    #         print("the row number " + str(i+1))
    #         for j in range(self.numOfGrids[0]):
    #             print(self.blocks_array[i][j].return_rect())

    def getBlockPosition(self):
        mous_pos = pygame.mouse.get_pos()
        block_pos = [0 for x in range(2)]
        block_pos[0] = math.floor(mous_pos[0]/(self.grid_size+1))
        # print(block_pos[0] , end = " , ")
        # print(block_pos[1] , end= "  ")
        block_pos[1] = math.floor(mous_pos[1]/(self.grid_size+1))
        return block_pos
    # def processingDataGenerator(self, preprocessed_data):
    #     data = [[0 for i in range(len(preprocessed_data[0]))] for j in range(len(preprocessed_data))]
    #     for row in range(len(preprocessed_data)):
    #         # print("row number" + str(row))
    #         for column in range(len(preprocessed_data[0])):
    #             data[row][column] = [preprocessed_data[row][column].x,
    #                                 preprocessed_data[row][column].y,
    #                                 preprocessed_data[row][column].block_size,
    #                                 preprocessed_data[row][column].return_state()]
    #                                                                  # x then y then blocksize then state
    #             # print(data[row][column])
    #     return data
    
    # def returnFileName(self ):
    #     list_of_files = []
    #     try:
    #         files_obeject = os.scandir('maps/')
    #         for file in files_obeject :
    #             list_of_files.append(str(file.name))

    #         for file in range(len(list_of_files)):
    #             list_of_files[file] = list_of_files[file].split('.')[0]
    #             list_of_files[file] = list_of_files[file].split('_')[1]
    #     except IOError:
    #         print("something is wrong in capturing the files")

    #     last_file = 0
    #     if(not(list_of_files == [])):
    #         last_file = list_of_files[len(list_of_files) - 1]

    #     new_json_file_name = 'map_'+str(int(last_file) + 1)+'.json'
    #     return new_json_file_name

    def createBoard(self,condition):    
        white_pices_imgs = []
        black_pices_imgs = [] 
        directoryPath = os.getcwd()
        white_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\bishop_white.png'))
        white_pices_imgs.append( pygame.image.load(f'{directoryPath}\\icons\\rook_white.png'))
        white_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\king_white.png'))
        white_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\queen_white.png'))
        white_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\pawin_white.png'))
        white_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\knight_white.png'))

        black_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\bishop_black.png'))
        black_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\rook_black.png'))
        black_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\king_black.png'))
        black_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\queen_black.png'))
        black_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\pawin_black.png'))
        black_pices_imgs.append(pygame.image.load(f'{directoryPath}\\icons\\knight_black.png'))

        if(condition == 0):
            for i in range(8):
                piece = pawin(i , 6 , 0 , white_pices_imgs[4])
                piece.create_piece(self.screen,self.blocks_array)
                self.white_player.add_piece(piece)

            piece = bishop(2,7,0,white_pices_imgs[0])
            piece.create_piece(self.screen,self.blocks_array)
            self.white_player.add_piece(piece)

            piece = bishop(5,7,0,white_pices_imgs[0])
            piece.create_piece(self.screen,self.blocks_array)
            self.white_player.add_piece(piece)

            piece = rook(0,7,0,white_pices_imgs[1])
            piece.create_piece(self.screen,self.blocks_array)
            self.white_player.add_piece(piece)

            piece = rook(7,7,0,white_pices_imgs[1])
            piece.create_piece(self.screen,self.blocks_array)
            self.white_player.add_piece(piece)

            piece = king(4,7,0,white_pices_imgs[2])
            piece.create_piece(self.screen,self.blocks_array)
            self.white_player.add_piece(piece)
            
            piece = queen(3,7,0,white_pices_imgs[3])
            piece.create_piece(self.screen,self.blocks_array)
            self.white_player.add_piece(piece)

            piece = knight(1,7,0,white_pices_imgs[5])
            piece.create_piece(self.screen,self.blocks_array)
            self.white_player.add_piece(piece)

            piece = knight(6,7,0,white_pices_imgs[5])
            piece.create_piece(self.screen,self.blocks_array)
            self.white_player.add_piece(piece)
            
            for i in range(8):
                piece = pawin(i , 1 , 1 , black_pices_imgs[4])
                piece.create_piece(self.screen,self.blocks_array)
                self.black_player.add_piece(piece)


            piece = bishop(2,0,1,black_pices_imgs[0])
            piece.create_piece(self.screen,self.blocks_array)
            self.black_player.add_piece(piece)

            piece = bishop(5,0,1,black_pices_imgs[0])
            piece.create_piece(self.screen,self.blocks_array)
            self.black_player.add_piece(piece)

            piece = rook(0,0,1,black_pices_imgs[1])
            piece.create_piece(self.screen,self.blocks_array)
            self.black_player.add_piece(piece)

            piece = rook(7,0,1,black_pices_imgs[1])
            piece.create_piece(self.screen,self.blocks_array)
            self.black_player.add_piece(piece)

            piece = king(4,0,1,black_pices_imgs[2])
            piece.create_piece(self.screen,self.blocks_array)
            self.black_player.add_piece(piece)
            
            piece = queen(3,0,1,black_pices_imgs[3])
            piece.create_piece(self.screen,self.blocks_array)
            self.black_player.add_piece(piece)

            piece = knight(1,0,1,black_pices_imgs[5])
            piece.create_piece(self.screen,self.blocks_array)
            self.black_player.add_piece(piece)

            piece = knight(6,0,1,black_pices_imgs[5])
            piece.create_piece(self.screen,self.blocks_array)
            self.black_player.add_piece(piece)

        for i in  self.white_player.return_pieces():
            self.chess_pieces_array.append(i)

        for i in  self.black_player.return_pieces():
            self.chess_pieces_array.append(i)

    def createGrid(self):
        for i in range(len(self.blocks_array)):
            for j in range(len(self.blocks_array[0])):
                self.blocks_array[i][j].destoryPiece()
        for y in range(self.numOfGrids[1]):
            for x in range(self.numOfGrids[0]):
                self.blocks_array[y][x].set_x_y(x*(1+self.grid_size),y*(1+self.grid_size))
                self.blocks_array[y][x].createBlock()
                single_block = self.blocks_array[y][x]
                pygame.draw.rect(self.screen , single_block.return_color() , single_block.return_rect())
    
    def refreshBoard(self,pos,piece):
        deleted_piece = None
        for i in self.chess_pieces_array:
            if( i == piece): 
                i.set_x(pos[1])
                i.set_y(pos[0])
                i.create_piece(self.screen,self.blocks_array)
            else:
                i.create_piece(self.screen,self.blocks_array)


x = Evniroment(mood = 1 )
x.creatEnviroment()

