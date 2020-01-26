class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('hackaton.db')
        self.create_user_table()
        self.createProject()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          Day boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXIST "Users"(
         id INTEGER PRIMARY KEY,
         Name TEXT,
         Email VARCHAR(320),
         PSSWD TEXT,
         CreatedOn Date DEFAULT CURRENT_DATE
        );
        """
        # create user table in similar fashion
        # come on give it a try it's okay if you make mistakes

class UserModel:
    TABLENAME = "USERS"

    def __init__(self):
        self.conn = sqlite3.connect('hackaton.db')

    def create(self, text, description):
        query = f'insert into {TABLENAME} ' \
                f'(Name, Email, PSSWD) ' \
                f'values ("{name}","{email},{psswd}")'
        
        result = self.conn.execute(query)
        return result
   # Similarly add functions to select, delete and update todo








