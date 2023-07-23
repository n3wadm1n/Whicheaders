#!/usr/bin/python3
####################
################
### n3wadm1n #####
### Euribot  #####
#####################

import requests, urllib3, readline
from requests.exceptions import RequestException
from colored import fg, attr

readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_headers(url):
    try:
        response = requests.get(url, timeout=5, verify=False)
        headers = response.headers
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
            "Cross-Origin-Opener-Policy"
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
    file_path = input("Enter the path of the file containing URLs: ")
    result_file = input("Enter the output file name for the result (leave blank to not save): ")

    result_all = ""

    with open(file_path, "r") as uurls:
        for line in uurls:
            url = line.strip()
            output = check_headers(url)
            result_all += output

    if result_file:
        with open(result_file, "w") as output:
            output.write(result_all)
        print("Output saved in this file:", result_file)
    else:
        print(result_all)

if __name__ == "__main__":
    main()
