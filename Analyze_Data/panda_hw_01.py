import pandas as pd
import numpy as np

def print_head_tail():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
    auto_df = pd.read_csv(url)
    print(auto_df.head(5))
    print(auto_df.tail(5))
    
def rename_na_Nan():
    url = 'Automobile_data.csv'
    auto_df = pd.read_csv(url)
    auto_df = auto_df.replace({"?":np.nan})
    print(auto_df.head(10))
    
def max_value_car():
    url = 'Automobile_data.csv'
    auto_df = pd.read_csv(url)
    auto_df.sort_values('price',inplace=True)
    filter = auto_df['price'] == auto_df['price'].max()
    pricy_car = auto_df.where(filter).dropna()
    print(pricy_car)
    
def print_toyota_cars():
    url = 'Automobile_data.csv'
    auto_df = pd.read_csv(url)
    auto_df.sort_values('company',inplace=True)
    filter = auto_df['company'].str.upper() == "TOYOTA"
    toyota_car = auto_df.where(filter).dropna()
    print(toyota_car)
    
def count_by_company():
    url = 'Automobile_data.csv'
    auto_df = pd.read_csv(url)
    auto_df.sort_values('company',inplace=True)
    auto_df.dropna(inplace = True)
    print(auto_df['company'].value_counts())    

def pricy_car_by_company():
    url = 'Automobile_data.csv'
    auto_df = pd.read_csv(url)
    auto_df.sort_values('company',inplace=True)
    auto_df.dropna(inplace = True)
    company_group = auto_df.groupby('company')
    pricy_car = company_group[['company','price']].max()
    print(pricy_car) 

def avg__miles_car_by_company():
    url = 'Automobile_data.csv'
    auto_df = pd.read_csv(url)
    auto_df.sort_values('company',inplace=True)
    auto_df.dropna(inplace = True)
    company_group = auto_df.groupby(['company','body-style'])
    avg_miles = company_group[['company','body-style','average-mileage']].mean()
    print(avg_miles)   

def sort_cars_by_price():
    url = 'Automobile_data.csv'
    auto_df = pd.read_csv(url)
    auto_df.sort_values('price',ascending=False,inplace=True)
    auto_df.dropna(inplace = True)
    print(auto_df)     
    
def concat_two_df():
    GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
    japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
    gcars = pd.DataFrame.from_dict(GermanCars)
    jcars = pd.DataFrame.from_dict(japaneseCars)
    all_cars = pd.concat([gcars,jcars], keys=["Germany", "Japan"])
    print(all_cars)

    
def main():
    #print_head_tail()
    #rename_na_Nan()
    #max_value_car()
    #print_toyota_cars()
    #count_by_company()
    #pricy_car_by_company()
    #avg__miles_car_by_company()
    #sort_cars_by_price()
    concat_two_df()
    
if __name__ == "__main__":
    main()
    

