dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename = dbfilename):
    "store db in the file"
    dbfile = open(dbfilename, 'w')
    for key in db:
        dbfile.write(key + '\n')
        for (name, value) in db[key].items():
            print(name + RECSEP +repr(value), file=dbfile) #repr allows me to save exact same data such as int or none
        print(ENDREC, file = dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()

def loadDbase(dbfilename=dbfilename):
    "restore the data"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input("Key input")
    while key != ENDDB:
        rec = {}
        field = input()
        while field!= ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value) #same here, but now i can read it correctly
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__=='__main__':
    from initdata import db
    storeDbase(db)

        
    
