from faker import Faker
import requests

class TestNewLocation:
    def __init__(self):
        self.url = "https://rahulshettyacademy.com/" # Базовая ссылка
        self.key = "?key=qaclick123" # Параметр для всех запросов
        self.fake = Faker("en_US")
        self.locations_count = 0

    def file_writer(self, place_id):
        file = open("place_id.txt", "a")
        file.write(place_id + "\n")
        file.close()

    def file_reader(self, i):
        file = open("place_id.txt", "r")
        place_id = file.readlines()
        file.close()
        return place_id[i].replace("\n", "")

    def file_cleaner(self):
        file = open("place_id.txt", "w")
        file.write("")
        file.close()

    def post_request_new_location(self, count):
        for i in range(count):
            post_resource = "/maps/api/place/add/json"
            post_url = f"{self.url}{post_resource}{self.key}"
            print(post_url)
            json_for_create_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
                "name": f"{self.fake.country()}",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                    "shoe park",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }

            result = requests.post(post_url, json = json_for_create_new_location)
            print(result.text)
            status_code = result.status_code

            assert status_code == 200, f"Некорректный статус код {status_code}"
            print("Статус код корректен")

            check_info = result.json()
            status = check_info.get('status')
            assert status == 'OK', f"Некорректеный статус {status}"
            print("Статус корректен")

            place_id = check_info.get('place_id')
            self.file_writer(place_id)
            self.locations_count += 1
            print(f"Place ID: {place_id}")
            print(f"Создано {self.locations_count} локаций")

    def get_created_location(self):
        for i in range(self.locations_count):
            place_id = self.file_reader(i)
            get_resource = "/maps/api/place/get/json"
            get_url = f"{self.url}{get_resource}{self.key}&place_id={place_id}"
            result = requests.get(get_url)
            print(result.text)

            assert result.status_code == 200, f"Некорректный статус код {result.status_code}"
            print("Статус код корректен")
            print(f"Количество проверенных локаций {i+1}")
        print("Все локации проверены")



location = TestNewLocation()
location.post_request_new_location(5)
location.get_created_location()
location.file_cleaner()