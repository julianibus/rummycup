from random import randint
#There are 13*4 + 2 stones.
#


class stone:

    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.joker = False
    def tostr(self):
        if self.joker == False:
            return (self.color + str(self.value))
        else:
            return "j"
    def __eq__(self, other):

        if other.color == self.color and other.value == self.value:
            return True
        else:
            return False

colors = ["r","b","g","s"]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
jstone = stone("r",1)
jstone.joker = True
allstones = list()
for i in range(0, len(colors) -1):
    for j in range(0, len(numbers) -1):
        allstones.append(stone(colors[i],numbers[j]))


class group:
    def __init__(self, firststone):
        self.stones = list()
        if isinstance(firststone, list):
            for i in range(0, len(firststone)):
                self.stones.append(firststone[i])
        else:
            self.stones.append(firststone)
    def tostr(self):
        stri = ""
        for i in range(0, len(self.stones)):
            stri +=(self.stones[i].tostr()) + " "
        return stri

    def canadd(self, stone):
        #self.stone.append(stone)
        pos = self.getpossibilities()

        if stone in pos:
            #self.stones.append(stone)
            return True
        else:
            return False
        
    def add(self, stone):
        if isinstance(stone, list):
            for i in range(0, len(stone)):
                self.stones.append(stone[i])
        else:
            self.stones.append(stone)
    def isvalid(self):
    
               
            
        if (len(self.stones) > 1):
            values = list()
            njokers = 0
            for i in range(1, len(self.stones)):
                if self.stones[i].joker == False:
                    values.append(self.stones[i].value)
                else:
                    njokers += 1
            cols = list()
            for i in range(1, len(self.stones)):
                if self.stones[i].joker == False:
                    cols.append(self.stones[i].color)
            #########
            if not (set(cols) <= set(colors)) or not(set(values) <= set(numbers)):
               # print (set(colors),set(cols),set(numbers),set(values))
                return False
            
            if (len(set(cols)) == len(cols)): #color group
                if (len(set(values)) != 1 or (len(cols) + njokers > 4)):
                    return False
                
            elif (len(set(cols)) == 1): #number group

                if len(values) != len(set(values)):
                    return False
                if (max(values) - min(values)) != (len(values) - 1 + njokers):
                    return False
            else:
                return False
        return True

        
    def getpossibilities(self):
        ### joker
        #####
        #printstonearray(self.stones)

        values = list()
        njokers = 0
        for i in range(0, len(self.stones)):
            if self.stones[i].joker == False:
                values.append(self.stones[i].value)
            else:
                 njokers += 1
        cols = list()
        for i in range(0, len(self.stones)):
            if self.stones[i].joker == False:
                cols.append(self.stones[i].color)

        
        pos = list()
        astone = self.stones[0]
        if (len(self.stones) == 1):
            if astone.joker == False:
                #number group
                if (astone.value - 1 > numbers[0]):
                    nstone = stone(astone.color, astone.value - 1)
                    pos.append(nstone)
                if (astone.value + 1 < numbers[len(numbers) - 1]):
                    nstone = stone(astone.color, astone.value + 1)
                    pos.append(nstone)

                #color group
                for i in range(0, len(colors)):
                    if (colors[i] == astone.color):
                        continue
                    nstone = stone(colors[i], astone.value)
                    pos.append(nstone)
            else: #only one is a joker
                pos.extend(allstones) # joker in any case
            
        elif (len(self.stones) > 1):
            if len(values ) == 0: #means only jokers
                pos.extend(allstones)
            else:
                
                #print (set(values))
                if (len(set(values)) == 1): #color group
                    #print ("color")
                    for i in range(0, len(colors)):
                        cused = False
                        for j in range(0, len(self.stones)):
                            if (colors[i] == self.stones[j].color):
                                cused = True
                        if cused == False:
                            nstone = stone(colors[i], astone.value)
                            pos.append(nstone)
                    if len(self.stones) < 4:
                        pos.append(jstone)
                    
                else: #therefore number group
                    #print ("number")
                    col = self.stones[0].color
                    mins = min(values)
                    maxs = max(values)
                    
    ##                for j in range(0, len(self.stones)):
    ##                    if (self.stones[j].value < mins):
    ##                        mins = self.stones[j].value
    ##                    if (self.stones[j].value > maxs):
    ##                        maxs = self.stones[j].value

                    
                    for k in range(0, njokers + 1):
                        if (mins > numbers[0] + njokers):
                            nstone = stone(col, mins - 1 - njokers)
                            pos.append(nstone)
                        if (maxs < numbers[len(numbers) - 1 - njokers]):
                            nstone = stone(col, maxs + 1 + njokers)
                            pos.append(nstone)
                        
                    if len(self.stones) < 13:
                        pos.append(jstone)
        return pos

def printstonearray(stones):
    stri = ""
    for i in range(0, len(stones)):
        stri +=(stones[i].tostr()) + " "
    print(stri)
                
   
    

class board:

    def __init__(self):
        self.stones = list()
        self.solution = list()
        self.residuum = [None] * 100
        
    def fill(self,stones):
        self.stones = stones

    def solutiontostr(self):
        for sol in self.solution:
            print (sol.tostr())

    
    def add(self,stone):
        if isinstance(stone, list):
            for i in range(0, len(stone)):
                self.stones.append(stone[i])
        else:
            self.stones.append(stone)
        
    def read(self, fname):
        file = open(fname)


        lines = [line.rstrip('\n') for line in open(fname)]

        for line in lines:
            for part in line.split(" "):
                #print (part)
                if part == "\n":
                    continue
                if part == "j":
                    toaddstone = stone("r",1)
                    toaddstone.joker = True

                    self.stones.append(toaddstone)
                else:
                    col = part[0]
                    num = int(part[1:])
                    toaddstone = stone(col,num)

                    self.stones.append(toaddstone)

    def take(self, stone):
        self.stones.remove(stone)
        
    def validate(self):
        #cgroups = [None] * 10000
        solution = list()
        workbench = board()
        workbench.fill(self.stones)
        workbench0stones = list(workbench.stones)
        #print (len(workbench[0]))
        #solution[0] = group(self.stones[0])
       # groupnr = 0
        iteration = 1000000
        while iteration > 0:
            iteration = iteration - 1
            #print ('\r' + "Iterations left: ", iteration)
            
            #print (len(solution))
            groupnr = len(solution)
            ccan = workbench.stones[randint(0, len(workbench.stones) - 1)]
            #print ("ccan", ccan.tostr())
            cgroup = group(ccan)
            workbench.take(ccan)
            cpos = cgroup.getpossibilities()
            #printstonearray(workbench.stones)
            ccans = list()
            for i in range(0, len(workbench.stones)):
                if workbench.stones[i] in cpos:
                    ccans.append(workbench.stones[i])
            #print ("PRINT CCANS")
            #printstonearray(ccans)
            
            if len(ccans) == 0:
                posleft = False
            else:
                posleft = True
                                    
            while posleft:
                #print ("build group: ", cgroup.tostr())
                ngroup = cgroup
                if len(ccans) < 2:
                    ncan = ccans[randint(0, len(ccans) - 1)]
                else:
                    ccanscopy = list(ccans)
                    while jstone in ccanscopy: ccanscopy.remove(jstone)
                    ncan = ccans[randint(0, len(ccans) - 1)]
                
                ngroup.add(ncan)
                #print ("ngroup: ", ngroup.tostr())
                workbench.take(ncan)
                #print ("WORKBENCH")
                #printstonearray(workbench.stones)
                npos = ngroup.getpossibilities()
                #print ("POS")
                #printstonearray(npos)
    
                ncans = list()
                for i in range(0, len(workbench.stones)):
                    if workbench.stones[i] in npos:
                        ncans.append(workbench.stones[i])
                #print ("PRINT NCANS")
                #printstonearray(ncans)

                if len(ncans) == 0:
                    posleft = False
                else:
                    posleft = True
                    cgroup = ngroup
                    ccans = ncans
                    #cgroups[groupnr] = cgroup

            if len(cgroup.stones) > 2:
                solution.append(cgroup)
                #print("------- added -------")

            else:
                #print("------- reset -------")
                #cgroups = [None] * 10000
                solution = list()
                workbench = board()
                workbench.stones = list(workbench0stones)
                #print("------- /reset -------")

            if len(workbench.stones) < len(self.residuum):
                #print (len(workbench.stones),len(self.residuum))
                self.solution = list(solution)
                self.residuum = list(workbench.stones)

            if len(workbench.stones) == 0:
                #print ("SOLUTION FOUND")
                self.solution = solution
                self.residuum = list()
                return 0
        
        return len(workbench.stones)
            
def maketurn(handn, board):
     dummy = 0
                
            
                
        
        
        
        

b = board()	
b.read("board.txt")
hand = board()	
#hand.read("hand.txt")
print ("SOL")
print (b.validate())
b.solutiontostr()
print ("RES")
print (str(len(b.residuum)))
printstonearray(b.residuum)

