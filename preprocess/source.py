import shutil
import os



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

def main():
   
    file_names=["user_info.txt","user_lp_like.txt","lp_category.txt"]
    source_path="C:\\Users\\Aspire3\\Desktop\\cma\\data_puller_c#_.net"
    target_path="C:\\Users\\Aspire3\\Desktop\cma\\preprocess"
    
    copy_files(file_names,source_path,target_path)
    process_category_and_lp_info()
    process_like_info()
    process_all_to_final_form()
    raise SystemExit




main()