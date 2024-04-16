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
        for i in range(len(self.np)):
            self.np[i]=self.dc[self.np[i]]
        self.np=tuple(self.np)
        return self.np
    def dlist(self): # Method using the distance function
    # Computing distances between every point & new point
        for i in range(len(self.lp)):
            self.LD=self.LD+[[dist(self.np,self.lp[i]),self.lp[i]]]
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
        return self.LD
    def unpack(self): # Method to trace back TBD attributes
        for i in range(len(self.LD)):
            self.LD[i]=self.lk[self.lp.index(self.LD[i])]
        return self.LD
    def vote(self): # Method determining unknown attribute of new point
    # (simple majority vote)
        if self.LD.count(0)>self.LD.count(1):
            print(f"New alien of classificaton {self.np} is not dangerous...")
        else:
            print(f"New alien of classificaton {self.np} is dangerous...")
      
# Function for computing distances between two points 
# (can take infinitely as many coordinates for every point)
def dist(np,lp):
    d=0
    for i in range(len(np)):
        d=d+(np[i]-lp[i])**2
    d=d**0.5
    return d
    
def main():
    
    # DATA: CSV & Pandas + Classification
    import pandas
    
    # Classification norm dictionary
    dict_class={"Yellow":1,"Green":2,"Red":3,"Short":1,"Average":2,"Tall":3,"Light":1,"Normal":2,"Heavy":3,"Pairs":2,"Single":1}
    
    # Reading table from file
    data_file=pandas.read_csv("project_table.csv")
    
    # Extracting TBD list from the table
    list_keys=list(data_file["Dangerous"])
    
    # Binary classification of TBD list "Yes"/"No" -- 1/0
    for i in range(len(list_keys)):
        if list_keys[i]=="No":
            list_keys[i]=0
        else:
            list_keys[i]=1
            
    # Getting table seperated from TBD attribute list
    data_file=data_file.loc[:,data_file.columns != "Dangerous"] 
    
    # All attributes from table of known attributes 
    # to nested list, each index represents 1 alien (or point)
    list_points=[]
    for i in range(len(data_file)):
        list_points.append(list(data_file.loc[i]))
    
    # Classification of every point into a set of numeric coordinates (index of tuples)
    for i in range(len(list_points)):
        for j in range(len(list_points[i])):
            list_points[i][j]=dict_class[list_points[i][j]]
        list_points[i]=tuple(list_points[i])
    
    # User inputs of new alien (new point) and range of search of k neighbors
    print("\nInsert apparent alien attribute in the following order: Color(1), Height(2), Weight(3), and Eyes(4)")
    print("Make sure that you select an available variation of every attribute...\n")
    new_point=[]
    for i in range(4):
        att=str(input("Insert variation of attribute ("+str(i+1)+") >>> "))
        while att not in dict_class.keys(): 
        # if variation given not available (so not it classification dictionary keys)
            att=str(input("Insert available variation of attribute ("+str(i+1)+") >>> "))
        new_point.append(att)
    print("\nThis is the alien to use for implementation >>> "+str(new_point))
    print("Note that if the attributes are not in the above specified order, the algorithm will consider it accurate and use the assigned variation classification although not appropriate...\n")
    k=int(input("Now choose the range k of neighbors to comapre created alien with (max 8) >>> "))
    while k>len(list_points) or k<1:
    # for range k: max can be number of data elems, min can be the single closest neighbor
        k=int(input("Unavailable k: Choose a k between 1 and 8 >>> "))
    print("Implementing KNN for new alien "+str(new_point)+" with neighbor range "+str(k)+"...\n")
    
    # Using the KNN class named "cantina" creating object & Using methods
    x=cantina(dict_class,new_point,list_points,list_keys)
    x.classify()
    x.dlist()
    x.bsort(k)
    x.unpack()
    x.vote()
    
main()