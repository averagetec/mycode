def main():
    
    lilstring  = "Alta3 Research offers classes on Python coding"
    #make a list
    newlist = lilstring.split(" ")
    print(newlist)

    myiplist = ["192", "168", "0", "12"]
    #make a string 
    singleip = ".".join(myiplist)
    print(singleip) 
    dir(singleip)
    dir(myiplist)
main()
