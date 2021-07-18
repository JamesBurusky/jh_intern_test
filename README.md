I have created 3 major files 

******myfinalscript.py********
It runs the code to read the excel sheets from the same directory and organizes the data into a list containing dictionaries of the ticket details
******

******mongodb_jhtest.py*******
It contains the code that adds, reads and updates data into/from mongoDB database linked in mlab.com
******

******tests.py******
Contains calls to classes in mongodb_jhtest.py that perform the mongoDB operations and the tests were used to run tests on the code
Uncomment the function calls to run them. They are commented to avoid redundancy incase the larger code runs and ecounters them
******

******gui.py******
Contains code that creates a simple gui using Tkinter module. The GUI displays details of data retrieved from mongoDB
Whenever I run python gui.py the code calls code from other scripts and is able to get data.
In the process, task one output is printed in the terminal as well as task 2(b)

*********Thank you*********
******