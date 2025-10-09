"""orm.py: sqlalchemy orm used to manage the Professors table"""
from db.server import get_session
from db.schema import Professor

"""Lab 4 - Part 2:
- Insert 3 records into the Professors table
- Update 1 record in the Professors table
- Delete 1 record in the Professors table
"""

def get_all_professors():
    """Select all records from the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # get all entries in the Professors table
        professors = session.query(Professor).all()
        return professors
    
    finally:
        session.close()

def insert_professors():
    """Insert 3 records into the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        prof1 = Professor(FirstName='Calista', LastName='Phippen', Email='Calista.Phippen1@Marist.edu')
        prof2 = Professor(FirstName='Bob', LastName='Johnson', Email='bob.johnson@example.com')
        prof3 = Professor(FirstName='Carol', LastName='Williams', Email='carol.williams@example.com')
        session.add_all([prof1, prof2, prof3])
        # "save" the changes
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error inserting professors:", e)

    finally:
        session.close()

def update_professor():
    """Update one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        professor = session.query(Professor).filter_by(FirstName='Carol', LastName='Williams').first()

        if professor:
            professor.Email = 'carol.williams@Marist.edu'
            session.commit()
        else:
            print("Professor not found")
        # "save" the changes
        session.commit()
    
    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)
        
    finally:
        session.close()

def delete_professor():
    """Delete one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        professor = session.query(Professor).filter_by(FirstName='Bob', LastName='Johnson').first()

        if professor:
            session.delete(professor)
            session.commit()
        else:
            print("Professor not found")
        # "save" the changes
        session.commit()

    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)

    finally:
        session.close()

