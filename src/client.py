from typing import Dict, List, Any
from datetime import date
import requests


class OpenAqApi:
    
    def __init__(self) -> None:
        """_summary_

        Args:
            access_key (_type_): _description_
        """
        self.base_url = "https://api.openaq.org/"
        self.headers = {"accept": "application/json",
                    "content-type": "application/json"}
        
        
    def get_api_request(self, params: dict ) -> List[Dict[Any, Any]]:
        """_summary_

        Args:
            url (str): _description_
            params (Dict): _description_

        Returns:
            List[Dict[Any, Any]]: _description_
        """
        result_list = []
        url =  f'{self.base_url}/v2/measurements'
        try:
            with requests.get(url=url, params=params, headers=self.headers) as response:
                response.raise_for_status()
                
                result = response.json()
                result_list.append(result)       
            
        except ConnectionError as e:
            print('Exception',  e)
        
        except requests.exceptions.RequestException as e:
            print('Exception',  e)
        finally:
            return result_list
    
            
        