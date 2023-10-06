from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.walmart.com/ip/Instant-Pot-Duo-6-Quart-7-in-1-Electric-Pressure-Cooker-Slow-Rice-Steamer-Saut-Yogurt-Maker-Warmer-Sterilizer-Includes-App-With-Over-800-Recipes-Stai/45918917")
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
print(soup.title)
