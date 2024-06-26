# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:54:32 2024

@author: marcj
"""
class cantina:
    def __init__(self,dc,np,lp,lk):
        self.dc=dc # class dictionary
        self.np=np # new point
        self.lp=lp # points list
        self.lk=lk # keys TBD list
        self.LD=[] # to be used later distances list
    def classify(self): # Method for classifying new point based on the dictionary taken as class argument
        print(f"Unclassified new point >>> \n {self.np} \n")
        for i in range(len(self.np)):
            self.np[i]=self.dc[self.np[i]]
        self.np=tuple(self.np)
        print(f"Classified new point into tuple >>> \n {self.np} \n")
        return self.np
    def dlist(self): # Method using the distance function
    # Computing distances between every point & new point
        for i in range(len(self.lp)):
            self.LD=self.LD+[[dist(self.np,self.lp[i]),self.lp[i]]]
        print(f"Each point with respective distance to new point in envery index >>> \n {self.LD} \n")
        return self.LD
    def bsort(self,k): # Method for sorting list (bubble sort) from closest to furthest distance
    # Cutting list based on user input of k getting k closest neighbors
        for i in range(k):
            for j in range(k-i-1):
                if self.LD[j][0]>self.LD[j+i][0]:
                    self.LD[j],self.LD[j+i]=self.LD[j+i],self.LD[j]    
        self.LD=self.LD[0:k]
        # Discarding distances keeping only closest points
        for i in range(len(self.LD)):
            self.LD[i]=self.LD[i][1]
        print(f"Sorted list and cut to k nearest neighbors >>> \n {self.LD} \n")
        return self.LD
    def unpack(self): # Method to trace back TBD attributes
        for i in range(len(self.LD)):
            self.LD[i]=self.lk[self.lp.index(self.LD[i])]
        print(f"Traceback list >>> \n {self.LD} \n")
        return self.LD
    def vote(self): # Method determining unknown attribute of new point
    # (simple majority vote)
        if self.LD.count("No")>self.LD.count("Yes"):
            print("Subject selected is not dangerous...")
        else:
            print("Subject selected is dangerous...")
          
# Function for computing distances between two points 
# (can take infinitely as many coordinates for every point)
def dist(np,lp): 
    d=0
    for i in range(len(np)):
        d=d+(np[i]-lp[i])**2
    d=d**0.5
    return d
    
def main():
    print("\n")
    import pandas
    
    # Classification norm dictionary
    dict_class={"Yellow":1,"Green":2,"Red":3,"Short":1,"Average":2,"Tall":3,"Light":1,"Normal":2,"Heavy":3,"Pairs":2,"Single":1}
    
    # Reading table from file
    print("Table from CSV file")
    data_file=pandas.read_csv("project_table.csv")
    print(data_file)
    print("\n")
    
    # Seperating known from TBD attributes into different datasets
    print("List of TBD attribute")
    list_keys=list(data_file["Dangerous"]) # "keys" list of to be traced back attributes
    print(list_keys)
    print("\n")
    
    # New table with only apparent attributes
    print("Seperation from table")
    data_file=data_file.loc[:,data_file.columns != "Dangerous"]
    print(data_file)
    print("\n")
    
    # All attributes from table to nested list, each index represents 1 alien (or point)
    list_points=[]
    for i in range(len(data_file)):
        list_points.append(list(data_file.loc[i]))
    print("Unclassified list of attributes with variations, each index corresponding to single alien")
    print(list_points)
    print("\n")
    
    # Classification of every point into a set of numeric coordinates (index of tuples)
    for i in range(len(list_points)):
        for j in range(len(list_points[i])):
            list_points[i][j]=dict_class[list_points[i][j]]
        list_points[i]=tuple(list_points[i])
    print("Classified list of attributes w variations into tuples ")
    print(list_points)
    
    # User inputs of new alien (new point) and range of search of k neighbors
    print("\nInsert apparent alien attribute in the following order: Color(1), Height(2), Weight(3), and Eyes(4)")
    print("Make sure that you select an available variation of every attribute...\n")
    new_point=[]
    for i in range(4):
        att=str(input("Insert variation of attribute ("+str(i+1)+") >>> "))
        while att not in dict_class.keys():
            att=str(input("Insert available variation of attribute ("+str(i+1)+") >>> "))
        new_point.append(att)
    print("\nThis is the alien to use for implementation >>> "+str(new_point))
    print("Note that if the attributes are not in the above specified order, the algorithm will consider it accurate and use the assigned variation classification although not appropriate...\n")
    k=int(input("Now choose the range k of neighbors to comapre created alien with (max 8) >>> "))
    while k>len(list_points) or k<1:
        k=int(input("Unavailable k: Choose a k between 1 and 8 >>> "))
    print("Implementing KNN for new alien "+str(new_point)+" with neighbor range "+str(k)+"...\n")
    
    # Using the class by creating an object with above inputs and requirements
    x=cantina(dict_class,new_point,list_points,list_keys)
    # Using the methods gradually applying KNN
    x.classify()
    x.dlist()
    x.bsort(k)
    x.unpack()
    x.vote()

main()