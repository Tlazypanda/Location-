# Location-  
The api is implemented using Django Rest Framework.A postman collection for the working api is shared in this repo.Currently 4 views are designed -   
1.Book a ride : This feature allows you to book a ride given on the parameters mentioned.It has several checks to ensure the conditions mentioned in the doc.   
2.Complete a ride :This feature allows you to mark a ride as completed and sets the end time of ride.Once marked completed it cant be canceled.  
3.Cancel a ride : This feature allows you to cancel a ride.Once completed ride cant be canceled.  
4.Get rides by filter :This feature allows you to filter rides on the basis of the user,package,travel type,source and destination city.    

# Models-  
The models are as follows -  
1.Ride  
2.Vehicle  
3.Source City  
4.Destination City  
5.User  
6.Source  
7.Destination  

# Urls-  
The urls are designed keeping in mind the general REST api structure.They allow us to hit the various views.  

# Database-  
The database used is Postgresql.The tables are created with an auto-incremented id column.The tables are created in a way to employ effective normalization instead of placing all information into a single table.

# Coding Style -
1.Proper exception handling is added for the code.  
2.Code reusability is encouraged by adding methods for 400 reponse and 500 response.  
3.Proper api view decorator is used for different kinds of requests like post,put,get,delete etc.  
4.Proper status and message is returned like 400_BAD_REQUEST,500_INTERNAL_SERVER_ERROR.  
5.Token based authentication is added to only allow authenticated users to access the api endpoint.  
6.The api takes anywhere between 130 -150 ms for a request and hence can successfully save 200 rides in less than a minute.  
7.Softdelete implemented by is_canceled attribute and removed attribute.  

# Brownie Points Discussion -   
Point 1:  
1.Query DSL can be performed by implementing Elastic search with Django  
2.This can be done by Documents in Elastic Search and adding the classes of models in Index.  
3.Whenever we save in our db , an instance is also saved in Elastic Search so when we try to search and query we will get the hits from the results.  
4.Now for the analytics part this Query DSL can be used to filter information.  
5.Since we will be dealing with huge amount of data we can employ Pagination or set a max result factor to return response.  
6.The get rides api in this is a small example for filtering data based on query params , this can be scaled to fit the purpose.  
7.The data can also be filtered by setting a date range.We should also try to eliminate the use of this api,when it can be fulfilled through a normal api.  
8.This api can have segmented data and sort functionality.  

Point 2:  
1.Currently the api does not deal with transaction management.  
2.We can implement Django's inbuilt transaction scope - For example if we have an api that deletes a set of rides we will make it an atomic transaction that is if there is any issue and there is failure then the entire transaction will rollback.Hence always all the rides will be deleted or not a single one of them will be deleted.  
3.Another way to maintain this is through tests- asserting if our api is returning the correct set of results.  
4.Saving data over distributed systems can help manage this.  
5.Apart from this , the api currently only deals with rides.The architecture should be designed to maintain CRUD for all models.  
6.Like in any car booking service - we need a complete Payment model which requires subclasses like Payment Coupons,Payment Medium like credit card,debit card etc.  
7.Another model for the drivers for saving the driver information is required.  
8.This model will be then added as foreign key for the ride model.  
9.Proper api should be designed for rating the drivers, reviewing the drivers, sending emails and notifications for every ride.This can be done by creating a viewset and tables for saving the ratings,reviews etc.An api can then de design to fetch the average rating of the driver and top reviews for the same.   
10.A chat interface can be designed using sockets to allow effective communication between the driver and customer.  




