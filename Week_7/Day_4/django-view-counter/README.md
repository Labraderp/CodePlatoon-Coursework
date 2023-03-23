# Django View-counter

For this exercise, you'll build a simple django application that counts how many times a user has visited the home page. 


## Requirements
- Create a global dictionary called `users` to track view counts for different users.
- When a user requests the root route `/` for the first time,
    - create a random user_id
    - set a cookie using `response.set_cookie('user_id', '<user_id value>')`
    - update the global `users` dictionary to track this user, and their views. 
    - render a template for the home page. Use variable interpolation in django templates to tell the user that they've visited the page 1 time. 
- When a user returns after their first visit, 
    - check their user_id from their cookie, using `request.COOKIES.get('user_id')`
    - update the global users dictionary to increment that user's view count.
    - render a template for the home page. Use variable interpolation in django templates to tell the user how many times they've visited that page.
- To test the application,
    - open the app in a new tab, and confirm that it starts counting from zero, and increments by 1 every time you refresh the page. 
    - open the app in a new incognito window, and confirm that it again starts counting from zero, and increments by 1 every time you refresh the page. 
    - You should be able to refresh your incognito window, and your regular window, and see two independent counts being incremented. This is because the incognito window does not share cookies with your main browser window, so the app sees this as a different user. 