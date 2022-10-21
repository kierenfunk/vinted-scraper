import requests

class VintedAPI:
    def __init__(self, vinted_session_token):
        self.session = requests.Session()
        self.session.cookies.set_cookie(requests.cookies.create_cookie('_vinted_fr_session', vinted_session_token))
        self.session.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})
        self.session.headers.update({'accept-language': 'en-US,en;q=0.9'})

    def invoices_current(self):
        response = self.session.get('https://www.vinted.pl/api/v2/wallet/invoices/current')
        return response.json()

    def invoice(self, year, month):
        response = self.session.get(f'https://www.vinted.pl/api/v2/wallet/invoices/{year}/{month}')
        return response.json()
