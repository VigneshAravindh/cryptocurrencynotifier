import requests
import time

ApiKey = 'c42d0066-2d12-4e25-9c10-18504892293a'
BotId = '5794474891:AAEAJ3wFk5knqqpyj01zd2VnWlPyxIUS-zs'
ChatId = ''
TimeLimit = 1 * 30 # in seconds
coin=1
threshold=0

#getting crypto currency data by using API Key
def get_crypto_price(coin):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': ApiKey
    }

    # make a request to the coinmarketcap API
    Data = requests.get(url, headers=headers)
    Data_json = Data.json()

    # extract the bitcoin price from the json data
    CryptoPrice = Data_json['data'][coin]
    return CryptoPrice['quote']['USD']['price']


# function to send_message through telegram
def send_message(chat_id, message):
    url = f"https://api.telegram.org/bot{BotId}/sendMessage?chat_id={ChatId}&text={message}"

    # send the msg
    requests.get(url)

def main():
    PriceData = []
    print("start")
    print("Enter 0 for BTC-bitcoin")
    print("Enter 1 for ETH-Ethereum")
    print("Enter 2 for USDT-Tether")


    while True:
        price = get_crypto_price(coin)
        PriceData.append(price)

        if coin == 0:
            if price < threshold:
                send_message(chat_id=ChatId, message=f'BTC Price Drop Alert: {price}')
                print("sucess")
            else:
                send_message(chat_id=ChatId,
                             message=f'BTC Price Drop Alert: {price} >>target reached above {threshold}')

        elif coin == 1:
            if price < threshold:
                send_message(chat_id=ChatId, message=f'ETH Price Drop Alert: {price}')
                print("sucess")
            else:
                send_message(chat_id=ChatId,
                             message=f'ETH Price Drop Alert: {price} >>target reached above {threshold}')
        elif coin == 2:
            if price < threshold:
                send_message(chat_id=ChatId, message=f'USDT Price Drop Alert: {price}')
                print("sucess")
            else:
                send_message(chat_id=ChatId,
                             message=f'USDT Price Drop Alert: {price} >>target reached above {threshold}')


        if len(PriceData) >= 6:
            send_message(chat_id=ChatId, message=PriceData)
            PriceData = []

        time.sleep(TimeLimit)