# -*- coding: utf-8 -*-
'''
MetMast
-------

A straightforward met mast import class built with the pandas library

'''
import pandas as pd
from pandas import DataFrame

class MetMast(object): 
    '''Subclass of the pandas dataframe built to import and quickly analyze
       met mast data.'''
       
    def __init__(self, lat=None, lon=None, height=None, time_zone=None):
        '''Data structure with both relevant information about the mast
        itself (coordinates, height, time zone), as well as methods to process
        the met mast data and manipulate it using tools from the pandas
        library. 
        
        Parameters
        ----------
        lat: float, default None
            Latitude of met mast
        long: float, default None
            Longitude of met mast
        height: float or int, default None
            Height of met mast
        time_zone: string
            Please follow the pytz time zone conventions: 
            http://pytz.sourceforge.net/
        '''
        self.lat = lat
        self.lon = lon
        self.height = height
        self.time_zone = time_zone
        
    def wind_import(self, path, header_row=None, time_col=None,
                    delimiter=None, **kwargs):
        '''Wind data import. This is a very thin wrapper on the pandas read_table 
        method, with the option to pass keyword arguments to pandas read_table 
        if needed. 
    
        Parameters:
        ----------
        path: string
            Path to file to be read
        header_row: int
            Row containing columns headers
        time_col: int
            Column with the timestamps
        delimiter: string
            File delimiter
    
        Returns: 
        --------
        DataFrame with wind data
        '''
        self.data = pd.read_table(path, header=header_row, index_col=time_col, 
                                  parse_dates=True, delimiter=delimiter,
                                  **kwargs)
                                  
    def mean_ws(time_period='all'):
        '''
        Averaging of mean wind speed
        '''
        pass 
        
    def sectorwise(sectors=12, **kwargs):
        '''Bin the wind data sectorwise
        '''
        pass
        # if not self.data:
            # print(("You have not imported any data. Use the 'wind_import'"
                    # "method to load data into your object"))
        # cuts = 360/sectors
        # bins = [0, cuts/2]
        # bins.extend(range(cuts, 360, cuts))
        # bins.extend([360-cuts/2, 360])
        # cats = pd.cut(self.data['Average Direction'], bins, right=False)
        # array = pd.value_counts(cats)
        
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  