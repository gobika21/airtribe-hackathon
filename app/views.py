from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def render_news_website(request):
  
  json_data = [{
    "symbol": "AAPL",
    "price": 143.25,
    "volume": 1234567,
    "change": -0.75
  },
  {
    "symbol": "GOOGL",
    "price": 2750.50,
    "volume": 987654,
    "change": 10.25
  },
  {
    "symbol": "MSFT",
    "price": 300.75,
    "volume": 2345678,
    "change": 1.20
  },
  {
    "symbol": "AMZN",
    "price": 3300.00,
    "volume": 345678,
    "change": -5.50
  },
  {
    "symbol": "TSLA",
    "price": 700.25,
    "volume": 456789,
    "change": 3.75
  },
  {
    "symbol": "NVDA",
    "price": 750.80,
    "volume": 567890,
    "change": -2.10
  },
  {
    "symbol": "NFLX",
    "price": 550.30,
    "volume": 678901,
    "change": 0.90
  },
  {
    "symbol": "FB",
    "price": 320.45,
    "volume": 789012,
    "change": -1.50
  },
  {
    "symbol": "GOEV",
    "price": 12.65,
    "volume": 890123,
    "change": -0.30
  },
  {
    "symbol": "UBER",
    "price": 43.20,
    "volume": 901234,
    "change": 2.10
  },
  {
    "symbol": "LYFT",
    "price": 52.15,
    "volume": 112233,
    "change": -1.80
  },
  {
    "symbol": "SQ",
    "price": 240.60,
    "volume": 445566,
    "change": 4.50
  },
  {
    "symbol": "PYPL",
    "price": 280.75,
    "volume": 778899,
    "change": 1.75
  },
  {
    "symbol": "INTC",
    "price": 55.90,
    "volume": 665544,
    "change": -0.25
  },
  {
    "symbol": "AMD",
    "price": 95.10,
    "volume": 554433,
    "change": 1.80
  },
  {
    "symbol": "NIO",
    "price": 42.30,
    "volume": 443322,
    "change": -0.90
  },
  {
    "symbol": "BABA",
    "price": 190.50,
    "volume": 332211,
    "change": 2.30
  },
  {
    "symbol": "JD",
    "price": 80.20,
    "volume": 221100,
    "change": -0.60
  },
  {
    "symbol": "PDD",
    "price": 120.75,
    "volume": 110011,
    "change": 3.20
  },
  {
    "symbol": "MRNA",
    "price": 220.35,
    "volume": 200100,
    "change": -2.70
  },
  {
    "symbol": "ZM",
    "price": 300.25,
    "volume": 198765,
    "change": 1.40
  },
  {
    "symbol": "CRM",
    "price": 250.80,
    "volume": 187654,
    "change": -0.80
  },
  {
    "symbol": "SHOP",
    "price": 1400.65,
    "volume": 176543,
    "change": 5.60
  },
  {
    "symbol": "SE",
    "price": 300.00,
    "volume": 165432,
    "change": 0.25
  },
  {
    "symbol": "BAC",
    "price": 45.75,
    "volume": 154321,
    "change": -1.10
  },
  {
    "symbol": "JPM",
    "price": 150.40,
    "volume": 143210,
    "change": 2.00
  }]

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
