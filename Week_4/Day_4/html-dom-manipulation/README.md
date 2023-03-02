# DOM Manipulation: Replace Images

This is a walkthrough of a [tutorial exercise from Eloquent Javascript](https://eloquentjavascript.net/14_dom.html#h_AlX6HES+2D)

You will improve your skills at manipulating the DOM and using DOM events to execute your JS code when a button is clicked!

**Review the tutorial in the link above before doing this walkthrough! They are the same : )**

This is also a very practical exercise, as you will learn about the `<img>` element's `alt` attribute, which is used when the browser is unable to download there desired image, or for accessibility purposes.
1. Create a very simple HTML page with at least three images on it.
2. Add the alt attribute with explanatory text to each of their images, if they haven’t.
3. Create an external JS file and add it to the document with a `<script>` tag.
5. Add a `<button>` to your HTML page.
6. In your JS file create a function named “replaceImages”, and use HTML element attribute `onclick` so that clicking on the button calls your function! Use console.log to confirm this works.
7. In your function, write some code using `document.body.getElementByTagName` to get all `<img>` tags, and then console.log the results to confirm your code works (be sure to check your devtools console).
8. Now, console.log the `alt` attribute of each `<img>` tag.
9. Finally, use document.createTextNode to create a "text node" (which will render as a string) which we’ll replace the <img> tag with. Use the `.parentNode()` and `.replaceChild()` DOM node methods to do this! **Look at the tutorial for an example of this**.