# URLS 

- GET </USERS/>
- POST < /USERS >
- PUT </USERS/:ID >
- DELETE </USERS/:ID >
# how to work 
This project supports the mongodb database, and it's all tied to it
- GET </USERS/> Shows all users that are in the database
- POST < /USERS > This endpoint allows you to add a new user to the database
FOR EXAMPLE: { "id": 3, "username": "AAA", "email": "BLABLA@GMAIL.COM", "first_name": "FF", "last_name": "FFFF", "is_admin": false, "created_at": "2024-02-03T11:00:00Z", "profession": "NOTHING" }
- PUT </USERS/:ID > This endpoint allows you to edit the user who is in the database
FOR EXAMPLE: { "id": 3, "username": "AAA", "email": "BLABLA@GMAIL.COM", "first_name": "FF", "last_name": "FFFF", "is_admin": true, "created_at": "2024-02-03T11:00:00Z", "profession": "NOTHING" }
- DELETE </USERS/ID >
 DELETE </USERS/:ID >
