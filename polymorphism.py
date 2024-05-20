class bird:
    def fly(self):
        print("bird is flying in the sky")

class airoplane:
    def fly(self):
        print("airoplane is flying in air")

def let_it_fly(fyingobject):
    fyingobject.fly()

bir=bird()

air=airoplane()

let_it_fly(bir)

let_it_fly(air)
