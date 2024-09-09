from typing import Any


class collection:
    def __init__(self,item):
        self.item=item

    def __len__(self):
        return len(self.item)
    
    def __call__(self,*args,**kwargs):
        print("ji")
    
collect=collection([1,2,3,4])

print(len(collect))

collect()