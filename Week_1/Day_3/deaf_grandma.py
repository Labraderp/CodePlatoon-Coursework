def deaf_grandma(resp):
    #Blank case
    if resp == '':
        resp = input("WHAT?!")
        deaf_grandma(resp)
    #CAPS case
    if resp.isupper():
        #GOODBYE! case
        if resp == "GOODBYE!":
            resp = input("LEAVING SO SOON?")

            if resp == "GOODBYE!":
                print("LATER, SKATER!")
                return
            else:
                deaf_grandma(resp)

        #CAPS, NOT GOODBYE
        else:
            resp = input("NO, NOT SINCE 1946!")
            deaf_grandma(resp)

    #Lowercase
    else:
        resp = input("SPEAK UP, KID!")
        deaf_grandma(resp)
        return

resp = input("HEY KID!" )
deaf_grandma(resp)