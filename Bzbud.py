import requests

headers = {
    'authority': 'www.boozebud.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': 'application/json',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.boozebud.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.boozebud.com/browse-products?filtercontext=ttype&ttype=tspirits',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'JSESSIONID=node01vnnk0hoixjnh1u5yqdndwevul155548.node0; STABLE_SESSION_ID=node01vnnk0hoixjnh1u5yqdndwevul155548|6e4847ca8bf31c9ecb80d99e080d3eda5694e2ced31698a5cf978fc42cdceac1; ab.storage.sessionId.31e1b32a-6429-4646-99ed-866675041cf0=%7B%22g%22%3A%220c612ac3-6416-48b9-4395-d0577fbeecb0%22%2C%22e%22%3A1641459209522%2C%22c%22%3A1641457409522%2C%22l%22%3A1641457409522%7D; ph_d5K-HmyjqsKWeaSYsWjbzyX4JOEXIeiLNu3k_GbNNS8_posthog=%7B%22distinct_id%22%3A%2217d4b5edb1017-0d1b6bfb48ab46-978183a-1fa400-17d4b5edb11e77%22%2C%22%24device_id%22%3A%2217d4b5edb1017-0d1b6bfb48ab46-978183a-1fa400-17d4b5edb11e77%22%2C%22%24search_engine%22%3A%22google%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%22www.google.com%22%2C%22%24session_recording_enabled%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%7D',
}

data = {
  '{"contentType":"product","searchContext":{"filtercontext":["ttype"],"ttype":["tspirits"],"page":["1"],"pagesize":["50"]},"passContext":false,"urlPath":"/browse-products","urlQuery":"?filtercontext': 'ttype',
  'ttype': 'tspirits"}'
}

response = requests.post('https://www.boozebud.com/a/v3/queryContentList', headers=headers, data=data)