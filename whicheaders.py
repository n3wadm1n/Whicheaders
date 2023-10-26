#!/usr/bin/python3
####################
################ 3.0
### n3wadm1n #####
### Euribot  #####
#####################

import argparse, requests, urllib3, readline, random
from requests.exceptions import RequestException
from colored import fg, attr

readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/94.0.4606.71 Chrome/94.0.4606.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.0; AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15 Edg/97.0.1072.55",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/81.0.4196.73",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
]

rnd_u_ag = random.choice(user_agents)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_headers(url):
    try:
        hders = {'User-Agent': rnd_u_ag}
        response = requests.get(url, headers=hders, timeout=5, verify=False)
        required_headers = [
            "X-XSS-Protection",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "Referrer-Policy",
            "Permissions-Policy",
            "Cross-Origin-Embedder-Policy",
            "Cross-Origin-Resource-Policy",
            "Cross-Origin-Opener-Policy",
            "X-Permitted-Cross-Domain-Policies",
            "Clear-Site-Data",
            "Cache-Control",
            "Feature-Policy",
            "Content-Security-Policy-Report-Only"
        ]
        present_headers = [header for header in required_headers if header in headers]
        missing_headers = [header for header in required_headers if header not in headers]

        output = f"URL: {url}\n"

        if present_headers:
            output += "Present Headers:\n"
            for header in present_headers:
                output += f"{fg(2)}{header}: {headers.get(header)}{attr(0)}\n"
            output += "\n"

        if missing_headers:
            output += "Missing Headers:\n"
            for header in missing_headers:
                output += f"{fg(1)}{header}{attr(0)}\n"
            output += "\n"

        return output

    except RequestException as e:
        output = f"URL: {url}\nConnection error: {e}\n\n"
        return output

def main():
    parser = argparse.ArgumentParser(description='Check headers of URLs')
    parser.add_argument('-f', '--file', help='Path to the file containing URLs')
    parser.add_argument('-o', '--output', help='Output file name for the result (leave blank to not save)')
    parser.add_argument('-u', '--url', help='Single URL to check')

    args = parser.parse_args()

    if args.file or args.url:
        result_all = ""
        
        if args.file:
            with open(args.file, "r") as uurls:
                for line in uurls:
                    url = line.strip()
                    output = check_headers(url)
                    result_all += output

        if args.url:
            output = check_headers(args.url)
            result_all += output

        if args.output:
            with open(args.output, "w") as output:
                output.write(result_all)
            print("Output saved in this file:", args.output)
        else:
            print(result_all)
    
    else:
        print("Please provide either -f or -u option.")

if __name__ == "__main__":
    main()
