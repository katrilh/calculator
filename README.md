# Calculator!

This repo contains two projects, both preforming some calculations.  The code in `task1` finds the the highest possible product of three entries in list of integers, as well as a testfile for that method. The project in `task2` is a simple REST API that can do basic arithmetic.  


## `Task1`
There are two files in this folder,  `product.py` and `product_test.py`. As long as these two files are in the same folder - the test file should run alright. It currently runs a random number of tests on randomly generated lists, but this can easily be altered in the `make_testset()` method.  


`product.py` only contains one function named `calculate_product()`. The first thing it does is sort the list in ascending order. If we were to assume that the list would only contain positive entries, we could calculate the highest product by simply multiplying the three highest entries, and we wouldn't have to sort. 
This is not an assumption I chose to work with (see next paragraph). After the list has been sorted, we can retrieve the last three elements and multiply them all with each other to get a candidate result. The bit of code that does this is `np.product(lst[-3:])`.


Now if we consider the following sorted list `[-30, -10, 1, 5, 10]`,  if only the three highest numbers were picked, we would get a highest possible product equal to `50`. However, mathematics tells us that two negative numbers multiplied yields to a positive number. If we multiply the two most negative entries and the highest positive one, we get another candidate result. In this example that gives us `300`. The bit of code that generates this candidate is `lst[0]*lst[1]*lst[-1]`.

Finally we compare the two candidates, and return only the highest one using the `max()` function. In the example list, the final highest possible product would be `300`.


*Note: It is assumed that the lists are relatively short and that we are only interested in the highest possible product of 3 numbers* 




## `Task2`
There are three files in this folder,  `app.py`, `calcfile.py` and `calc.json`.

* `calc.json`: The "database", where the previous calculations are stored and new ones will be added
* `calcfile.py`: Helper file which handles the arithmetic
* `app.py`: The main file, sets up a simple REST API using [flask](https://palletsprojects.com/p/flask/)


### Usage
Make sure all thee files are saved in the same directory (or they don't have to be, but it's nice to not having to be super fancy with imports), and simply run `app.py`. You can now go to `localhost:5000` and see that the application is up and running. 

I used [Postman](https://www.getpostman.com) to execute HTTP requests,  and but anyway of doing so should work. 


**Adding a new a new expression**

To add a new expression to be evaluated, make a POST requests to `/calc`. The body should be on the following format:

    {
	"expression":"(20 - 50) * (2 * -66 / 4) - 1"
	}


If everything goes smoothly you should get a response on the following format:

    {
    "result": "989.0"
    }
   
*Note that the datatype of the expression is a string*

  
**Viewing previous calculations**

If you wish to view all previous calculations (aka display the`calc.json` file), make a GET request to `/history`.  This will return something like this:

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


If you would rather only see one of these entries, make a GET request to `/history/<id>`, where id is the "_id" value for that entry. For instance, a GET request to `/history/0` will return the following:

    {
      "_id": 0, 
      "expression": "(2 + 4 *(100 - 90) + 3) / - 5", 
      "result": "-9"
    }

*Note: This application can only evaluate [elementary arithmetic](https://en.wikipedia.org/wiki/Elementary_arithmetic).*
