import requests
import json
import pandas as pd
from time import sleep

def check_domain(domain):
    url = 'https://sitereview.zscaler.com/api/lookup'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://sitereview.zscaler.com',
        'Referer': 'https://sitereview.zscaler.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    
    payload = {"urls": [domain]}
    
    try:
        response = requests.post(url, headers=headers, json=payload , verify=False)
        response.raise_for_status()
        data = response.json()
        
        # Extract categories
        result = data.get(domain, {})
        zurldb = ', '.join(result.get('zurldblist', []))
        thirdparty = ', '.join(result.get('thirdPartyList', []))
        
        return f"ZURLDB: {zurldb} | ThirdParty: {thirdparty}"
        
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Read domains from file
    with open('C:/Users/basil/Downloads/domains.txt', 'r') as f:
        domains = [line.strip() for line in f.readlines() if line.strip()]
    
    results = []
    
    for domain in domains:
        print(f"Checking: {domain}")
        result = check_domain(domain)
        results.append({'Domain': domain, 'Result': result})
        sleep(1)  # Add delay to avoid rate limiting
    
    # Save to Excel
    df = pd.DataFrame(results)
    df.to_excel('zscaler_results.xlsx', index=False)
    print("Results saved to zscaler_results.xlsx")

if __name__ == "__main__":
    main()