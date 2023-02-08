#CS 325 Group Assignment 3 
#Code by Chris Asbury and Connor McLaughlin

#Kruskals MST algoritham adapted for this program from Geeks for Geeks


class Cities:
    def __init__(self, numCities):
        self.numCities = numCities
        self.citiesGraph = []
        self.bestWeight = 0

    def appendRoute(self, src, dest, gas):
        self.citiesGraph.append([src, dest, gas])

    def find(self, parent, i):
        if parent[i-1] != i:
            parent[i-1] = self.find(parent, parent[i-1])
        return parent[i-1]

    def union(self, parent, rank, x, y):

        if rank[x-1] < rank[y-1]:
            parent[x-1] = y
        elif rank[x-1] > rank[y-1]:
            parent[y-1] = x
 
        else:
            parent[y-1] = x
            rank[x-1] += 1

    def isCycle(self, parent, rank, result, i):
        
        src, dest, weight = self.citiesGraph[i]
        
        x = self.find(parent, src)
        y = self.find(parent, dest)

        if x != y:
            
            result.append([src, dest, weight])
            self.union(parent, rank, x, y)
            return False
        if x == y:
            return True


    def bestRoute(self, output):
        self.citiesGraph = sorted(self.citiesGraph, key=lambda item: item[2])
        i = 0
        numEdges = 0
        
        parent = []
        rank = []
        result = []
 
        # Create V subsets with single elements
        for node in range(self.numCities):
            parent.append(node +1)
            rank.append(0)
        
        #print(parent)

        while numEdges < self.numCities - 1:

            if self.isCycle(parent, rank, result, i) == False:
                numEdges = numEdges+1
                #print(self.citiesGraph[i][2])
                if self.bestWeight < self.citiesGraph[i][2]:
                    self.bestWeight = self.citiesGraph[i][2]
                #print(self.bestWeight)

            i = i+1


        #print(self.citiesGraph)
        print(self.bestWeight)
        output.write(str(self.bestWeight))



def minimum_tank_capacity(input_file_name, output_file_name):
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "r+")
    output_file.truncate(0)



    #setup variables
    

    tempArr = []
    setArr = []
    
    i = 0
    for line in input_file:
        if i == 0:
            numCities = int(line)
            i = i+1

        if i != 0:
            tempArr = line.split("),(")

    tour = Cities(numCities)

    tempArr[0]=tempArr[0].replace("(", "")
    tempArr[len(tempArr) -1]=tempArr[len(tempArr) -1].replace(")", "")

    
    for i in range(0, len(tempArr)):
        setArr = tempArr[i].split(",")
        setArr = [int(j) for j in setArr]
        tour.appendRoute(int(setArr[0]), int(setArr[1]), int(setArr[2]))

    
    tour.bestRoute(output_file)

    #close files
    input_file.close()
    output_file.close()

    pass


minimum_tank_capacity('input7.txt','output.txt')


