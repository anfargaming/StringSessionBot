 # Import the necessary modules
from sqlalchemy import Column, BigInteger, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base for the SQLAlchemy ORM
Base = declarative_base()

# Define the "users" table
class Users(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BigInteger, primary_key=True)
    channels = Column(BigInteger)

    def __init__(self, user_id, channels=None):
        self.user_id = user_id
        self.channels = channels

# Connect to the database and create the table if it doesn't exist
engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine, checkfirst=True)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to return the number of users in the "users" table
def num_users():
    try:
        return session.query(Users).count()
    finally:
        session.close()
