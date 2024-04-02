
import pandas as pd
from pandas import json_normalize
from typing import List, Optional, Dict

from sqlalchemy import true

from .model import MeasurementModel


class Transformer:
    def __init__(self, raw_data: List[Dict[str, str]]) -> None:
        """This class transforms extracted data according to the desired model

        Args:
            raw_data (json): extracted data
        """
        self.raw_data = raw_data
    
    
    def transform_json(self) -> List[MeasurementModel]:
        """
        transforms extracted data

        Returns:
           transformed data as a list of model
        """
        air_quality_data = []
        
        for item in self.raw_data:
            transformed_data = self.transform_data(item)
            data_list = transformed_data.to_dict(orient='records')
            air_quality_data.append(data_list)
        print('transformed data successfully')
        
        return air_quality_data
            
    
    def transform_data(self, item: dict)  -> Optional[MeasurementModel] : 
        """transforms and cleans single item of data by renaming and filtering for valid values

        Args:
            item (dict): extracted data

        Returns:
            pd.DataFrame: transformed df
        """
        measurement_data = item['results']
        df = json_normalize(measurement_data)
        
        df = df.rename(columns={'coordinates.latitude': 'latitude', 'coordinates.longitude': 'longitude', 
                                'date.utc': 'date_utc', 'date.local': 'date_local', 'locationId': 'location_id',
                                'isMobile': 'is_mobile', 'isAnalysis': 'is_analysis', 'sensorType': 'sensor_type'})
        df.reset_index(drop=True, inplace=True)
        
        df['id'] = range(1, len(df) + 1)
        
        filtered_df = df[df['value'] >= 0]
        return filtered_df