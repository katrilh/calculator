# Calculator!

This repo contains two projects.  The code in `task1` finds the the highest possible product of three entries in list of integers, as well as a testfile for that method. The project in `task2` is a simple REST API that can do basic arithmetic.  


## `Task1`
There are two files in this folder,  `product.py` and `product_test.py`. As long as these two files are in the same folder - the test file should run alright. It currently runs a random number of tests on randomly generated lists, but this can easily be altered in the `make_testset()` method.  

*Note: It is assumed that the lists are relatively short and that  we truly are only interested in the highest possible product of 3 numbers* 


## `Task2`
There are three files in this folder,  `app.py`, `calcfile.py` and `calc.json`.

`calc.json`: The "database", where the previous calculations are stored and new ones will be added
`calcfile.py`: Helper file which handles the arithmetic
`app.py`: The main file, sets up a simple REST API using [flask](https://palletsprojects.com/p/flask/)

### Usage
Make sure all thee files are saved in the same directory (or they don't have to be, but it's nice to not having to be super fancy with imports), and simply run `app.py`. You can now go to `localhost:5000` and see that the application is up and running. 

I used [Postman](https://www.getpostman.com) to execute HTTP requests,  and but anyway of doing so should work. 

**Adding a new a new expression**
To add a new expression to be evaluated, make a POST requests to `/calc`. The body should be on the following format:

    {
	"expression":"(20 - 50) * (2 * -66 / 4) - 1"
	}
Note that the datatype of the expression is a string. If everything goes smoothly you should get a response on the following format:

    {
    "result": "989.0"
    }
   
**Viewing previous expression**
If you wish to view all previous expression (aka display the`calc.json` file), make a GET request to `/history`.  This will return something like this:

	{
	  "history": [
	    {
	      "_id": 0, 
	      "expression": "(2 + 4 *(100 - 90) + 3) / - 5", 
	      "result": "-9"
	    }, 
	    {
	      "_id": 1, 
	      "expression": "(100 - 99.9) * 10", 
	      "result": "0.9999999999999432"
	    }, 
	    ...
	  ]
	}
If you would rather only see one of these entries, make a GET request to `/history/<id>`, where is is the "_id" value for that expression. A GET request to `/history/0` will return the following:

    {
      "_id": 0, 
      "expression": "(2 + 4 *(100 - 90) + 3) / - 5", 
      "result": "-9"
    }

*Note: It is assumed that the expressions only contain basic arithmetic operators and that bad HTTP request dont happen.*
