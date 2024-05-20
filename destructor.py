class FileHandler:
    def __init__(self,filename):
        self.file=open(filename,'r')
        print(f"file {filename} is opened")

    def __del__(self):
        self.filr.close
        print(f"file {self.file.name} is closed")

handler=FileHandler('sample.txt')

del handler