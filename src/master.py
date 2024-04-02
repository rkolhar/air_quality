from datetime import date
from .extract import Extractor
from .transform import Transformer
from .load import Loader
from .model import create_tables


def run_etl(connection_url: str, date_from: str, date_to: str, limit: int): 
    """_summary_

    Args:
        connection_url (str): postgres connection url
        date_from (str): extract data from current_date - 1 
        date_to (str):  extract data from current_date 
        limit (int): 500
    """
  
    create_tables(connection_url)
    extractor = Extractor()
    raw_data = extractor.extract_data(date_from, date_to, limit)

    transformer = Transformer(raw_data)
    
    loader = Loader(transformer.transform_json(), connection_url=connection_url)
    loader.load_data()

    