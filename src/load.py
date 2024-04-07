
from .model import MeasurementOrm, MeasurementModel
from sqlalchemy import create_engine, exists, select
from sqlalchemy.orm import Session, sessionmaker
from typing import List


def connect(connection_url: str) -> Session:
    """_summary_

    Args:
        connection_url (str): _description_

    Returns:
        _type_: _description_
    """
    Session = sessionmaker()
    Session.configure(bind=create_engine(connection_url, echo = True))
    return Session()


class Loader:
    def __init__(self, air_quality_data: List[MeasurementModel], connection_url: str) -> None:
        self.session = connect(connection_url)
        self.air_quality_data = air_quality_data
    
    
    def check_if_id_exists(self, item_id):
    #    print(self.session.query(MeasurementOrm).filter(MeasurementOrm.id == item_id))
        return self.session.query(MeasurementOrm).filter(MeasurementOrm.id == item_id).first() is not None
    
    def load_data(self):
        try:
            for item in self.air_quality_data: # [0]
            #    print(item)
                if self.check_if_id_exists(item['id']):
                    print("Data already present. Skipping...")
                    break
                else:
                    air_instance = MeasurementOrm(**item)
                    self.session.add(air_instance)
                self.session.commit()
                print("Data inserted successfully.")
    
        except Exception as e:
            print(f"Error adding data for item {item}: {e}")
            self.session.rollback()
            raise NotImplementedError

        finally:
            self.session.close()
            
        