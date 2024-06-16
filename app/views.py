from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def render_news_website(request):
  
  json_data = [
    {
      "symbol": "AAPL",
      "name": "Apple Inc.",
      "price": 142.45,
      "change": -1.23,
      "percent_change": -0.85,
      "volume": 25678432,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "GOOGL",
      "name": "Alphabet Inc.",
      "price": 2731.20,
      "change": 12.45,
      "percent_change": 0.46,
      "volume": 1568945,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "MSFT",
      "name": "Microsoft Corporation",
      "price": 378.90,
      "change": 5.67,
      "percent_change": 1.52,
      "volume": 20378456,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "AMZN",
      "name": "Amazon.com Inc.",
      "price": 3298.50,
      "change": -18.75,
      "percent_change": -0.57,
      "volume": 3987456,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "TSLA",
      "name": "Tesla Inc.",
      "price": 679.40,
      "change": 8.20,
      "percent_change": 1.22,
      "volume": 7845963,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "NVDA",
      "name": "NVIDIA Corporation",
      "price": 315.75,
      "change": -2.15,
      "percent_change": -0.68,
      "volume": 5698741,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "FB",
      "name": "Meta Platforms Inc.",
      "price": 345.60,
      "change": 6.75,
      "percent_change": 1.99,
      "volume": 2345678,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "NFLX",
      "name": "Netflix Inc.",
      "price": 412.30,
      "change": -3.45,
      "percent_change": -0.83,
      "volume": 1789456,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "CRM",
      "name": "Salesforce.com Inc.",
      "price": 260.15,
      "change": 4.20,
      "percent_change": 1.64,
      "volume": 1324567,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "PYPL",
      "name": "PayPal Holdings Inc.",
      "price": 285.80,
      "change": 0.90,
      "percent_change": 0.32,
      "volume": 2456789,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "V",
      "name": "Visa Inc.",
      "price": 234.75,
      "change": -1.50,
      "percent_change": -0.63,
      "volume": 1894567,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "NVDA",
      "name": "NVIDIA Corporation",
      "price": 315.75,
      "change": -2.15,
      "percent_change": -0.68,
      "volume": 5698741,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "INTC",
      "name": "Intel Corporation",
      "price": 56.30,
      "change": 0.25,
      "percent_change": 0.45,
      "volume": 3456789,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "ADBE",
      "name": "Adobe Inc.",
      "price": 600.80,
      "change": 9.30,
      "percent_change": 1.57,
      "volume": 987654,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "CSCO",
      "name": "Cisco Systems Inc.",
      "price": 52.10,
      "change": 0.90,
      "percent_change": 1.76,
      "volume": 234567,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "QCOM",
      "name": "Qualcomm Inc.",
      "price": 148.25,
      "change": 1.60,
      "percent_change": 1.09,
      "volume": 456789,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "IBM",
      "name": "International Business Machines Corporation",
      "price": 123.80,
      "change": -0.75,
      "percent_change": -0.60,
      "volume": 567890,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "BABA",
      "name": "Alibaba Group Holding Limited",
      "price": 210.60,
      "change": -3.40,
      "percent_change": -1.59,
      "volume": 678901,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "PG",
      "name": "Procter & Gamble Co.",
      "price": 138.90,
      "change": 2.10,
      "percent_change": 1.54,
      "volume": 789012,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "PFE",
      "name": "Pfizer Inc.",
      "price": 47.20,
      "change": -0.30,
      "percent_change": -0.63,
      "volume": 890123,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "KO",
      "name": "The Coca-Cola Company",
      "price": 56.80,
      "change": 0.10,
      "percent_change": 0.18,
      "volume": 901234,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "NFLX",
      "name": "Netflix Inc.",
      "price": 412.30,
      "change": -3.45,
      "percent_change": -0.83,
      "volume": 1789456,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "MRNA",
      "name": "Moderna Inc.",
      "price": 195.60,
      "change": 1.20,
      "percent_change": 0.62,
      "volume": 1122334,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "SPOT",
      "name": "Spotify Technology S.A.",
      "price": 235.40,
      "change": 4.50,
      "percent_change": 1.95,
      "volume": 1456789,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "ABNB",
      "name": "Airbnb Inc.",
      "price": 172.30,
      "change": -0.80,
      "percent_change": -0.46,
      "volume": 223344,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "NKE",
      "name": "Nike Inc.",
      "price": 152.70,
      "change": 2.80,
      "percent_change": 1.87,
      "volume": 334455,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "AMD",
     

 "name": "Advanced Micro Devices Inc.",
      "price": 102.80,
      "change": -0.50,
      "percent_change": -0.48,
      "volume": 556677,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "F",
      "name": "Ford Motor Company",
      "price": 15.60,
      "change": 0.15,
      "percent_change": 0.97,
      "volume": 112233,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "GM",
      "name": "General Motors Company",
      "price": 67.40,
      "change": -0.20,
      "percent_change": -0.30,
      "volume": 445566,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "SBUX",
      "name": "Starbucks Corporation",
      "price": 98.50,
      "change": 1.10,
      "percent_change": 1.13,
      "volume": 667788,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "CRM",
      "name": "Salesforce.com Inc.",
      "price": 260.15,
      "change": 4.20,
      "percent_change": 1.64,
      "volume": 1324567,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "MCD",
      "name": "McDonald's Corporation",
      "price": 245.80,
      "change": -0.40,
      "percent_change": -0.16,
      "volume": 778899,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "WMT",
      "name": "Walmart Inc.",
      "price": 140.20,
      "change": -0.80,
      "percent_change": -0.57,
      "volume": 889900,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "PYPL",
      "name": "PayPal Holdings Inc.",
      "price": 285.80,
      "change": 0.90,
      "percent_change": 0.32,
      "volume": 2456789,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "VZ",
      "name": "Verizon Communications Inc.",
      "price": 55.30,
      "change": -0.10,
      "percent_change": -0.18,
      "volume": 345678,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "T",
      "name": "AT&T Inc.",
      "price": 28.90,
      "change": 0.05,
      "percent_change": 0.17,
      "volume": 456789,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "ORCL",
      "name": "Oracle Corporation",
      "price": 82.60,
      "change": 1.20,
      "percent_change": 1.47,
      "volume": 567890,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "BA",
      "name": "The Boeing Company",
      "price": 215.30,
      "change": -1.50,
      "percent_change": -0.69,
      "volume": 678901,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "HD",
      "name": "The Home Depot Inc.",
      "price": 320.40,
      "change": -2.30,
      "percent_change": -0.71,
      "volume": 789012,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "DIS",
      "name": "The Walt Disney Company",
      "price": 170.90,
      "change": 2.60,
      "percent_change": 1.55,
      "volume": 890123,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "LMT",
      "name": "Lockheed Martin Corporation",
      "price": 390.70,
      "change": 1.80,
      "percent_change": 0.46,
      "volume": 901234,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "UNH",
      "name": "UnitedHealth Group Incorporated",
      "price": 415.20,
      "change": 3.40,
      "percent_change": 0.83,
      "volume": 112233,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "ABBV",
      "name": "AbbVie Inc.",
      "price": 116.80,
      "change": -0.60,
      "percent_change": -0.51,
      "volume": 334455,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "LRCX",
      "name": "Lam Research Corporation",
      "price": 583.10,
      "change": -2.90,
      "percent_change": -0.50,
      "volume": 556677,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "TXN",
      "name": "Texas Instruments Incorporated",
      "price": 185.20,
      "change": 0.80,
      "percent_change": 0.43,
      "volume": 112233,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "SO",
      "name": "The Southern Company",
      "price": 65.70,
      "change": 0.20,
      "percent_change": 0.31,
      "volume": 445566,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "CL",
      "name": "Colgate-Palmolive Company",
      "price": 85.40,
      "change": 0.50,
      "percent_change": 0.59,
      "volume": 667788,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "LOW",
      "name": "Lowe's Companies Inc.",
      "price": 200.10,
      "change": 1.30,
      "percent_change": 0.65,
      "volume": 778899,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "CAT",
      "name": "Caterpillar Inc.",
      "price": 232.80,
      "change": -1.20,
      "percent_change": -0.51,
      "volume": 889900,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "MMM",
      "name": "3M Company",
      "price": 175.60,
      "change": 0.80,
      "percent_change": 0.46,
      "volume": 112233,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "GOOG",
      "name": "Alphabet Inc.",
      "price": 2731.20,
      "change": 12.45,
      "percent_change": 0.46,
      "volume": 1568945,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "BAC",
      "name": "Bank of America Corporation",
      "price": 43.80,
      "change": -0.20,
      "percent_change": -0.45,
      "volume": 223344,
      "timestamp": "2024-06-15"
    },
    {
      "symbol": "GS",
      "name": "The Goldman Sachs Group Inc.",
      "price": 398.70,
      "change": 2.10,
      "percent_change": 0.53,
      "volume": 334455,
      "timestamp": "2024-06-15"
    }
]

  data_dict = {
        'name': 'John Doe',
        'age': 30,
        'interests': json_data
    }
  
  # json_result = json.dumps(json_data)
  
  context = {'data_dict': data_dict}
  print(context, "context")

  return render(request, 'stocks.html',context)


def render_stocks(request):
  

  pass  
  
  # return HttpResponse( "Hi...")
