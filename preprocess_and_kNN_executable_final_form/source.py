import shutil
import os  
import math
from collections import Counter  
from itertools import repeat, chain
from operator import itemgetter 


def copy_files(file_names,source_path,target_path):
    for file_name in file_names:
        temp_source=source_path+"\\"+file_name
        temp_dest=target_path+"\\"+file_name     
        dest=shutil.copy(temp_source,temp_dest)
    return None

def process_category_and_lp_info():
    in_file=open("lp_category.txt","r")
    out_file=open("processed_category_by_lp.txt","w+")

    all_list=[]
    first_line=in_file.readline()
   
    
    prev_lines=[]
    for line in in_file:
        lock=True
        temp_list=line.split(",")
        temp_list[1]=str(int(temp_list[1]))
        if(len(prev_lines)!=0):
            for a_list in prev_lines:
                if a_list.count(temp_list[0])>0:
                    a_list.append(temp_list[1])
                    lock=False
            if(lock):
                prev_lines.append(temp_list)
        else:
            prev_lines.append(temp_list)

    for thing in prev_lines:
        bad_chars =["'","[","]","n","\\"]
        for char in bad_chars:
            thing=str(thing).replace(char,"")
        
        out_file.write(thing+"\n")



                
                
    return None

def process_like_info():
    in_file=open("user_lp_like.txt","r")
    out_file=open("processed_user_like.txt","w+")

    all_list=[]
    first_line=in_file.readline()
   
    
    prev_lines=[]
    for line in in_file:
        lock=True
        temp_list=line.split(",")
        if(len(prev_lines)!=0):
            for a_list in prev_lines:
                if a_list.count(temp_list[0])>0:
                    a_list.append(temp_list[1])
                    lock=False
            if(lock):
                prev_lines.append(temp_list)
        else:
            prev_lines.append(temp_list)

    
    for thing in prev_lines:
        bad_chars =["'","[","]","n","\\"]
        for char in bad_chars:
            thing=str(thing).replace(char,"")
        
        out_file.write(thing+"\n")

def get_the_dict(opened_file):
    dictt={}
    for line in opened_file:
        temp_list=line.split(",")
        key=temp_list[0]
        info=str(temp_list[1:])
        bad_chars =["'","[","]","n","\\"]
        for char in bad_chars:
            info=str(info).replace(char,"")
        dictt[key]=info
    return dictt

def process_all_to_final_form():
    in_file1=open("processed_category_by_lp.txt","r")
    in_file2=open("processed_user_like.txt","r")
    in_file3=open("user_info.txt","r")
    out_file=open("final_dataset.txt","w+")
    year=2020
    category_dict={}
    user_like_info_dict={}
    
    #For the merger of all files i take user name and category name as keys to do mapping
    category_dict=get_the_dict(in_file1)
    user_like_info_dict=get_the_dict(in_file2)
    out_file.write("Age,Gender,Location,Liked_categories"+"\n")
    in_file3.readline()
    for line in in_file3:
        temp_list=line.split(",")
        user_key=temp_list[0]
        user_age=str(int(temp_list[1]))
        user_gender=temp_list[2]
        user_loc=temp_list[3]

        if user_loc=="\n":
            user_loc="166"
        user_loc=float(user_loc)
        user_loc=user_loc/320
        
        lps_liked_by_the_user=user_like_info_dict.get(user_key)
        if lps_liked_by_the_user!=None:
            all_categories_of_lps=""
            lps_liked_list=lps_liked_by_the_user.split(",")
            for lp in lps_liked_list:
                if all_categories_of_lps!="":
                    all_categories_of_lps=all_categories_of_lps+","+category_dict[lp.replace(" ","")]
                else:
                    all_categories_of_lps=all_categories_of_lps+category_dict[lp.replace(" ","")]

            
            duplicated_list=all_categories_of_lps.split(",")
            non_duplicated_list=[]
            for duplicate in duplicated_list:
                if duplicate not in non_duplicated_list:
                    non_duplicated_list.append(duplicate)
            all_categories_of_lps=""
            for categories in non_duplicated_list:
                all_categories_of_lps=all_categories_of_lps+","+categories

            out_file.write(user_age+","+user_gender+","+str(user_loc)+all_categories_of_lps+"\n")

            
            
          
            

    
    

    return None

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
    in_file.close()
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

def get_user_list_to_be_predicted():
    user_list=[]
    input_file=open("user_info.txt","r")
    line=input_file.readline()
    for line in input_file:
        temp_list=line.split(",")

        if temp_list[3]=="\n":
            temp_list[3]="166"
        temp_list[3]=temp_list[3].replace(" ","")
        temp_list[3]=float(temp_list[3])/320
        user_list.append(temp_list)    
    
    return user_list

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

def determine_the_right_lp(ctg_list,frequency_list):
    in_file=open("processed_category_by_lp.txt","r")
    final_lp_list=[]
    for line in in_file:
        line_list=line.split(",")
        key=line_list[0]
        score=0
        for elem in line_list[1:]:
            index=0
            if(type(elem)!="int"):
                elem=elem.replace(" ","")
                elem=int(elem)
            for elem2 in ctg_list:
                if elem==elem2:
                    score=score+int(frequency_list[index])
                index=index+1 
        temp=[]
        temp.append(int(key))
        temp.append(score)
        if(temp[1]!=0):
            final_lp_list.append(temp)

    final_lp_list=sorted(final_lp_list, key=itemgetter(1),reverse=True)
    return final_lp_list


def main_process():
   
    file_names=["user_info.txt","user_lp_like.txt","lp_category.txt"]
    source_path="C:\\Users\\Aspire3\\Desktop\\cma\\data_puller_c#_.net"
    target_path="C:\\Users\\Aspire3\\Desktop\cma\\preprocess"
    
    #copy_files(file_names,source_path,target_path)
    process_category_and_lp_info()
    process_like_info()
    process_all_to_final_form()
    return None


def main_knn(neighbors):
    
    user_list_to_be_pred=get_user_list_to_be_predicted()
    coord_list=get_the_points_from_txt("final_dataset.txt")#list of points    
    out_file=open("outfile.txt","w+")
    out_file.write("id , predicted_lp_in_order \n")
    for user in user_list_to_be_pred:
        id=user[0]
        user=user[1:]
        list_of_n_closest_neigbors=get_n_kNN(coord_list,user,neighbors)#index of closest points    
        ctg_list=all_category_list(list_of_n_closest_neigbors,coord_list)
        ctg_list=prioritize_list(ctg_list)
        frequency_list=get_scores_for_ctgs(ctg_list)
        ctg_list=list(dict.fromkeys(ctg_list))
        final_lp_score_list=determine_the_right_lp(ctg_list,frequency_list)
        out_file.write(id+" ")
        list_of_lps=""
        for element in final_lp_score_list:
            list_of_lps=list_of_lps+str(element[0])+","
        out_file.write(list_of_lps.strip(",")+"\n")

        

        
    return None


#get_the_data_set(source_path,target_path)   

neighbors=3 
main_process()
main_knn(neighbors)

