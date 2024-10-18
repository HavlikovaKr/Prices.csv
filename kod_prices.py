# # Kódování hrubých dat s pomocí ChatGPT 
import csv  

hour = ";1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24; "  
price = "111,03;    99,00;    92,00;    88,71;    84,72;    81,37;    99,95;   140,41;   155,49;   110,01;    90,00;    79,90;    70,10;    58,11;    61,95;    66,95;    70,00;    71,35;    82,44;   100,80;   109,01;    90,69;    81,37;    80,57;"  

# ÚPRAVA  PŘEVOD
price = [float(x.strip().replace(',', '.')) for x in price.split(';') if x.strip()]  
hour = [int(x) for x in hour.split(';') if x.isdigit()]  

# print(hour)  
# print(price)  

price_dict = dict(zip(hour, price))  
# print(price_dict)  

# CSV soubor
csv_file = 'prices.csv'  

with open(csv_file, mode='w', newline='') as file:  
    writer = csv.writer(file, delimiter=',')   
    writer.writerow(['Hour', 'Price(EUR/MWh)'])    
    for hour, price in price_dict.items():  
        writer.writerow([hour,price])   


print("Data byla úspěšně zapsána do souboru.")   


# ================================================================

#CHAT GPT  
# hour = list(range(1, 25)) 
# price = [111.03, 99.00, 92.00, 88.71, 84.72, 81.37, 99.95, 140.41, 155.49, 110.01, 90.00, 79.90, 70.10, 58.11, 61.95, 66.95, 70.00, 71.35, 82.44, 100.80, 109.01, 90.69, 81.37, 80.57] 

# # Vytvoření slovníku 
# price_dict = dict(zip(hour, price)) 
# # print(price_dict) 

# # CSV soubor. 
# csv_file = 'prices.csv' 

# with open(csv_file, mode='w', newline='') as file: 
#     writer = csv.writer(file, delimiter=',')
#     writer.writerow(['Hour', 'Price(EUR/MWh)'])   
#     for hour, price in price_dict.items(): 
#         writer.writerow([hour, price])  

# print("Data byla úspěšně zapsána do souboru.") 

 