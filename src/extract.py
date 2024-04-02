from typing import Any, Dict, List
from .client import OpenAqApi
import pandas as pd


class Extractor():
    
    def __init__(self) -> None:
       self.client = OpenAqApi()
    
    def extract_data(self, date_from, date_to, limit) -> List[Dict[Any, Any]]:
        """extract air quality data using API client

        Returns:
            json data from APi
        """
        
        params = {'date_from' : date_from, 
                       'date_to' : date_to,
                       'limit': limit}
        
        air_quality = self.client.get_api_request(params = params)
        return air_quality



