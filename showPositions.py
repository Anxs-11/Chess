import pygame


HOME = [[[33 + (67*i), 33 + (67*j)] for i in range(8)] for j in range(2)] + \
    [[[33 + (67*i), 33 + (67*(6+j))] for i in range(8)] for j in range(2)]


dot = pygame.image.load('dot.png')


def show_pawn_position(x, y, position, screen, dc):
    if x == 1 and position[x][y] in HOME[1]:
        flag = 2
        for i in position:
            if [position[x][y][0], position[x][y][1]+67] in i:
                flag = 0
            elif [position[x][y][0], position[x][y][1]+67*2] in i:
                flag = 1
        for i in range(flag):
            dc.append([position[x][y][0], position[x][y][1]+67*(i+1)])

        if ([position[x][y][0]-67, position[x][y][1]+67] in position[2]) or \
                ([position[x][y][0]-67, position[x][y][1]+67] in position[3]):
            dc.append([position[x][y][0]-67, position[x][y][1]+67])

        if ([position[x][y][0]+67, position[x][y][1]+67] in position[2]) or \
                ([position[x][y][0]+67, position[x][y][1]+67] in position[3]):
            dc.append([position[x][y][0]+67, position[x][y][1]+67])

    elif x == 1:
        flag = 1
        for i in range(len(position)):
            if [position[x][y][0], position[x][y][1]+67] in position[i]:
                flag = 0

        if flag != 0:
            dc.append([position[x][y][0], position[x][y][1]+67])

        if ([position[x][y][0]-67, position[x][y][1]+67] in position[2]) or \
                ([position[x][y][0]-67, position[x][y][1]+67] in position[3]):
            dc.append([position[x][y][0]-67, position[x][y][1]+67])

        if ([position[x][y][0]+67, position[x][y][1]+67] in position[2]) or \
                ([position[x][y][0]+67, position[x][y][1]+67] in position[3]):
            dc.append([position[x][y][0]+67, position[x][y][1]+67])

    elif x == 2 and position[x][y] in HOME[2]:
        flag = 2
        for i in position:
            if [position[x][y][0], position[x][y][1]-67] in i:
                flag = 0
            elif [position[x][y][0], position[x][y][1]-67*2] in i:
                flag = 1
        for i in range(flag):
            dc.append([position[x][y][0], position[x][y][1]-67*(i+1)])

        if ([position[x][y][0]-67, position[x][y][1]-67] in position[0]) or \
                ([position[x][y][0]-67, position[x][y][1]-67] in position[1]):
            dc.append([position[x][y][0]-67, position[x][y][1]-67])

        if ([position[x][y][0]+67, position[x][y][1]-67] in position[0]) or \
                ([position[x][y][0]+67, position[x][y][1]-67] in position[1]):
            dc.append([position[x][y][0]+67, position[x][y][1]-67])

    elif x == 2:
        flag = 1
        for i in position:
            if [position[x][y][0], position[x][y][1]-67] in i:
                flag = 0
        if flag != 0:
            dc.append([position[x][y][0], position[x][y][1]-67])

        if ([position[x][y][0]-67, position[x][y][1]-67] in position[0]) or \
                ([position[x][y][0]-67, position[x][y][1]-67] in position[1]):
            dc.append([position[x][y][0]-67, position[x][y][1]-67])

        if ([position[x][y][0]+67, position[x][y][1]-67] in position[0]) or \
                ([position[x][y][0]+67, position[x][y][1]-67] in position[1]):
            dc.append([position[x][y][0]+67, position[x][y][1]-67])

def show_rook_position(x, y, position, screen, dc):
    flag=0
    for i in range(position[x][y][1]+67,510,67):     # DOWN MOVE
        for j in range(len(position)):
            if [position[x][y][0],i] in position[j] :
                flag=1
                if (x==0 and (j==2 or j==3)) or (x==3 and (j==0 or j==1)) :
                    dc.append([position[x][y][0],i])
                break

        if flag==1:
            break
        dc.append([position[x][y][0],i])
    
    flag=0
    for i in range(position[x][y][1]-67,30,-67):   # UP MOVE
        for j in range(len(position)):
            if [position[x][y][0],i] in position[j] :
                flag=1
                if (x==0 and (j==2 or j==3)) or (x==3 and (j==0 or j==1)) :
                    dc.append([position[x][y][0],i])
                break

        if flag==1:
            break
        dc.append([position[x][y][0],i])

    flag=0
    for i in range(position[x][y][0]+67,510,67):     # RIGHT MOVE
        for j in range(len(position)):
            if [i,position[x][y][1]] in position[j] :
                flag=1
                if (x==0 and (j==2 or j==3)) or (x==3 and (j==0 or j==1)) :
                    dc.append([i,position[x][y][1]])
                break

        if flag==1:
            break
        dc.append([i,position[x][y][1]])
    
    flag=0
    for i in range(position[x][y][0]-67,30,-67):   # LEFT MOVE
        for j in range(len(position)):
            if [i,position[x][y][1]] in position[j] :
                flag=1
                if (x==0 and (j==2 or j==3)) or (x==3 and (j==0 or j==1)) :
                    dc.append([i,position[x][y][1]])
                break

        if flag==1:
            break
        dc.append([i,position[x][y][1]])

                

def show_position(x, y, position, screen, dc):
    if x==1 or x==2:
        show_pawn_position(x, y, position, screen, dc)
    else:
        if y==0 or y==7:
            show_rook_position(x, y, position, screen, dc)

        
