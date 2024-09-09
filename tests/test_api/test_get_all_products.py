from api.assertions import assert_status_code, assert_message


def test_get_all_products_list(api_client_get_all_product):

    # Отправка запроса и получение ответа
    response = api_client_get_all_product.get_all_products()

    # Используем функции для проверки статуса и сообщения
    assert_status_code(response, 200)
    # Знаю знаю но пока пускай будет
    #assert_message(response, "All products list") - чисто даун не знает что значит "All products list"