import joblib
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
x= pd.read_csv('x.csv')
y=pd.read_csv('y.csv')
df= pd.read_csv('df_clean.csv')
#columns == ['location', 'total_sqft', 'bath', 'balcony', 'price', 'bhk_alt']

#import model from joblib file made in jupyter notebook

model_lr = joblib.load('model_lr.joblib')

def predict_price(location,sqft,bath,balcony,bhk):

    loc_index = np.where(x.columns==location)


    xp = np.zeros(len(x.columns))
    xp[0] = sqft
    xp[1] = bath
    xp[2] = balcony
    xp[3] = bhk
    if type(loc_index) == int:
        xp[loc_index[0][0]] = 1



    return int(model_lr.predict([xp])[0])

# print(predict_price('1st Phase JP Nagar', 1875,3,1,3))
# print(y.iat[0,0])

def predict():
    location_val = location.get()
    sqft_val = area.get()
    bath_val = bath.get()
    balcony_val = balcony.get()
    bhk_val = bhk.get()
    val = predict_price(location_val,sqft_val,bath_val,balcony_val,bhk_val)
    price.delete('0.0', tk.END)
    if val<100:
        price.insert('0.0', f'{val} lakh')
    else:
        price.insert('0.0', f'{val/100} crore')



#tkinter gui


root= tk.Tk()
root.geometry('600x500')
root.title('real estate price predictor')


location_label = tk.Label(root, text= 'Location:')
area_label = tk.Label(root, text= 'Area in sqft:')
bhk_label = tk.Label(root, text= 'Bedrooms:')
balcony_label = tk.Label(root, text= 'Balconies:')
bath_label = tk.Label(root, text= 'Bathrooms:')
price_label= tk.Label(root, text='Predicted price:')

location_label.grid(row= 0, column=0, padx=0, pady=10)
area_label.grid(row= 1, column=0, padx=0, pady=10)
bhk_label.grid(row= 2, column=0, padx=0, pady=10)
balcony_label.grid(row= 3, column=0, padx=0, pady=10)
bath_label.grid(row= 4, column=0, padx=0, pady=10)
price_label.grid(row=6, column=0,padx=0, pady=10)




location = ttk.Combobox(root, values= list(df.location.unique()))
location.current(159)
location.grid(row=0, column=1, padx=0)

area= tk.Scale(root, from_=0, to=20000, orient= tk.HORIZONTAL, tickinterval=20000, sliderlength= 20,length= 300)
area.grid(row=1, column=1, padx=10)

# area= tk.Entry(root)
# area.grid(row=1, column=1, padx=10)

bhk= tk.Scale(root, from_=0, to=15, orient= tk.HORIZONTAL, tickinterval=15, sliderlength= 20,length= 150)
bhk.grid(row=2, column=1, padx=0)

balcony= tk.Scale(root, from_=0, to=15, orient= tk.HORIZONTAL, tickinterval=15, sliderlength= 20,length= 150)
balcony.grid(row=3, column=1, padx=0)

bath= tk.Scale(root, from_=0, to=15, orient= tk.HORIZONTAL, tickinterval=15, sliderlength= 20,length= 150)
bath.grid(row=4, column=1, padx=0)


button = tk.Button(root, text='predict',height= 1, width=10,bg= 'white' ,command=predict)
button.grid(row= 5, column= 1, pady=10)

price = tk.Text(root, height = 1, width = 20)
price.grid(row= 6, column=1, pady=10)

root.mainloop()


