from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests

class ScrapHotel:

    def __init__(self, hotel_name):
        #self.html_doc = 'https://www.booking.com/hotel/cl/ibis-budget-providencia.html?'
        self.html_doc = f'https://www.booking.com/hotel/cl/{hotel_name}.html?'

        self.chrome_path = "C:\\chromedriver"
        headers = {"Accept-Language": "es-ES,es;q=0.5"}
        params = dict(lang='es-ES,es;q=0.5')
        self.content = requests.get(self.html_doc, headers=headers, params=params)

    def get_hotel_data(self):
        hotel_data = {}
        hotel_description = {}
        room = self.get_room_info()
        soup = BeautifulSoup(self.content.text, 'html.parser')
        name_hotel = soup.find(id='hp_hotel_name').find_all(text=True, recursive=False)
        address_hotel = soup.find(class_='hp_address_subtitle').find_all(text=True, recursive=False)
        photos_hotel = soup.find(class_='bh-photo-grid').find_all('img')
        photo_hotel = [n['src'] for n in photos_hotel if 'hotel' in n['src']]
        review_score = soup.find(class_='bui-review-score__badge').text
        review_quantities = soup.find(class_='bui-review-score__text').text

        hotel_description['name_hotel'] = str(name_hotel).translate({ord(i): None for i in "[',]"}).replace('\\n', "")
        hotel_description['address_hotel'] = str(address_hotel).translate({ord(i): None for i in "[']"}).replace('\\n',"")
        hotel_description['photo_hotel'] = str(photo_hotel[0:5]).translate({ord(i): None for i in "[',]"})
        hotel_description['review_score'] = review_score
        hotel_description['review_quantities'] = review_quantities

        hotel_data['hotel_description'] = hotel_description
        hotel_data['rooms'] = room

        return hotel_data

    def get_room_info(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es,es_ES'})
        # options.add_argument('--headless')
        driver = webdriver.Chrome(self.chrome_path, chrome_options=options)
        driver.get(self.html_doc)

        room_table = driver.find_element_by_class_name('roomstable')
        links = room_table.find_elements_by_class_name('jqrt')
        room = []
        for link in links:
            room_amenities = {}
            link.click()
            time.sleep(5)

            soup2 = BeautifulSoup(driver.page_source, 'html.parser')
            images = soup2.find(class_='hp_rt_lightbox_wrapper').findAll('img')
            photo_room_temp = [image.get('src') or image.get('data-lazy') for image in images if
                               image.get('src') is not None]
            photo_room = [photo for photo in photo_room_temp if 'square' not in photo]

            equipments_bathroom = driver.find_elements_by_xpath(
                "//ul[@class='hprt-lightbox-list js-lightbox-facilities'][1]")
            equipment_bathroom = [n.text for n in equipments_bathroom]

            room_views = driver.find_elements_by_xpath(
                "//ul[@class='hprt-lightbox-list js-lightbox-facilities'][2]")
            room_view = [n.text for n in room_views]

            equipments_room = driver.find_elements_by_xpath(
                "//ul[@class='hprt-lightbox-list js-lightbox-facilities'][3]")
            equipment_room = [n.text for n in equipments_room]

            room_amenities['room_name'] = link.text
            room_amenities['photo_room'] = str(photo_room).translate({ord(i): None for i in "[',]"})
            room_amenities['bathroom'] = str(equipment_bathroom).translate({ord(i): None for i in "[]','"}).replace('\\n', ',')
            room_amenities['room_view_title'] = str(room_view).translate({ord(i): None for i in "[]','"}).replace('\\n', ',')
            room_amenities['equipment_title'] = str(equipment_room).translate({ord(i): None for i in "[]','"}).replace('\\n', ',')
            room.append(room_amenities)
            time.sleep(1)
            driver.find_element_by_class_name('lightbox_close_button').click()

        driver.quit()
        return room
