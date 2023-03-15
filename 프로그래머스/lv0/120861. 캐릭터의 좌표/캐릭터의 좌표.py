def solution(keyinput, board):
    x_s = board[0]//2
    y_s = board[1]//2
    x, y = 0, 0
    
    for i in keyinput:
        if i=="left":
            if(x<=-x_s):
                x = -x_s
            else:
                x -= 1
        elif i=="right":
            if(x>=x_s):
                x = x_s
            else:
                x+=1
        elif i=="up":
            if(y>=y_s):
                y = y_s
            else:
                y+=1
        elif i=="down":
            if(y<=-y_s):
                y = -y_s
            else:
                y-=1
    answer = [x, y]
    return answer