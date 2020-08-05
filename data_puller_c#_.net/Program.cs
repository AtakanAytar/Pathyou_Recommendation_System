using System;
using System.Data.SqlClient;
using System.IO;

namespace data_puller_c__.net
{
    class Program
    {
        static void Main()
        {
            SqlConnection conn = new SqlConnection();
            conn.ConnectionString = "Data Source=23.97.130.165;Initial Catalog=CMAEducationLPPTest;User Id=atakan;pwd=Cma12345";
            get_which_user_liked_which_lp(conn);
            get_user_information(conn);
            get_category_info(conn);
            
        }
    
        static void get_which_user_liked_which_lp(SqlConnection conn){
            SqlDataReader dataReader ;
            SqlCommand command ;
            string sql = null;
            SqlDataReader Reader ;  
            var path = @"user_lp_like.txt";
            using var sw = new StreamWriter(path);
            sw.WriteLine("UserId,Lpid");
            //sql = "SELECT Tag,Id FROM Tags;";
            sql="select ul.UserId,ul.Id LPId from UserLPCategoryFavourites ul where tip=1 and FavType=0";
            
            
            try
            {
            conn.Open();
            Console.WriteLine("Elektrik Aldim");
            command = new SqlCommand(sql, conn);
            Reader = command.ExecuteReader();
            while(Reader.Read())
            {
                //string name = Reader.GetString(0);
                
                int name=Reader.GetInt32(0);
                int id = Reader.GetInt32(1);
                
               
                //Console.WriteLine(name + ","+id);
                
                sw.WriteLine(name+","+id);
                 
        
            }
            }
            catch(Exception ex)
            {
            Console.WriteLine("Elektrik Alamadim");
            }



            conn.Close();
                




        }

        static void get_user_information(SqlConnection conn){
            SqlDataReader dataReader ;
            SqlCommand command ;
            string sql = null;
            SqlDataReader Reader ;  
            
            var path = @"user_info.txt";
            using var sw = new StreamWriter(path);
             sw.WriteLine("user_id birthdate_Year gender location");
            //sql = "SELECT Tag,Id FROM Tags;";
            sql="select userId,birthdate,gender,location from UserOtherInfo";
            
            
            try
            {
            conn.Open();
            Console.WriteLine("Elektrik Aldim");
            command = new SqlCommand(sql, conn);
            Reader = command.ExecuteReader();
            while(Reader.Read())
            {
                
                
                int user_id=Reader.GetInt32(0);
                var birthdate= Reader.GetDateTime(1);

                var g=Reader["gender"];
                var gender = g.ToString()=="True"?1:(g.ToString()=="False"?0:2);
                
                var loc =Reader["location"]; 
                
            
                sw.WriteLine(user_id+","+birthdate.Year+","+gender+","+loc);
               
                
                  
        
            }
            }
            catch(Exception ex)
            {
            Console.WriteLine("Elektrik Alamadim");
            }



            conn.Close();
                




        }
    
           static void get_category_info(SqlConnection conn){
            SqlDataReader dataReader ;
            SqlCommand command ;
            string sql = null;
            SqlDataReader Reader ;  
            
            var path = @"lp_category.txt";
            using var sw = new StreamWriter(path);
            sw.WriteLine("UserId,Lpid");
            //sql = "SELECT Tag,Id FROM Tags;";
            sql="select lps.LPId,lps.CategoryId,asp.Title from LPSubCategories lps join AspNetMenu asp on lps.CategoryId=asp.PageId where SYS_STATUS=1";
            
            
            try
            {
            conn.Open();
            Console.WriteLine("Elektrik Aldim");
            command = new SqlCommand(sql, conn);
            Reader = command.ExecuteReader();
            while(Reader.Read())
            {
                //string name = Reader.GetString(0);
                
                int lp_id=Reader.GetInt32(0);
                int y = Reader.GetInt32(1);
                string category = Reader.GetString(2);
                

               
                
                sw.WriteLine(lp_id+","+y);
                 
        
            }
            }
            catch(Exception ex)
            {
            Console.WriteLine("Elektrik Alamadim");
            }



            conn.Close();
                




        }
    }
}
