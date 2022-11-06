import requests, os

class tools:
    def checkURLStable(url):
        print("[*] Checking URL stability...")
        try:
            r = requests.get(url)
            print("[*] URL is stable.")
            return True
        except:
            print("[*] URL is not stable.")
            return False

    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

def searchPlate(plate):
    url = f"https://api.g.service.nsw.gov.au/v1/rms/gateway-proxy/anon/getVehicleList/{plate}"

    if tools.checkURLStable(url) == True:
        headers = {
            "Cookie": "rms=eyJ0b2tlbnMiOiIiLCJzZXNzaW9uSWQiOiI5MTE5NTMxZC00MTQzLTRmOTktYTA0Mi01MDZlNTFkYzM1NTQifQ==; SL_G_WPT_TO=en; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; AS=rrt-5996075356883641261-c-gsy1-4347-34939607-2; rms=eyJ0b2tlbnMiOiIiLCJzZXNzaW9uSWQiOiI5MTE5NTMxZC00MTQzLTRmOTktYTA0Mi01MDZlNTFkYzM1NTQifQ==",
            "Host": "api.g.service.nsw.gov.au",
            "Origin": "https://free-rego-check.service.nsw.gov.au",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "x-token": "VE4tMzI0MTY0OTI=",
        }

        r = requests.get(url, headers=headers)

        if "Please check the plate number and try again." in r.text:
            print("[*] Plate not found.")
        else:
            if r.json() == []:
                print("[*] Plate not found.")
            else:
                data = r.json()
                print(f"\nPlate: {data['ResponseDetails']['VehicleDetails'][0]['Plate']['PlateNumber']}")
                print(f"Manufacturer: {data['ResponseDetails']['VehicleDetails'][0]['Manufacturer']['Description']}")
                print(f"Model: {data['ResponseDetails']['VehicleDetails'][0]['Model']['Description']}")
                print(f"Body Shape: {data['ResponseDetails']['VehicleDetails'][0]['BodyShape']['Description']}")
                print(f"Vehicle Colour: {data['ResponseDetails']['VehicleDetails'][0]['VehicleColour']['Description']}")
                print(f"Vehicle Type: {data['ResponseDetails']['VehicleDetails'][0]['VehicleType']['Description']}")
                print(f"Manufacture Year: {data['ResponseDetails']['VehicleDetails'][0]['ManufactureYear']}")
                print(f"Last 4 Digit Vehicle Number: {data['ResponseDetails']['VehicleDetails'][0]['Last4DigitVehicleNumber']}")
                print(f"Tare Weight: {data['ResponseDetails']['VehicleDetails'][0]['TareWeight']}")
                print(f"Registration End Date: {data['ResponseDetails']['RegistrationEndDate']}")
                print(f"Registration Status: {data['ResponseDetails']['RegistrationStatus']}")
                print(f"Policy End Date: {data['ResponseDetails']['PolicyDetails']['EndDate']}")
                print(f"Insurer Code: {data['ResponseDetails']['PolicyDetails']['InsurerCode']}")
                print(f"Insurer Name: {data['ResponseDetails']['PolicyDetails']['InsurerName']}")
                print(f"Concession On Rego: {data['ResponseDetails']['ConcessionOnRego']}")
                print(f"Conditions: {data['ResponseDetails']['Conditions']}")
