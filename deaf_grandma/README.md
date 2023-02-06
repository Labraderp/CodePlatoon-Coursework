Deaf Grandma

This small challenge comes from Chris Pine's "Learn to Program". Ensure that you read everything and click every link before starting the work.
Premise

Write a program which can imitate a Grandma who's hard of hearing and follows these constraints:

    If you don't input anything (just hit enter) she responds with WHAT?!

    If you ask a question with any lower-case letters, she responds with SPEAK UP, KID!

    If you talk to her in all upper-case letters, she responds with NO, NOT SINCE 1946!

    The first time you say GOODBYE! she says LEAVING SO SOON?

    The second time you say GOODBYE! she says LATER, SKATER! and the program exits.

Example

HEY KID!
> hi, grandma
SPEAK UP, KID!
> I SAID HI, GRANDMA
NO, NOT SINCE 1946!
>
WHAT?!
> Goodbye!
SPEAK UP, KID!
> GOODBYE!
LEAVING SO SOON?
> GOODBYE!
LATER, SKATER!

Considerations (Python)

    In your code you'll definitely need to use if and likely an elif and else.
    Also remember that input() is the "inverse" method of print() -- while print() outputs information to the terminal, input('command Prompt') captures information from the user by presenting a command prompt and allowing them to type input.
    If you have an infinite loop, how might you break out of it?

Considerations (Javascript)

    In your code you'll definitely need to use if and likely an else if and else.
    This will be hard to do in the terminal with Node.js, because Node.js doesn't have a great built-in prompt.
    This is relatively easy to do in the browser with window.prompt, but you'll need to use an HTML file to run your javascript file.

Challenge Yourself

For a little extra fun, try refactoring your code to use regular expressions.