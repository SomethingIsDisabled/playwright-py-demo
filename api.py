import requests

base_url = 'http://127.0.0.1:50213/'

# api字典
api_endpoits = {
  'start_browser': f'{base_url}/api/v2/browser/start'
}

def start_browser(account_id='', headless=False):
    param = {
        'account_id': account_id,
    }
    if headless:
        param['headless'] = headless
    response = requests.get(api_endpoits['start_browser'], param)
    print(response)
    print(response.json())
    return response

if __name__ == '__main__':
  start_browser('ea256bfc7df14c10977680f66cfca5c9')