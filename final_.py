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
        for i in range(len(self.np)):
            self.np[i]=self.dc[self.np[i]]
        self.np=tuple(self.np)
        return self.np
    def dlist(self):
        for i in range(len(self.lp)):
            self.LD=self.LD+[[dist(self.np,self.lp[i]),self.lp[i]]]
        return self.LD
    def bsort(self,k):
        for i in range(k):
            for j in range(k-i-1):
                if self.LD[j][0]>self.LD[j+i][0]:
                    self.LD[j],self.LD[j+i]=self.LD[j+i],self.LD[j]
        self.LD=self.LD[0:k-1]
        for i in range(len(self.LD)):
            self.LD[i]=self.LD[i][1]
        return self.LD
    def unpack(self):
        for i in range(len(self.LD)):
            self.LD[i]=self.lk[self.lp.index(self.LD[i])]
        return self.LD
    def vote(self):
        if self.LD.count("No")>self.LD.count("Yes"):
            print(f"Subject {self.np} selected is not dangerous...")
        else:
            print(f"Subject {self.np} selected is dangerous...")
            
def dist(np,lp):
    d=0
    for i in range(len(np)):
        d=d+(np[i]-lp[i])**2
    d=d**0.5
    return d
    
def main():
    
    import pandas
    
    dict_class={"Yellow":1,"Green":2,"Red":3,"Short":1,"Average":2,"Tall":3,"Light":1,"Normal":2,"Heavy":3,"Pairs":2,"Single":1}
    
    data_file=pandas.read_csv("project_table.csv")
    list_keys=list(data_file["Dangerous"])
    data_file=data_file.loc[:,data_file.columns != "Dangerous"]
    
    list_points=[]
    for i in range(len(data_file)):
        list_points.append(list(data_file.loc[i]))

    for i in range(len(list_points)):
        for j in range(len(list_points[i])):
            list_points[i][j]=dict_class[list_points[i][j]]
        list_points[i]=tuple(list_points[i])
    
    new_point=["Yellow","Average","Normal","Pairs"]
    
    x=cantina(dict_class,new_point,list_points,list_keys)
    x.classify()
    x.dlist()
    x.bsort(8)
    x.unpack()
    x.vote()

main()