import requests

def shorten_url(url):
    endpoint = "https://tinyurl.com/api-create.php"
    params = {"url": url}
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.text.strip()  # Stripping to remove leading/trailing whitespaces
    else:
        return None

# Example usage:
long_url = input("Please enter the link: ")  # corrected input function
short_url = shorten_url(long_url)
print("Shortened URL:", short_url)
