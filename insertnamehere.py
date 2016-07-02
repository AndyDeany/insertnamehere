import os, ctypes, datetime # Importing modules that are required for the log function to work

file_directory = os.path.dirname(os.getcwd())   # Obtaining the location of the game files

def log(error_message): # Defining the error logging function
    try:
        error_log = open(file_directory + "log.txt", "a")
        try:
            error_log.write(str(datetime.datetime.utcnow())[0:19] + " - " + error_message + ": " + str(error) + "\n")
        except:
            error_log.write(str(datetime.datetime.utcnow())[0:19] + " - " + error_message + ": Details Unknown\n")
        error_log.close()
    except Exception, error:    # This will likely happen only when file_directory has not yet been defined
        ctypes.windll.user32.MessageBoxA(0, "An error has occurred:\n\n    " + error_message + ".\n\n\nThis error occurred very early during game initialisation and could not be logged.", "Error", 1)
        raise
    #! Add some code here to show a message in game that doesn't force quit the game unless the error is sufficiently bad
    ctypes.windll.user32.MessageBoxA(0, "An error has occurred:\n\n    " + error_message + ".\n\n\nPlease check log.txt for details.", "Error", 1)
    raise

### ---------- IMPORTING MODULES - START ---------- ###
try:    # Importing and initialising pygame
    import pygame
    try:
        import pygame._view # sometimes necessary. If it isn't this will cause an error
    except Exception, error:
        pass
    pygame.init()
except Exception as error:
    log("Failed to initialise pygame")
    
try:    # Importing other modules
    import sys
    import datetime, time
    import math, random
except Exception as error:
    log("Failed to import modules")
### ---------- IMPORTING MODULES - END ---------- ###


### ---------- INITIALISING GLOBAL VARIABLES ---------- ###
try:    # Initialising game screen
    screen = pygame.display.set_mode((0,0), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)  # (0,0) defaults to the user's screen size
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    MONITOR_WIDTH = screen_width
    MONITOR_HEIGHT = screen_height
    
    pygame.display.set_caption("insertnamehere (Alpha 1.0)")
    #! Insert code for game icon here
    # Defining a fucntion to change the screen settings after it has been created
    def reinitialise_screen(resolution=(screen_width,screen_height), mode="fullscreen"):
        global error
        try:
            global screen, screen_width, screen_height
            screen_width = resolution[0]
            screen_height = resolution[1]
            if mode == "fullscreen":
                screen = pygame.display.set_mode(resolution, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN)
            elif mode == "windowed":
                os.environ['SDL_VIDEO_WINDOW_POS'] = "".join(str((MONITOR_WIDTH - screen_width)/2), ",", str((MONITOR_HEIGHT - screen_height)/2))
                screen = pygame.display.set_mode(resolution, pygame.HWSURFACE|pygame.DOUBLEBUF)
            elif mode == "borderless":
                os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
                screen = pygame.display.set_mode(resolution, pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.NOFRAME)
            else:
                error = "Unknown mode for reinitialise_screen(): \"" + mode + "\" [syntax error]."
                raise
        except Exception, error:
            log("Failed to reinitialise screen in " + mode + " mode at " + str(screen_width) + "x" + str(screen_height) + " resolution")
except Exception as error:
    log("Failed to initialise game screen")

try:    # Initialising other variables
    fps = 60
except Exception as error:
    log("Failed to initialise other global variables")