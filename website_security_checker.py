import requests

url = input("Enter website URL: ")

try:
    response = requests.get(url, timeout=5)

    headers = response.headers

    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    print("\nSecurity Header Report")
    print("----------------------")

    for header in security_headers:
        if header in headers:
            print(f"[+] {header}: Present")
        else:
            print(f"[-] {header}: Missing")

except Exception as error:
    print("Error:", error)
