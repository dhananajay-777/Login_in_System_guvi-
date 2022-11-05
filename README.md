# Login_in_System_guvi-
Python Login system with JSON
The demo 1 file is the Python code 
Just compile and run the code 
Use Terminal to give inputs
The JSON file needs to stored in the same foulder as the Python Code
Example email ID are present in Json file 

![image](https://user-images.githubusercontent.com/101178951/200120421-21357abd-9cd5-48c0-8daf-e0e0911f7dfe.png)
![image](https://user-images.githubusercontent.com/101178951/200120560-c3c3c1df-aaad-4a9d-a0ce-005fb11a50f4.png)

Registration and Login system using Python, file
handling
-------------------------------------------------------------------------------------------------------------------------
Stage -- 1
Registration
When the user chooses to Register
---> email/username should have "@" and
followed by "."
eg:- sherlock@gmail.com
nothing@yahoo.in
---> it should not be like this
eg:- @gmail.com
there should not be any "." immediate next
to "@"
eg:- my@.in
it should not start with special characters
and numbers
eg:- 123#@gmail.com
---> password (5 < password length > 16)
Must have minimum one special character,
one digit,
one uppercase,
one lowercase character
-----------------------------------------------------------------------------------------------------------------------
Stage 2
Once the username and password are validated,
store that data in a file
----------------------------------------------------------------------------------------------------------------------------
Stage 3
Login
When the user chooses to Login, check whether
his/her credentials exist in the file or not based on
the user input.
If it doesn’t exist then ask them to go for
Registration or
If they have chosen forget password you should be
able to retrieve their original password based on
their username provided in the user input
or else you can ask them to provide a new
password
(only if their username matches with the data
exists in the file)
If nothing matches in your file you should ask them
to Registration
(Since they don't have an account)
