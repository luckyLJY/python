import dbm
with dbm.open('mydb','c') as db:
    db['name'] = 'tony'
    print(db['name'].decode())

    age = int(db.get('age',b'18').decode())
    print(age)

    if 'age' in db:
        db['age'] = '20'
    del db['name']