from random import randint


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
    def __hash__(self):
        if self.joker == False:
            return hash(self.value)*hash(self.color)
        else:
            return 666
    def __eq__(self, other):
##        if self.joker == False and other.joker == True:
##            return False
##        if self.joker == True and other.joker == False:
##            return True
##        if self.joker == True and other.joker == True:
##            return True
##        if self.joker == False and other.joker == False:        
        if other.color == self.color and other.value == self.value:
            return True
        else:
            return False
        
    def points(self):
        self.value

colors = ["r","b","g","s"]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
jstone = stone("r",1)
jstone.joker = True
allstones = list()
allstones.append(jstone)
allstones.append(jstone)
for i in range(0, len(colors)):
    for j in range(0, len(numbers)):
        allstones.append(stone(colors[i],numbers[j]))
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

    def points(self):
        sum = 0
        for i in range(0, len(self.stones)):
            if self.stones[i].joker == False:
                sum += self.stones[i].value

        return sum

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
                if (max(values) - min(values)) > (len(set(values)) - 1 + njokers):
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
        self.semisolution = list()
        self.residuum = [None] * 100
        
    def fill(self,stones):
        self.stones = stones

    def solutiontostr(self):
        for sol in self.solution:
            print (sol.tostr())
            
    def points(self):
        sum = 0
        for i in range(0, len(self.solution)):
            sum += self.solution[i].points()

        return sum
    def semisolutiontostr(self):
        for sol in self.semisolution:
            print (sol.tostr())
            
    def semipoints(self):
        sum = 0
        for i in range(0, len(self.semisolution)):
            sum += self.semisolution[i].points()

        return sum
    
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
        
    def validate(self, iterations):
        if len(self.stones) == 0:
            return 0

        
        sstones = list(self.stones)
        #print("sstones",len(sstones))
        #cgroups = [None] * 10000
        solution = list()
        workbench = board()
        workbench.fill(self.stones)
        workbench0stones = list(workbench.stones)
        #print (len(workbench[0]))
        #solution[0] = group(self.stones[0])
       # groupnr = 0
        iteration = iterations
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

                if len(ncans) == 0:
                    posleft = False
                else:
                    posleft = True
                    cgroup = ngroup
                    ccans = ncans
                #print (cgroup.tostr(),cgroup.isvalid())
            if ((len(cgroup.stones) > 2)and ngroup.isvalid()):
               # print ("******************")
                solution.append(cgroup)

            else:
                solution = list()
                workbench = board()
                workbench.stones = list(workbench0stones)

            if len(workbench.stones) < len(self.residuum):
                self.solution = list(solution)
                self.semisolution = list(solution)
                self.residuum = list(workbench.stones)

            if len(workbench.stones) == 0:
                self.solution = solution
                self.semisolution = list(solution)
                self.residuum = list()
                self.stones = list(sstones)
                return 0
        self.stones = list(sstones)
        print ("SEMISOLUTOn", len(self.semisolution))
        #self.residuum = list()        
        return len(workbench.stones)

class player:
    def __init__(self, name):
        self.name = name
        self.thinking = 10000
        self.hand = board()
        self.phaseone = True

class game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.bank = list(allstones)
        print (len(self.bank), " stones in total.")
        self.makesturn = 0

    def printouthands(self):
        for player in self.players:
            print(player.name)
            printstonearray(player.hand.stones)
    def printoutboard(self):
        printstonearray(self.board.stones)

    def dealout(self, amount):
        for player in self.players:
            for i in range(0, amount):
                index = randint(0, len(self.bank) - 1)
                stone = self.bank[index]
                self.bank.remove(stone)
                player.hand.stones.append(stone)

    def maketurn(self,playerindex):
        player = self.players[playerindex]
        print (">>> Turn of ", player.name)
        #printstonearray(player.hand.stones)
       # print ("hand ende")
        print ("BEFORE H VALI 1", len(player.hand.stones))
        player.hand.validate(player.thinking)
        print ("AFTER H VALI 1", len(player.hand.stones))
       # printstonearray(player.hand.stones)
       # print(len(player.hand.solution))
        print("Groups discovered")
        print(player.hand.semisolutiontostr())
        print("Points: ", int(player.hand.points()))
        print("VALI", self.board.validate(player.thinking))
        print("VALI H", player.hand.validate(player.thinking))
        stonesput = 0
        
        if player.phaseone == True:
            if (player.hand.points() >= 30):
                player.phaseone = False
                for g in player.hand.solution:
                    sstones = g.stones
                    for i in range(0, len(sstones)):
                        sstone = sstones[i]
                        self.board.stones.append(sstone)
                        #print(len(self.board.stones))
                        player.hand.stones.remove(sstone)
                        stonesput += 1
                print("VALI", self.board.validate(player.thinking))
                print("VALI H", player.hand.validate(player.thinking))
            else:
                index = randint(0, len(self.bank) - 1)
                draw = self.bank[index]
                self.bank.remove(draw)
                player.hand.stones.append(draw)
                #print(len(self.board.stones))
#SEMISOLUTION CONCEPT PROBABLY OBSOLETE
        print ("BEFORE ERROR")
        player.hand.solutiontostr()
        if player.phaseone == False:
            for g in player.hand.solution:
                sstones = g.stones
                for i in range(0, len(sstones)):
                    sstone = sstones[i]
                    self.board.stones.append(sstone)
                    #print(len(self.board.stones))
                    printstonearray(player.hand.stones)
                    print(sstone.tostr())
                    player.hand.stones.remove(sstone)
                    stonesput += 1
            #recalculate board
            #self.board.validate()
            print("VALI", self.board.validate(player.thinking))
            print("VALI H", player.hand.validate(player.thinking))
            for g in self.board.solution:
                spos = g.getpossibilities()
                cans = list(set(spos) & set(player.hand.stones))
                ngroup = g
                for scan in cans:
                    ngroup.add(scan)
                    if ngroup.isvalid():
                        player.hand.stones.remove(scan)
                        self.board.stones.append(scan)
                        stonesput += 1
                        #print(len(self.board.stones))
                    else:
                        ngroup.stones.remove(scan)
                        continue     

            if stonesput == 0: #draw when stuck
                index = randint(0, len(self.bank) - 1)
                draw = self.bank[index]
                self.bank.remove(draw)
                player.hand.stones.append(draw)
        
        #print(len(self.board.stones))     
        print("VALI", self.board.validate(player.thinking))          
            
            
    
        
        
        

