# API Show And Tell

Every API is a little different. Some can be easier to work with than others, for a variety of reasons. In this exercise, you'll choose an API that seems to interesting to you, and figure out how to work with it. You don't need to build a full application with this API, but just build a proof of concept in Django that shows you're able to authenticate and request data from it. 


## Requirements
- Choose an API from [public apis](https://github.com/public-apis/public-apis) that requires some form of Auth (check the third column).
- Read their documentation to figure out how to authenticate to the API, and how to query the API after you've authenticated. 
- Create a simple Django application with at least 2 routes. Each of these routes should query different URLs in the API, and use some of the data they return to render an HTML template so the user can view it.
- Use `python-dotenv` to keep your keys out of your application code. Add your `.env` file to a `.gitignore` to keep it out of git.
- Remember, the main purpose of this exercise is to demonstrate that you can authenticate to an API and get data out of it. You don't need to build out a full, complex application. 


## Resources
- [requests](https://docs.python-requests.org/en/latest/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)