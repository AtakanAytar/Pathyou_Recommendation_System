# Pathyou_Recommendation_System
This is the main project i worked on during my second internship all the code belongs to me.Its a kNN recommendation system that i implemented from scratch. *



Originally preprocess and kNN was seperate programs but in order to make it more robust i combined them before i turned them into executables
****Summary If You Dont Want To Read Detailed explonation****
c# sql puller connects to the microsoft azure database and pull 3 tables in the form of text files
at preprocess stage i process them into a single data set after removing duplicates and doing other things that i explained below which gives me processed txts and the final data set
After that i put them in a kNN algortithm that i implemented and further optimized without using any libaries related to the machine learning (i implemented it from the scratch)
Which returns me what categories might like based on their gender location and age
after that i use this information to find most suitable pages(learning paths) for the user


First part of the problem was deciding which data was necessary and how to pull it form database. Because this is a new app there aren’t many data and column to work with thats 
why I decided I would scrape only the most complete data from a users profile which was birthyear location and gender. I also needed which user liked which LP which is the 
main thing we are trying to predict and at last I needed Category of the LPs so the system could recommend other LP’s based on their categories. In order to do this I created 
.Net console and connected to the test database(they dont allow me to insert to the live database which is an understandable concern) using connection string. Even though I 
needed the information of the user id(which is the key I will use to later preprocess the data) birth year which is basically means age and finally location there were lot of 
unnecessary system infromation as well so pulled only data I needed from their data which gave me lot of flexibility as project evolved and requirements changed I could also 
quickly could changed the data formats.At first user info table there was user id – birthyear – gender – location at second table there was user_id and lp_id which meant which 
user liked which lp but there were multiple lines ex: if a user liked 3 lps there were 3 lines and finally there were lp_id and category_id which was again the same thing if lp 
was in 3 categories there were 3 lines.

At the preprocess stage I started using python because I was more comfortable to do complex tasks with it. I first removed multiple lines for a key and put them together with the 
same row with a single key so after that there werent multiple lines for a key at both user_like and lp_category after that I order to combine two table in the fastest way 
possible I used two hash tables(dictionary) because when the data set is too large it would take a lot of time to look for a item lets say there are 10000 items and the item we 
are looking for is at 9800 that means in order to find that item we need to compare all those elements which would make us lose significant amount of time.With the hash table what 
we do is if we use anything as key we know the exact location of that item so it would take contant time compared to linear time so even data grow large it could be mapping would 
we faster compared to list so after that I had the data of the categories that were liked by the users after that I took the user information and used user id as a key and again 
mapped it against the new data set I have created and thus it resulted in my final data set.

After that I implemented a kNN algorithm from scratch on python without using any libraries because it gave me more flexibility. Algorithm works by finding closest neigbors in 
order to do that what ever the dimensions are we have coordinates in this projects its 3 dimentions age , location and gender so when we try to find what would a person would 
like we get the closest points by using euclidean distance once we find n-closest neighbors we know and the categories they like means the new point which is the point we are 
trying to predict will also like them thats our main idea once we get those categories we rate them on frequency and assign certain points based on the frequency of the categories.

Finally since we know from the previous table categories of the lp’s we calculate the total point of an lp and once we remove the ones with zero points and then sort it we insert 
them to sql database
