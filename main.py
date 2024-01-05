import os
from dotenv import load_dotenv
from sqlmodel import Session, select, or_

load_dotenv()

import database

if __name__ == "__main__":
    database.create_tables()
    session =  Session(database.engine)

    # ! 1. how to select a multiple rows from our data
    # statement = select(database.models.Session)
    # result = session.exec(statement)

    # ! 2. how to filter the data
    # statement = select(database.models.Session).where(or_(database.models.Session.is_dm == False, database.models.Session.channel_id == "12345"))
    # print(statement)
    # result = session.exec(statement).all()
    # print(result)

    # ! 3. how to select a single row from our data
    statement = select(database.models.Session).where(database.models.Session.id == 1)
    print(session.exec(statement).first()) # get the first
    print(session.exec(statement).one_or_none()) # ensure only one or none
    print(session.exec(statement).one()) # ensure only one

    # ! 4. selecting based of id
    # session_1 = session.exec(select(database.models.Session).where(database.models.Session.id == 1)).one()
    session_2 = session.get(database.models.Session, 1)
    # session_3 = session.get(database.models.Session, 0) # none
    # print(session_2, session_3)

    # ! 5. how to create a message with a relationship to a session
    # message = database.models.Message(author="kdt", text="hello", session_id=session_2.id)
    # session.add(message)
    # session.commit()
    # session.refresh(message)
    # print(message)
    # print(message.session)

    # message2 = database.models.Message(author="jaz", text="hello", session=session_2)
    # session.add(message2)
    # session.commit()
    # session.refresh(message2)
    # print(message2)
    # print(message2.session)
    
    # ! 6. how to edit & delete
    # session_2.channel_id = "54321"
    # session.add(session_2)
    # session.commit()

    message = session.get(database.models.Message, 1)
    # message.session_id = 3
    # session.add(message)
    # session.commit()
    # session.refresh(message)

    # print(message)

    session.delete(message)
    session.commit()
