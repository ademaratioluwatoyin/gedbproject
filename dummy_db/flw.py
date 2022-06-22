from model import * 

Flutterwave = Company("Flutterwave", "Payment")

Flutterwave.overview =  """
Flutterwave provides a payment service for global merchants and payment service providers. It provides technology, infrastructure, and services to enable global merchants, payment service providers, and helps banks and businesses build secure and seamless payment solutions for their customers by smoothening the exchange of funds. 
\nThe company was founded in 2016 by Iyinoluwa Aboyeji and Olugbenga Agboola and is headquartered in San Francisco, California.
"""

employees_count = Info('Qualitative', 'Team', "Employees", "255")
total_funding = Info('Quantitative', 'Funding', "Total Funding Amount", "$474.5M")

Flutterwave.addInfo([employees_count, total_funding])


