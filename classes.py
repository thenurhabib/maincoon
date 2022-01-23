#! /usr/bin/python3
# Author Md. nur habib

# Import Modules
import os
import re
import colors
import shodan
import requests
import webbrowser
import platform


# Main Class
class AllTools:

    #  Whois Information
    def whoisInformation():
        try:
            print("Get Whois Information.")
            url = input("Enter Domain name : ")
            result = requests.get(f"http://api.hackertarget.com/whois/?q={url}").text
            print(result)
        except Exception as error:
            print(f"An error occurred : {error}")


    # Get Torrent Information Via IP
    def torrent():
        try:
            getipaddress = input("Enter IP Address : ")
            r = requests.get(
                f"https://api.antitor.com/history/peer/?ip={getipaddress}&key=3cd6463b477d46b79e9eeec21342e4c7"
            )
            res = r.json()
            print("Please wait, Loading Torrent...")
            if len(res) > 4:
                print(f"IP Address: {res}['ip']:\n")
                print(f"ISP: {res['isp']}\n")
                printf("Country: {res['geoData']['country']}\n")
                print(f"Latitude: {str(res['geoData']['latitude'])}\n")
                print(f"Longitude:{str(res['geoData']['longitude'])}\n")
                for i in res["contents"]:
                    print(f"Category: {i['category']}\n")
                    print(f"Name: {i['name']}")
                    print(f"Start: {i['startDate']}\n")
                    print(f"End: {i['endDate']}")
                    print(f"Size: {str(i['torrent']['size'])}")
            else:
                print("Error: Something Went Wrong")
        except Exception as error:
            print(f"An error occurred : {error}")

    # IP Information From Shodan
    def shodanipInformation():
        try:
            print("IP/Domain Information.")
            ipaddress = input("Enter IP Address : ")
            host = api.host(ipaddress)
            print("Geting IP/Domain Information from shodan.\n")
            print(f"IP Address : {str(host['ip_str'])}")
            print(f"Country : {str(host['country_name'])}")
            print(f"City : {str(host['city'])}")
            print(f"Organization : {str(host['org'])}")
            print(f"ISP : {str(host['isp'])}")
            print(f"Open ports : {str(host['ports'])}")
        except Exception as error:
            print(f"An error occurred : {error}")

    # Reverse Image Search
    def reverseImageSearch():
        try:
            image = print("Enter Your Image Path :")
            surl = "https://www.google.co.in/searchbyimage/upload"
            murl = {"encoded_image": (image, open(image, "rb")), "image_content": ""}
            response = requests.post(surl, files=murl, allow_redirects=False)
            fetchUrl = response.headers["Location"]
            openWeb = input("Open Search Result in web broser? (Y/N) : ")
            if openWeb.upper() == "Y":
                webbrowser.open(fetchUrl)
            else:
                pass
        except Exception as error:
            print(f"An error occurred : {error}")

    # Proxy Server Information
    def profyInformation():
        try:
            ipaddress = input("Enter IP Address : ")
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ipaddress):
                db = profyInformation.profyInformation()
                db.open("./components/output.csv")
                record = db.get_all(ipaddress)
                db.close()
                if record["is_proxy"] != 0:
                    print(f"Proxy Type: {record['proxy_type']}")
                    print(f"Country Code: {record['country_short']}")
                    print(f"Country: {record['country_long']}")
                    print(f"Region Name:  {record['region']}")
                    print(f"City:  {record['city']}")
                    print(f"Isp:  {record['isp']}")
                    print(f"Domain: {record['domain']}")
                    print(f"Usage: {record['usage_type']}")
                    print(f"ASN: {record['asn']}")
                    print(f"Name:  {record['as_name']}")
                    api_key = ipstack()
                    r = requests.get(
                        f"http://api.IPstack.com/{ipaddress} ?access_key= {api_key}"
                    )
                    response = r.json()
                    print("Latitude :{latitude.format(**response)}")
                    print("Longitude :{longitude.format(**response)}")
                else:
                    print("IP does not use any Proxy or VPN")
            else:
                print("Enter a Valid IP Address")
        except Exception as error:
            print(f"An error occurred : {error}")

    # Port Scanning
    def PortScanning():
        try:
            ipaddress = input("Enter IP Address : ")
            result = requests.get(
                "http://api.hackertarget.com/nmap/?q={ipaddress}"
            ).text
            print("\n{result}\n")
        except Exception as error:
            print(f"An error occurred : {error}")

    # Phone Number Information
    def phoneNumberInformation():
        try:
            getPhoneNumber = input("Enter Phone Number with Country Code : ")
            print(" Fetching Phonenumber Details...")
            apikey = "e01791e4d18fbbdfa0c9033bf207decd,2f8c8e865a0b25bbf4da08c4db039b8d"
            ph = "".join([i for i in ph if i.isdigit()])
            for api_key in apikey.split(","):
                url = f"http://apilayer.net/api/validate?access_key={api_key}&number={str(getPhoneNumber)}"
                try:
                    response = requests.get(url)
                    if "error" in response.json().keys():
                        continue
                    elif response.json()["valid"] == False:
                        print("Error: Invalid Mobile Number")
                        return
                    else:
                        get = response.json()
                        print(f"Number: {get['number']}")
                        print(f"Type: {get['line_type']}")
                        print(f"CountryCode: {get['country_code']}")
                        print(f"Country: {get['country_name']}")
                        print(f"Location: {get['location']}")
                        print(f"Carrier: {get['carrier']}")
                        return
                except:
                    continue
            print(str(response.json()["error"]["info"]).split(".")[0])
        except Exception as error:
            print(f"An error occurred : {error}")

    # DNS lookup
    def dnslookup():
        try:
            getDomainName = input("Enter Domain Name : ")
            result = requests.get(
                "http://api.hackertarget.com/dnslookup/?q={getDomainName}"
            ).text
            print("\nresult")
        except Exception as error:
            print(f"An error occurred : {error}")

    # get Mail Information
    def mailInformation():
        try:
            emailaddress = input("Enter Email Address : ")
            if ("@" and ".com") or ("@" and ".in") in emailaddress:
                req = requests.get(
                    f"https://api.hunter.io/v2/domain-search?domain={emailaddress}&api_key=9f189e87e011a1d2f3013ace7b14045dec60f62c"
                )
                j = req.json()
                print("Gething Data from {emailaddress}...")
                for i in range(len(j["data"]["emails"])):
                    print("Email ID   :", j["data"]["emails"][i]["value"])
                    print("First Name :", j["data"]["emails"][i]["first_name"])
                    print("Last Name  :", j["data"]["emails"][i]["last_name"])
                    if j["data"]["emails"][i]["position"] != None:
                        print("Position   :", j["data"]["emails"][i]["position"])
                    if j["data"]["emails"][i]["linkedin"] != None:
                        print("Linkedin   :", j["data"]["emails"][i]["linkedin"])
                    if j["data"]["emails"][i]["twitter"] != None:
                        print("Twitter    :", j["data"]["emails"][i]["twitter"])
                    print()
            else:
                print("Error: Invalid Email Address")
        except Exception as error:
            print(f"An error occurred : {error}")

    # Get Information About Mac Address
    def MacAddressLookup():
        try:
            getMacAddress = input("Enter MAC Address : ")
            url = f"https://macvendors.co/api/{getMacAddress}"
            response = requests.get(url)
            result = response.json()
            if result["result"]:
                final = result["result"]
                print(f"Company: {final['company']}")
                print(f"Address: {final['address']}")
                print(f"Country: {final['country']}")
            else:
                print("Error: Something Went Wrong")
        except Exception as error:
            print(f"An error occurred : {error}")

    # DNS Dump
    def dnsDump():
        try:
            getDomainName = input("Enter Domain Name : ")
            image = requests.get(
                "https://dnsdumpster.com/static/map/%s.png" % getDomainName
            )
            if image.status_code == 200:
                image_name = domain.replace(".com", "")
                with open("%s.png" % image_name, "wb") as f:
                    f.write(image.content)
                    print(
                        "\n%s.png DNS Map image stored to current reconspider directory"
                        % image_name
                    )
                    if platform.system() != "Windows":
                        pass
                    else:
                        os.startfile("%s.png" % image_name)
            else:
                print("Sorry, I Can't Find the DNSmap")

        except Exception as error:
            print(f"An error occurred : {error}")

    # Censys Information Gathering from IP Address
    def censysipinformation():
        try:
            print("Censys Information Gathering from IP Address")
            getipAddesss = input("Enter IP Address : ")
            dirty_response = get("https://censys.io/ipv4/%s/raw" % IP).text
            clean_response = dirty_response.replace("&#34;", '"')
            x = clean_response.split('<code class="json">')[1].split("</code>")[0]
            censys = json.loads(x)

            print("Gathering Location Information from [censys]\n")
            print(f"Country : {str(censys['location']['country'])}")
            print(f"Continent : {str(censys['location']['continent'])}")
            print(f"Country Code  {str(censys['location']['country_code'])}")
            print(f"Latitude : {str(censys['location']['latitude'])}")
            print(f"Longitude : {str(censys['location']['longitude'])}")
        except Exception as error:
            print(f"An error occurred : {error}")
