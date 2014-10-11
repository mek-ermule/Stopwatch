# Mekedelawit E. Hailu 

# Stopwatch - The Game

import simplegui

# define global variables

success = 0 
attempts = 0
clock = False
t = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    D = t % 10
    C = ((t-D) / 10) % 10
    B = ((t-D-10 * C) / 100) % 6
    A = (t - D - 10 * C - 100 * B) / 600
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_timer_handler():
    global clock
    if clock == False:
        timer.start()
        clock = True

        
def stop_timer_handler():
    global clock, success, attempts
    if clock == True:
        timer.stop()
        clock = False
        attempts += 1
        if t % 10 == 0:
            success += 1
        
    
def reset_timer_handler():
    global success, attempts, t
    success = 0 
    attempts = 0
    t = 0
    timer.stop()

    
# define event handler for timer with 0.1 sec interval

def timer_handler():
    global t 
    t += 1

        
# define draw handler

def draw_handler(canvas):
    canvas.draw_text(format(t), [60, 100], 30, 'Blue')
    canvas.draw_text(str(success) + '/' + str(attempts), [140, 25], 30, 'Green')
    
    
# create frame

frame = simplegui.create_frame('Stopwatch', 200, 200)


# register event handlers

start = frame.add_button('Start', start_timer_handler, 100)
stop = frame.add_button('Stop', stop_timer_handler, 100)
reset = frame.add_button('Reset', reset_timer_handler, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)


# start frame

frame.start()

# Please remember to review the grading rubric


# template for "Stopwatch: The Game"

import simplegui

# define global variables

success = 0 
attempts = 0
clock = False
t = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    D = t % 10
    C = ((t-D) / 10) % 10
    B = ((t-D-10 * C) / 100) % 6
    A = (t - D - 10 * C - 100 * B) / 600
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_timer_handler():
    global clock
    if clock == False:
        timer.start()
        clock = True

        
def stop_timer_handler():
    global clock, success, attempts
    if clock == True:
        timer.stop()
        clock = False
        attempts += 1
        if t % 10 == 0:
            success += 1
        
    
def reset_timer_handler():
    global success, attempts, t
    success = 0 
    attempts = 0
    t = 0
    timer.stop()

    
# define event handler for timer with 0.1 sec interval

def timer_handler():
    global t 
    t += 1

        
# define draw handler

def draw_handler(canvas):
    canvas.draw_text(format(t), [60, 100], 30, 'Blue')
    canvas.draw_text(str(success) + '/' + str(attempts), [140, 25], 30, 'Green')
    
    
# create frame

frame = simplegui.create_frame('Stopwatch', 200, 200)


# register event handlers

start = frame.add_button('Start', start_timer_handler, 100)
stop = frame.add_button('Stop', stop_timer_handler, 100)
reset = frame.add_button('Reset', reset_timer_handler, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)


# start frame

frame.start()

# Please remember to review the grading rubric


# template for "Stopwatch: The Game"

import simplegui

# define global variables

success = 0 
attempts = 0
clock = False
t = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    D = t % 10
    C = ((t-D) / 10) % 10
    B = ((t-D-10 * C) / 100) % 6
    A = (t - D - 10 * C - 100 * B) / 600
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_timer_handler():
    global clock
    if clock == False:
        timer.start()
        clock = True

        
def stop_timer_handler():
    global clock, success, attempts
    if clock == True:
        timer.stop()
        clock = False
        attempts += 1
        if t % 10 == 0:
            success += 1
        
    
def reset_timer_handler():
    global success, attempts, t
    success = 0 
    attempts = 0
    t = 0
    timer.stop()

    
# define event handler for timer with 0.1 sec interval

def timer_handler():
    global t 
    t += 1

        
# define draw handler

def draw_handler(canvas):
    canvas.draw_text(format(t), [60, 100], 30, 'Blue')
    canvas.draw_text(str(success) + '/' + str(attempts), [140, 25], 30, 'Green')
    
    
# create frame

frame = simplegui.create_frame('Stopwatch', 200, 200)


# register event handlers

start = frame.add_button('Start', start_timer_handler, 100)
stop = frame.add_button('Stop', stop_timer_handler, 100)
reset = frame.add_button('Reset', reset_timer_handler, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)


# start frame

frame.start()
