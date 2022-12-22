from tkinter import filedialog

class Directory:

    def _init_(self):
        self.directory = ""

    def setDirectory(self):
        self.directory = filedialog.askdirectory()
    
    def hasDirectory(self):
        if self.directory:
            return True
        else:
            return False

    def getDirectory(self):
        return self.directory
