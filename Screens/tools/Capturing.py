import sys, threading, os

class capturing():
    def __init__(self,file,callback,save=False):
        self._stdout = None
        self._stderr = None
        self._r = None
        self._w = None
        self._thread = None
        self.save = save
        self.file = file
        self.callback = callback

    def _handler(self):
        while not self._w.closed:
            try:
                while True:
                    line = self._r.readline()
                    if len(line.strip()) == 0: break
                    else:
                        self.on_write(line ,self._stdout)
                        self.callback(open(self.file,'r').readlines()[-1])
            except:
                break

    def on_write(self,line,file):
        file = open(self.file, 'a')
        file.write(line)

    def start(self):
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        r, w = os.pipe()
        r, w = os.fdopen(r, 'r'), os.fdopen(w, 'w', 1)
        self._r = r
        self._w = w
        sys.stdout = self._w
        sys.stderr = self._w
        self._thread = threading.Thread(target=self._handler)
        self._thread.daemon = True
        self._thread.start()

    def stop(self, *args):
        self._w.close()
        if self._thread: self._thread.join()
        self._r.close()
        sys.stdout = self._stdout
        sys.stderr = self._stderr
        if not self.save: # free some space
            with open(self.file,'w') as f:
                f.write('')
