from sqlite3 import connect
db = connect("myDatabase.db")
LIST = ['name', 'actor', 'actress', 'director', 'year']
HELP = """
ENTER THE VALUE FOR OPTION
--------------------------
1] SHOW ALL VALUE
2] SEARCH DATA BY VALUE
3] INSERT DATA
Q] QUIT
--------------------------
"""


try:
    db.execute("CREATE TABLE movie(name , actor, actress, director,year);")
    db.commit()
except:
    pass



def main(n=''):
    while(n != 'q'):
        print(HELP)
        n = input("OPTION:> ")
        if(n ==  '1'):
            try:
                for r in db.execute("SELECT * FROM movie;"):
                    for c in r:
                        print(f"{c:<12}", end="")
                    print()
            except:
                print()
        if(n ==  '2'):
            try:
                c = input("Enter Column name:")
                while(c not in LIST):
                    print("Enter Among option:\n", LIST)
                    c = input("Enter Column name:")
                r = input("Enter the value to search:")
                for r in db.execute(f"SELECT * FROM movie WHERE {c}=\"{r}\";"):
                    for c in r:
                        print(f"{c:<12}", end="")
                    print()
            except:
                print()
        elif(n == '3'):
            name = input("Enter Name of the movie:")
            actor = input("Enter actor name:")
            actress = input("Enter actress Name:")
            director = input("Enter director name:")
            year = input("Enter year of relise:")
            if(name and actor and actress and director and year):
                db.execute(f"INSERT INTO movie VALUES(\"{name}\",\"{actor}\",\"{actress}\",\"{director}\",\"{year}\");")
                db.commit()
            else:
                print("Please enter all fields")

main()
