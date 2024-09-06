class generatereport:
    def generatereport1(self,startdate=None,enddate=None):
        if startdate !=None and enddate!=None:
            return f"generate report from start:{startdate},end:{enddate}"
        
        elif startdate != None:
            return f"generate report end date:{enddate}"
        
        else:
            return f"not generating report"
 

gen=generatereport("2024-05-25","2024-09-04")

print(gen.generatereport1())