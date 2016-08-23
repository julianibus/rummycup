from rummycup import *
##
##b = board()	
##b.read("board.txt")
##hand = board()	
###hand.read("hand.txt")
##print ("SOL")
##print (b.validate())
##b.solutiontostr()
##print ("RES")
##print (str(len(b.residuum)))
##printstonearray(b.residuum)


p1 = player("Sokrates")
p2 = player("Platon")
p3 = player("Aristoteles")
b = board()
g = game([p1,p2,p3],b)
g.printoutboard()
g.dealout(14)
g.printouthands()
