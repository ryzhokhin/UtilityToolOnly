from django.http import HttpResponse
import requests

def view_on_web(request):

    userRequest = request

    budget = request.POST['budget']
    banks = []
    currency = request.POST['currency']

    for key, val in userRequest.POST.items():
        if key != 'csrfmiddlewaretoken' and key != 'budget' and key != 'currency':
            banks.append(val)

    userRequestCalc = {
        'budget': budget,
        'banks': banks,
        'currency': currency
    }

    # calculation
    # coin_names_list = ['BTC', 'BUSD', 'BNB', 'ETH', 'USDT']
    coin_names_list = ['BUSD', 'USDT']
    fullResponse = []
    for i in coin_names_list:
        for j in coin_names_list:
            for b_i in banks:
                for b_j in banks:
                    try:
                        response = calculating_the_profit(float(budget), i, j, b_i, b_j, userRequestCalc['currency'])
                        print(b_i, b_j)
                        # print(response)
                        if response['percentage']>0.0:
                            NAME_AND_PERCENT = response['first_p2p_userName']
                            print(NAME_AND_PERCENT)
                            fullResponse.append(response)
                    except:
                        None

                    # response = calculating_the_profit(float(budget), i, j, b_i, b_j, userRequestCalc['currency'])
                    # print(b_i, b_j)
                    # print(response)
                    # fullResponse.append(response)

    return HttpResponse(fullResponse)


class Algorythm:
    def hello(request):
        print('Hello World')








#  << Toool >>



# import time
# start = time.time()

### Taking the SPOT prices


# name = 'BNBUSDT'

# url = 'https://data.binance.com/api/v3/aggTrades'
# param = {
#     'symbol': 'ETHBTC',
#     'limit': 1
# }
# t = requests.get(url, params=param).json()
# print(t)

def get_binance_spot(name): # Возврат цены со спота
    bin_url_test = 'https://data.binance.com/api/v3/aggTrades'
    param = {
        'symbol': name,
        'limit': 1
    }
    r = requests.get(bin_url_test, params=param).json()
    return r[0]['p']


#### Taking the p2p prices

def get_binance_buy(name, bank, fiat):  # string params  #
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    params = {"proMerchantAds": False,
              "page": 1,
              "rows": 10,
              "payTypes": [bank],
              "countries": [],
              "publisherType": None,
              "fiat": fiat,
              "tradeType": "BUY",
              "asset": name,
              "merchantCheck": True,
              "transAmount": ""
              }
    response = requests.post(url=url, headers=headers, json=params).json()

    response_to_return = {
        'price': response['data'][0]['adv']['price'],
        'min': response['data'][0]['adv']['minSingleTransAmount'],
        'max': response['data'][0]['adv']['dynamicMaxSingleTransAmount'],
        'name': response['data'][0]['advertiser']['nickName']
    }
    # response_with_name = 'Name: ' + response['data'][0]['advertiser']['nickName'] + ' Price: ' + \
    #                      response['data'][0]['adv']['price']
    return response_to_return


def get_binance_sell(name, bank, fiat):
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    params = {"proMerchantAds": False,
              "page": 1,
              "rows": 10,
              "payTypes": [bank],
              "countries": [],
              "publisherType": None,
              "fiat": fiat,
              "tradeType": "SELL",
              "asset": name,
              "merchantCheck": True,
              "transAmount": ""
              }
    response = requests.post(url=url, headers=headers, json=params).json()

    # print(response['data'][0]['adv']['tradeMethods'][0]['identifier'])

    response_to_return = {
        'price': response['data'][0]['adv']['price'],
        'min': response['data'][0]['adv']['minSingleTransAmount'],
        'max': response['data'][0]['adv']['dynamicMaxSingleTransAmount'],
        'name': response['data'][0]['advertiser']['nickName']
    }
    # response_with_name = 'Name: ' + response['data'][0]['advertiser']['nickName'] + ' Price: ' + \
    #                      response['data'][0]['adv']['price']
    return response_to_return


# def get_binance_buy_all(name):  # string params
#     url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
#
#     headers = {
#         'accept': '*/*',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
#     }
#
#     params = {
#         "proMerchantAds": False,
#         "page": 1,
#         "rows": 10,
#         "payTypes": [],
#         "countries": [],
#         "publisherType": None,
#         "transAmount": "",
#         "asset": name,
#         "fiat": "USD",
#         "tradeType": "BUY",
#     }
#     response = requests.post(url=url, headers=headers, json=params).json()
#     response_to_return = {
#         'price': response['data'][2]['adv']['price'],
#         'min': response['data'][2]['adv']['minSingleTransAmount'],
#         'max': response['data'][2]['adv']['dynamicMaxSingleTransAmount'],
#         'name': response['data'][2]['advertiser']['nickName']
# 
#     }
#     # response_with_name = 'Name: ' + response['data'][0]['advertiser']['nickName'] + ' Price: ' + \
#     #                      response['data'][0]['adv']['price']
#     return response_to_return

####


# 1. мы берем на p2p покупка покупаем по курсу [валюта]/(к выбранной криптовалюте)
# 2. потом берем покупамем вторую криптовалюту по курсу (вторая крипта)/(первая крипта)
# 3. далее берем вторую купленную крипту и выставляем ордер в продаже на (вторая крипта)/[валюта]
# 4. сравниваем [валюта] в конце к гривне сначала

def calculating_the_profit(uah_budget, name_firstp2p, name_spot, bank_first, bank_second, fiat):
    #  1.
    firstP2P_name = name_firstp2p
    firstP2P_price = get_binance_buy(firstP2P_name, bank_first, fiat)
    tmp_first = firstP2P_price['price']

    firstRound = uah_budget / float(tmp_first)
    #   2.
    spot_name = name_spot
    try:
        spot_price = get_binance_spot(name_spot + name_firstp2p)
        secondRound = firstRound / float(spot_price)
    except:
        try:
            spot_price = get_binance_spot(name_firstp2p + name_spot)
            secondRound = firstRound * float(spot_price)
        except:
            return print('No match: ' + name_firstp2p + ' ' + name_spot)

    #   3.
    secondP2P_name = spot_name
    secondP2P_price = get_binance_sell(secondP2P_name, bank_second, fiat)
    tmp_second = secondP2P_price['price']

    uah_after = float(tmp_second) * secondRound
    delta = uah_after - uah_budget
    percentage = (100.0 * uah_after) / uah_budget - 100

    limit_first = 'min: ' + firstP2P_price['min'] + ' max: ' + firstP2P_price['max']
    limit_second = 'min' + secondP2P_price['min'] + ' max: ' + secondP2P_price['max']
    output_func = {
        'budget': uah_budget,
        'final_budget': uah_after,
        'percentage': percentage,
        'delta': delta,
        'first_name': firstP2P_name,
        'spot_name': spot_name,
        'limit_first': limit_first,
        'limit_second': limit_second,
        'first_p2p_userName': firstP2P_price['name'],
        'second_p2p_userName': secondP2P_price['name'],
        'first_bank': bank_first,
        'second_bank': bank_second
    }
    return output_func




# print(get_binance_buy('USDT'))
# print(calculating_the_profit(100, 'BTC', 'ETH'))
# print(get_binance_sell("DAI"))
#
# resp_test = calculating_the_profit(734.56, 'USDT', 'BTC')
# print(resp_test)
# print('<<<----->>>')
#
#
#     print()
# end = time.time()
# print(end-start)
# print(get_binance_spot('BTCETH'))
# print(calculating_the_profit(400, 'BTC', 'BNB'))
