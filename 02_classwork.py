electricity_bill = [150,90,87,200,136,345,230,180,156,200,90,102]
total_bill = electricity_bill[0] + electricity_bill[1] + electricity_bill[2] + electricity_bill[3] + electricity_bill[4] + electricity_bill[5] + electricity_bill[6] +electricity_bill[7] + electricity_bill[8] + electricity_bill[9] + electricity_bill[10]+ electricity_bill[11]
print(f"The total electricity bill from january to december is: {total_bill}")

average_bill = (total_bill/12)
print(f"The average electricity bill per month is: {average_bill}")
