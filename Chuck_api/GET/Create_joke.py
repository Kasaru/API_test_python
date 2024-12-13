import requests


class TestCreateJoke:

    url = 'https://api.chucknorris.io/jokes/random'

    def create_categories_list(self):
        url = 'https://api.chucknorris.io/jokes/'
        result = requests.get(url + 'categories')
        categories = result.json()
        return categories

    def test_create_joke_category_positive(self, category, expected_status_code):
        path_joke_category = f"?category={category}"
        url_joke_category = self.url + path_joke_category
        print(url_joke_category)

        result = requests.get(url_joke_category)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == expected_status_code, 'ОШИБКА, Статус-код не совпадают'
        print('Статус-код корректен')

        check_joke = result.json()
        joke_value = check_joke.get("value")
        print(joke_value)

        joke_category = check_joke.get("categories")
        print(joke_category)
        assert joke_category[0] == category, 'ОШИБКА, Статус-код не совпадает'
        print('Категория корректна')

        assert_word = 'Chuck'
        assert assert_word in joke_value, 'ОШИБКА, Проверочное слово отсутствует'
        print('Проверочное слово присутствует')
        print("Тест прошел успешно")



start = TestCreateJoke()
category_list = start.create_categories_list()
for category in category_list:
    start.test_create_joke_category_positive(category, 200)
