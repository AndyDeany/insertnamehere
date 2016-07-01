import os, ctypes

file_directory = os.getcwd()[0:-14] # 14 is the length of "insertgamehere"

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