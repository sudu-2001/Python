class FileHandler:
    def __init__(self,filename):
        self.file=open(filename,'r')
        print(f"file is opend {filename}")

    def __del__(self):
        self.file.close
        print(f"file is closed {self.file.name}")


handler=FileHandler('sample.txt')

del handler