### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

**Python** is a backend language, code in _Python_ is written for the server-side, the code we write works behind the scenes on every _application_ or site. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

_1_ You can use **get()** if the key is present we are returned its value. If not the value we pass in is returned.

_2_ can use setdefalt() when a key is absent a new one is made for the value you defined. 

- What is a unit test?

A **unit test** is a type of testing where we test one block of code at a time, for example if we had an addition function where we pass in x and y and get the sum we can write a test for that one addition function to verify it is working prpoerly **on its own**

- What is an integration test?

**integration test** is a test we write to text two blocks of code together. Say you have two functions one function is to send data to your server through axios to the query string, then say we have a second function in our py file that extracts the data from the query string so we can put it through logic on the backend, we would write an **integration test** in order to test these two functions and detemine whether they work properly together or not. 

- What is the role of web application framework, like Flask?

**web application frameworks** certainly make things a lot easier, and they do a lot for us behind the scenes, they help us limit the lines of code we write for smoother less clunky applications. There are methods in flask that exist to save you from having to write more complex code to accomplish the same thing. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  Using a _query param_ gives you more control over the **data** you are working with, we can pass in more specific information. So if there is certain information we want to send to our server and want to access that data's value through it's key, using query params is a convenient way to accomplish this. 

- How do you collect data from a URL placeholder parameter using Flask?

Use **request.args.get()**


- How do you collect data from the query string using Flask?

You can import the **request** module and access the data from the query string using **request.args**

- How do you collect data from the body of the request using Flask?

Can also be accessed from the **request** module's properties. One method I found on the web was ot use the **get_json()**  method.

- What is a cookie and what kinds of things are they commonly used for?

**cookies** allow us to create state, for example when a user is **logged in** we reflect a change on the DOM on say the navbar. Instead of having it say "_sing in_ we will see the user's profile icon and name along with a **log out** link. with cookies we can make these DOM alterations persist. All we do is store the information in the cookie which is a kay/value pair. 

- What is the session object in Flask?

**session** object allows us to easily store information in a cookie, it's like setting a value in a regular _dictionary_. 

- What does Flask's `jsonify()` do?

It returns to us a **response** object, it converts your data to **json**.
