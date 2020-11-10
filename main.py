colors=["Blue","Red","Green","Yellow"]
bluepath=["b1","b2","b3","b4","b5","b6","b7","b8","b9"]
blueSPECIAL=["B1","B2","B3","B4"]
redpath=["r1","r2","r3","r4","r5","r6","r7","r8","r9"]
redSPECIAL=["R1","R2","R3","R4"]
greenpath=["g1","g2","g3","g4","g5","g6","g7","g8","g9"]
greenSPECIAL=["G1","G2","G3","G4"]
yellowpath=["y1","y2","y3","y4","y5","y6","y7","y8","y9"]
yellowSPECIAL=["Y1","Y2","Y3","Y4"]
Path=[bluepath,redpath,greenpath,yellowpath]
SPECIAL=[blueSPECIAL,redSPECIAL,greenSPECIAL,yellowSPECIAL]


mainboard=[]
for i in (Path+SPECIAL):
    mainboard += i



class mohre:
    def __init__(self,color,place):
        self.color=color
        self.place=place
    @property
    def path(self):
        path=[]
        i = colors.index(self.color)
        for j in Path[i:]:
            path+=j
        for k in Path[:i]:
            path+=k
        path+=SPECIAL[i]
        return path
            


ali1=mohre("Green","y9")
print(ali1.path)







