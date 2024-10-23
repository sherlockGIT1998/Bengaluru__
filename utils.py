import pickle 
import json
import pandas as pd   
import numpy as np 
import warnings
warnings.filterwarnings('ignore')
import config 

class BengaluruHousePrice():
    
    def __init__(self,area_type,availability,location,size,total_sqft,bath,balcony):
        
        self.area_type_col = 'area_type_'+ area_type
        self.availability = availability
        self.location = location
        self.size_col = 'size_'+ size
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f:
            
            self.save_data = json.load(f)
        
    def get_predicted_price(self):
        
        self.load_models()
        
        area_type_index = np.where(self.save_data == self.area_type_col)[0]
        size_index = np.where(self.save_data ==self.size_col)[0]
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.save_data['availability'][self.availability]
        array[1] = self.save_data['location'][self.location]
        array[2] = self.total_sqft
        array[3] = self.bath
        array[4] = self.balcony
        array[area_type_index] = 1
        array[size_index] = 1
        print('Array :',array)
        
        prediction = self.model.predict([array])[0]
        
        return prediction
    
if __name__ == '__main__':
    
    availability = '19-Dec'
    location = 'Electronic City Phase II'
    total_sqft = '1056.0'
    bath = 2.0
    balcony = 1.0

    area_type = 'Built-up Area'
    size = '1 BHK'

    house_price = BengaluruHousePrice(area_type,availability,location,size,total_sqft,bath,balcony)
    
    prediction = house_price.get_predicted_price()
    
    print(f'Price of House is Rs {round(prediction,2)} Lakh /-')