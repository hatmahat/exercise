import re

flight = 'Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT'

'''
"Here you have your boarding pass LA4214 AER-CDB 06NOV"
> The two letters indicate the airline (LA)
> The 4 numbers are the flight number (4214)
> The three letters correspond to the depature (AER)
> The destination (CBD)
> The date (06NOV)
'''

regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

flight_matches = re.findall(regex, flight)

print(
    'Arline: {}, Flight number: {}'.format(
        flight_matches[0][0], 
        flight_matches[0][1]
    )
)

print(
    'Depature: {}, Destination: {}'.format(
        flight_matches[0][2],
        flight_matches[0][3]
    )
)

print(
    'Date: {}'.format(
        flight_matches[0][4]
    )
)