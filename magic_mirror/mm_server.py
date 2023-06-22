from flask import Flask, Response
import json
import re
import bs4
from urllib.request import urlopen
from config import Config
import requests


app = Flask(__name__)


def get_stock_price_details(stock_symbol):
    url = 'https://in.finance.yahoo.com/quote/{}?p={}'.format(stock_symbol, stock_symbol)
    page = urlopen(url)
    soup = bs4.BeautifulSoup(page, 'html.parser')
    price = soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    if soup.find('span', {'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}):
        change, change_percent = soup.find('span', {'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'}).text.split()
        color = 'red'
    else:
        change, change_percent = soup.find('span', {'class': 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}).text.split()
        color = 'green'
    return {'price': price, 'change': change, 'percentage_change': change_percent, 'color': color}


@app.route('/getStockPrice')
def get_stock_price():
    body = list()
    for stock_symbol in Config.INCLUDED_STOCKS:
        details = get_stock_price_details(stock_symbol.get('symbol'))
        details.update({'stock': stock_symbol.get('name')})
        body.append(details)
    response = Response(
        json.dumps(body), status=200, content_type='application/json')
    return response


def get_latest_nav(url):
    response = requests.get(url).json()
    return float(response.get('data')[0].get('nav'))


@app.route('/getPortfolioDetails')
def get_portfolio_details():
    response = list()
    for portfolio_data in Config.PORTFOLIO_DETAILS:
        mf_current_nav = get_latest_nav(portfolio_data.get('api'))
        current_price = mf_current_nav * portfolio_data.get('units_owned')
        portfolio_data.update({'current_price': round(current_price, 2), 'returns': round(current_price - portfolio_data.get('amount_invested'), 2)})
        if portfolio_data.get('returns') < 0:
            portfolio_data.update({'color': 'red'})
        else:
            portfolio_data.update({'color': 'green'})
        response.append(portfolio_data)
    return Response(json.dumps(response), status=200, content_type='application/json')


if __name__ == "__main__":
    app.run(debug=True)

