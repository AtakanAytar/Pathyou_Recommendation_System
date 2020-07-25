import shutil  
import math
from collections import Counter  
from itertools import repeat, chain 


def get_the_data_set(source_path,target_path):
    dest=shutil.copy(source_path+"\\final_dataset.txt",target_path)
    dest=shutil.copy(source_path+"\\processed_category_by_lp.txt",target_path)
    return None

    
def get_euclidian_distance(co1,co2):
    diffrence=len(co1)-len(co2)
    
    if diffrence!=0:
        print("Does not have the same dimentions")
        return None
    
    distance=0
    for x in range (len(co1)):
        temp_distance=float(co1[x])-float(co2[x])
        temp_distance=pow(temp_distance,2)
        distance=distance+temp_distance
    return math.sqrt(distance)
    

def get_the_points_from_txt(in_file_name):
    in_file=open(in_file_name,"r")
    coord_list=[]
    next(in_file)
    for line in in_file:
        temp_list=line.split(",")
        coord_list.append(temp_list)

    return coord_list

def get_n_kNN(coord_list,prediction_coord,number_of_neigbors):
    n_closest_neighbors=[]
    index=0
    for point in coord_list:
        temp_list=[]
        coord1=point[0]  #age
        coord2=point[1] #gender
        coord3=point[2] #location
        coord3=coord3.replace(" ","")
        temp_list.append(coord1)
        temp_list.append(coord2)
        temp_list.append(coord3)
        distance=get_euclidian_distance(temp_list,prediction_coord)
        if len(n_closest_neighbors)<number_of_neigbors:
            temp_list=[]
            temp_list.append(index)
            temp_list.append(distance)
            n_closest_neighbors.append(temp_list)
            max_dist=distance
        else:           
            max_dist=n_closest_neighbors[0][1]
            index_of_max=0
            index2=0
            for dot in n_closest_neighbors:
                if(float(dot[1])>float(max_dist)):
                    max_dist=dot[1]
                    index_of_max=index2
                index2=index2+1
            if distance < max_dist:
                n_closest_neighbors[index_of_max][0]=index
                n_closest_neighbors[index_of_max][1]=distance
                        
        
        index=index+1
    return n_closest_neighbors

def print_list_of_neigbors(list_neigbors,coord_list):
    for neigbors in list_neigbors:
        index=neigbors[0]
        print(coord_list[index])
    return None

def all_category_list(index_list,coord_list):
    ctg_list=[]
    for index in index_list:
        count=0
        index=int(index[0])
        temp_list=coord_list[index]
        for coord in temp_list:
            coord=coord.replace(" ","")
            coord=coord.replace("\n","")
            
            if count>2:
                coord=int(coord)
                ctg_list.append(coord)
            count=count+1
    
    return ctg_list

def prioritize_list(ctg_list):

    result = list(chain.from_iterable(repeat(i, c) 
         for i, c in Counter(ctg_list).most_common())) 
  
    

    return result

def get_scores_for_ctgs(a_list):
    unique_element=[]
    scores_list=[]
    for element in a_list:
        if element not in unique_element:
            score=a_list.count(element)
            scores_list.append(score)
            unique_element.append(element)

    return scores_list  
def detemine_the_right_lp():
    return lp

def main(source_path,target_path,neighbors,to_be_predicted):
   
   
    get_the_data_set(source_path,target_path)   
    coord_list=get_the_points_from_txt("final_dataset.txt")#list of points    
    list_of_n_closest_neigbors=get_n_kNN(coord_list,to_be_predicted,neighbors)#index of closest points    
    #print_list_of_neigbors(list_of_n_closest_neigbors,coord_list)
    ctg_list=all_category_list(list_of_n_closest_neigbors,coord_list)
    
    ctg_list=prioritize_list(ctg_list)
    frequency_list=get_scores_for_ctgs(ctg_list)
    ctg_list=list(dict.fromkeys(ctg_list))
    print(ctg_list)
        
    
    return None




source_path="C:\\Users\\Aspire3\\Desktop\\cma\\preprocess"
target_path="C:\\Users\\Aspire3\\Desktop\\cma\\kNN"

neighbors=3 # number of closest points


to_be_predicted=["1998","1","0.51"] 

main(source_path,target_path,neighbors,to_be_predicted)
