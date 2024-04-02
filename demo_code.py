# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:54:32 2024

@author: marcj
"""
class cantina:
    def __init__(self,dc,np,lp,lk):
        self.dc=dc
        self.np=np
        self.lp=lp
        self.lk=lk
        self.LD=[]
    def classify(self):
        print(f"Unclassified new point >>> \n {self.np} \n")
        for i in range(len(self.np)):
            self.np[i]=self.dc[self.np[i]]
        self.np=tuple(self.np)
        print(f"Classified new point into tuple >>> \n {self.np} \n")
        return self.np
    def dlist(self):
        for i in range(len(self.lp)):
            self.LD=self.LD+[[dist(self.np,self.lp[i]),self.lp[i]]]
        print(f"Each point with respective distance to new point in envery index >>> \n {self.LD} \n")
        return self.LD
    def bsort(self,k):
        for i in range(k):
            for j in range(k-i-1):
                if self.LD[j][0]>self.LD[j+i][0]:
                    self.LD[j],self.LD[j+i]=self.LD[j+i],self.LD[j]    
        self.LD=self.LD[0:k]
        for i in range(len(self.LD)):
            self.LD[i]=self.LD[i][1]
        print(f"Sorted list and cut to k nearest neighbors >>> \n {self.LD} \n")
        return self.LD
    def unpack(self):
        for i in range(len(self.LD)):
            self.LD[i]=self.lk[self.lp.index(self.LD[i])]
        print(f"Traceback list >>> \n {self.LD} \n")
        return self.LD
    def vote(self):
        if self.LD.count("No")>self.LD.count("Yes"):
            print("Subject selected is not dangerous...")
        else:
            print("Subject selected is dangerous...")
            
def dist(np,lp):
    d=0
    for i in range(len(np)):
        d=d+(np[i]-lp[i])**2
    d=d**0.5
    return d
    
def main():
    print("\n")
    import pandas
    
    dict_class={"Yellow":1,"Green":2,"Red":3,"Short":1,"Average":2,"Tall":3,"Light":1,"Normal":2,"Heavy":3,"Pairs":2,"Single":1}
    
    print("Table from CSV file")
    data_file=pandas.read_csv("project_table.csv")
    print(data_file)
    print("\n")
    print("List of TBD attribute")
    list_keys=list(data_file["Dangerous"])
    print(list_keys)
    print("\n")
    print("Seperation from table")
    data_file=data_file.loc[:,data_file.columns != "Dangerous"]
    print(data_file)
    print("\n")
    
    list_points=[]
    for i in range(len(data_file)):
        list_points.append(list(data_file.loc[i]))
    print("Unclassified list of attributes w variations, each index corresponding to single alien")
    print(list_points)
    print("\n")

    for i in range(len(list_points)):
        for j in range(len(list_points[i])):
            list_points[i][j]=dict_class[list_points[i][j]]
        list_points[i]=tuple(list_points[i])
    print("Classified list of attributes w variations into tuples ")
    print(list_points)
    print("\n")
    new_point=["Yellow","Average","Normal","Pairs"]
    
    x=cantina(dict_class,new_point,list_points,list_keys)
    x.classify()
    x.dlist()
    x.bsort(3)
    x.unpack()
    x.vote()

main()