from bs4 import BeautifulSoup
import requests

url = "https://omgtu.ru/ecab/persons/index.php?b=14"
page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.text, "html.parser")
name_blocks = soup.find_all('div', class_="person__name")
staff = [div.a.get_text(strip=True) for div in name_blocks if div.a]
print(staff)

with open("staff.txt", "w", encoding="utf-8") as file:
    for name in staff:
        file.write(name + "\n")