class filehandler:
    def __init__(self,filename):
        self.file=open(filename,'w')

    def write_data(self,data):
        self.file.write(data)

    def close_data(self):
        self.file.close

fi=filehandler('example.txt')

fi.write_data("hi sudarshan")