import pandas as pd

### Basic Instantiation

class Complex():
    def __init__(self,name,address,rating,num_of_reviews):
        self.name = name
        self.address = address
        self.rating = rating
        self.num_of_reviews = num_of_reviews
    def __str__(self):
        print(self.name)

complex_objects = {}
failed_complexes = []

### Read in complex names
housing_df = pd.read_csv("/Users/nicholasoxenden/Oxenden/Programming/Scrapy/housing/complex_list.csv")
complex_names = housing_df['complex_name']
