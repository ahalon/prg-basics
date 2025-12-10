hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]


def hotel_list(hotels):
    return ", ".join([hotel["name"] for hotel in hotels])

def avg_price(hotels):
    if not hotels:
        return 0
    
    total_price = sum(hotel["price"] for hotel in hotels)
    avarage = total_price/len(hotels)
    return round(avarage)

krakow_names = hotel_list(hotels_in_Krakow)
krakow_avg = avg_price(hotels_in_Krakow)

sopot_names = hotel_list(hotels_in_Sopot)
sopot_avg = avg_price(hotels_in_Sopot)

if krakow_avg < sopot_avg:
    cheaper_city = "Kraków"
elif sopot_avg < krakow_avg:
    cheaper_city = "Sopot"
else:
    cheaper_city = "W obu miastach ceny są równe"

print(f"Hotels in Krakow: {krakow_names}")
print(f"Average hotel price in Krakow: {krakow_avg}")

print(f"\nHotels in Sopot: {sopot_names}")
print(f"Average hotel price in Sopot: {sopot_avg}")

print(f"\nCheaper hotels in: {cheaper_city}")