from Database import Database


class FastBrain(object):
    def __init__(self, user, password, host, database):
        self.number = None
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def FBsearch(self,d):
        self.number = d
        FBdatabase = Database(self.user, self.password, self.host, self.database)
        FBdatabase.connect()
        return FBdatabase.search(self.number)

    def addit(self):
        FBdatabase = Database(self.user, self.password, self.host, self.database)
        FBdatabase.connect()
        FBdatabase.input(self.number)
        return True
