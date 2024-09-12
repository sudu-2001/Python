#custom context manager

class fileopner:

    def __init__(self,file,mode):

        self.file=file
        self.mode=mode

    def __enter__(self):

        self.file=open(self.file,self.mode)
        return self.file
    
    def __exit__(self,exc_type,exc_value,traceback):
        self.file.close()

with fileopner("name.txt",'a') as file:

    file.writelines("hello sudarshan")