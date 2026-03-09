import pandas as pd
import numpy as np
def create_dummy_data():
    states=['A', 'B', 'C', 'D', 'E']
    years=list(range(2010, 2021))
    data=[]
    for state in states:
        for year in years:
            base_sales=100+(year-2010)*5
            noise=np.random.normal(0, 2)
            sales=base_sales+noise
            data.append([state, year, sales])
    df=pd.DataFrame(data, columns=['State', 'Year', 'Sales'])
    treatment_effect=25
    df.loc[(df['State']=='A')&(df['Year']>=2016), 'Sales']+=treatment_effect
    df.to_csv('marketing_data.csv', index=False)
    print("Data generated and saved to 'marketing_data.csv' ")
if __name__=="__main__":
    create_dummy_data()