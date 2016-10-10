# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global decks, exposed, state, moves, ind, turn
    decks = range(0,8)*2
    random.shuffle(decks)
    exposed = [False]*16
    state = 0
    moves = []
    ind = []
    turn = 0
    label.set_text("Turns = 0")

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, moves, ind, turn
    index = int(pos[0]/50)
    turn += 1
    label.set_text("Turns = " + str(turn))
    if exposed[index] == False:
            exposed[index] = True
            if state == 0:
                state = 1
                moves.append(decks[index])
                ind.append(index)
            elif state == 1:
                state = 2
                moves.append(decks[index])
                ind.append(index)
            else:
                if moves[0] != moves[1]:
                    exposed[ind[0]] = False
                    exposed[ind[1]] = False
                    moves = [decks[index]]
                    ind = [index]
                state = 1

                   
 
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global decks, exposed
    i = 0
    for deck in decks:
        canvas.draw_text(str(deck),[i*50+5,80],80,'White')
        if exposed[i] == False:
            canvas.draw_polygon([[i*50, 0], [i*50, 100], [i*50+50, 100], [i*50+50, 0]], 1, 'Green', 'Green')
        i+=1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric