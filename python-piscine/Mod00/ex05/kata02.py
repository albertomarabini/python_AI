# Tuple
kata = (2019, 9, 25, 3, 30)

def format_datetime(dt):
    return f"{dt[1]:02d}/{dt[2]:02d}/{dt[0]} {dt[3]:02d}:{dt[4]:02d}"

# Calling the function and printing the result
formatted_date = format_datetime(kata)
print(formatted_date)