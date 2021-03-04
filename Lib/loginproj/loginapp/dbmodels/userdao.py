from django.db import connection
from .user import *
from .dbfactory import *
#for password hash
from django.contrib.auth.hashers import *

#dao design pattern
class UserDAO:

    def getDBCursor(self):
        c=DBFactory.getInstance().getDBCursor()
        return c

    def insertUser(self, u):
        c=self.getDBCursor()
        try:
            c.execute("INSERT INTO users VALUES(%s,%s)",[u.getEmail(), make_password(u.getPw())]) #security SQL injection block
            return True
        except:
            return False
        finally:
            c.close()

    def authenticate_user(self, u):
        c=self.getDBCursor()
        try:
            c.execute("SELECT pass FROM users WHERE email=%s",[u.getEmail()]) #security SQL injection block
            ret=c.fetchall() #list of tuple
            if len(ret)==1:
                print("yes")
                row=ret[0]
                auth=check_password(u.getPw(), row[0])
                if auth is True:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False
        finally:
            c.close()




# scnario:
#
# sign up:
# password = 1234 #don't save directly in db
# hash(1234) = aljfdaljfalfjaljflasjfasljfalj #break supercomputer
#
#
# login:
# pass = 1234
# hash(1234)=aljfdaljfalfjaljflasjfasljfalj
#
# pass = aljfdaljfalfjaljflasjfasljfalj
