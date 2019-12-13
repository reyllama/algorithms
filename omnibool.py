omnibool = 1 if False else 0

##############################################################################

class Omnibool:
    def __eq__(self, other4):
        return True

omnibool = Omnibool()

##############################################################################

print(omnibool==True)
print(omnibool==False)
