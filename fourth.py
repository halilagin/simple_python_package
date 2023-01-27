
#__name__=__main__
def f():
    print("fer")
    return "fret"


#executed when you call it and when you import it
print("importing", f())



# this will be only executed when you call the file, not executed when imported
if __name__=="__main__":
    f()


