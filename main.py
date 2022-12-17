import requests
import bs4

page_num = 0

while True:
    try:
        url = f'https://eg.hatla2ee.com/ar/new-car/page/{page_num}'
        result = requests.get(url)
        pages = result.content

        soup = bs4.BeautifulSoup(pages, "html.parser")

        car_name = []
        car_price = []
        payment_plan = []

        car_names = soup.findAll("a", {"class": "nCarListData_title"})
        car_prices = soup.findAll("div", {"class": "nCarListData_prices"})
        payment_plans = soup.findAll("div", {"class", "nCarListData_deposit"})

        for n in range(len(car_names)):
            car_name.append(car_names[n].text.replace("\n", ""))
            car_price.append(car_prices[n].text.replace("\n", " "))
            payment_plan.append(payment_plans[n].text.replace("\n", " "))


        full_list = [car_name,car_price,payment_plan]
        for all in zip(*full_list):
         print(all)
        page_num += 1
        if (page_num > 15):
         print("\npages ended, terminate")
         break
        print("\npage switched\n")

    except :

         print("error occurred")
         break