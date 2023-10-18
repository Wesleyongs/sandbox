import requests

url = "https://raw.githubusercontent.com/bumbeishvili/sample-data/main/org.csv"
response = requests.get(url, allow_redirects=True)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content to a local file
    with open("org.csv", "wb") as f:
        f.write(response.content)
    print("Dataset downloaded successfully as 'org.csv'")
else:
    print("Failed to download the dataset. Status code:", response.status_code)
