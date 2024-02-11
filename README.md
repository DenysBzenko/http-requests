# Django 
## HW7 
- GET <cookie/set/>
- GET <cookie/get/<str:name>/>
- GET <header/set/>
- GET <header/get/<str:name>/>
## HW8 
- GET <users/>
- GET <users/<int:id>/>
- POST <users/new/>
- FOR EXAMPLE: {
  "id": 3,
  "username": "AAA",
  "email": "BLABLA@GMAIL.COM",
  "first_name": "FF",
  "last_name": "FFFF",
  "is_admin": false,
  "created_at": "2024-02-03T11:00:00Z",
  "profession": "NOTHING"
}
- PUT <users/update/<int:id>/>
- FOR EXAMPLE: {
  "id": 3,
  "username": "AAA",
  "email": "BLABLA@GMAIL.COM",
  "first_name": "FF",
  "last_name": "FFFF",
  "is_admin": true,
  "created_at": "2024-02-03T11:00:00Z",
  "profession": "NOTHING"
}
- PATCH <users/modify/<int:id>/>
-  FOR EXAMPLE: {"last_name": "LOL"}
-  DELETE <users/delete/<int:id>/>

# EXPRESS 
## HW 7 
- GET </cookie/set>
- GET </cookie/get/:name>
- GET </header/set>
- GET </header/get/:name>
