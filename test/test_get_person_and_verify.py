"""
Автоматизовані тести для перевірки відповіді сервера на запити GET /verify та GET /person
Сервісу перевірки даних фізичної особи у Державному демографічному реєстрі України
"""
import pytest
import requests

from Query import QUERY_POSITIVE, QUERY_NEGATIVE, QUERY_NEGATIVE_404

server = 'http://10.0.0.10:8080'  # Адреса сервера
header = {'Content-Type': 'application/json',
          }

TEST_DATA = False  # Якщо True, то буде перевірка даних на рівність
IS_PRINT = False # Якщо True, то буде вивід інформації про кожний тест на консоль

@pytest.mark.parametrize('endpoint', ['verify','person'])  # Параметризація тестів
@pytest.mark.parametrize('status_code', [200])  # Параметризація тестів (код статусу)
@pytest.mark.parametrize('result_code', [0])  # Параметризація тестів (код результату)
@pytest.mark.parametrize('result_data', [])    # Параметризація тестів (результат)
@pytest.mark.parametrize('query', QUERY_POSITIVE)  # Параметризація тестів (запит)
def test_verefy_positive(endpoint: str, query: dict, status_code: int, result_code: int, result_data: dict):
    """Тест на позитивні дані
    :param endpoint: str: Назва ендпоінту
    :param query: dict: Запит
    :param status_code: int: Код статусу
    :param result_code: int: Код результату
    :param result_data: dict: Результат
    """
    verify(endpoint, query, status_code, result_code, result_data)


@pytest.mark.parametrize('endpoint', ['verify','person']) # Параметризація тестів
@pytest.mark.parametrize('status_code', [200])  # Параметризація тестів (код статусу)
@pytest.mark.parametrize('result_code', [2])  # Параметризація тестів (код результату)
@pytest.mark.parametrize('result_data', [])  # Параметризація тестів (результат)
@pytest.mark.parametrize('query', QUERY_NEGATIVE)  # Параметризація тестів (запит)
def test_verefy_negative(endpoint: str, query: dict, status_code: int, result_code: int, result_data: dict):
    """Тест на негативні дані
    :param endpoint: str: Назва ендпоінту
    :param query: dict: Запит
    :param status_code: int: Код статусу
    :param result_code: int: Код результату
    :param result_data: dict: Результат
    """
    verify(endpoint, query, status_code, result_code, result_data)


@pytest.mark.parametrize('endpoint', ['verify','person'])  # Параметризація тестів
@pytest.mark.parametrize('status_code', [200])  # Параметризація тестів (код статусу)
@pytest.mark.parametrize('result_code', [2])   # Параметризація тестів (код результату)
@pytest.mark.parametrize('result_data', [])  # Параметризація тестів (результат)
@pytest.mark.parametrize('query', QUERY_NEGATIVE_404)  # Параметризація тестів (запит)
def test_verefy_negative_404(endpoint: str, query: dict, status_code: int, result_code: int, result_data: dict):
    """Тест на негативні дані з кодом 404
    :param endpoint: str: Назва ендпоінту
    :param query: dict: Запит
    :param status_code: int: Код статусу
    :param result_code: int: Код результату
    :param result_data: dict: Результат
    """
    verify(endpoint, query, status_code, result_code, result_data)


# Функція для перевірки відповіді сервера на запити
def verify(endpoint: str, query: dict, status_code: int, result_code: int, result_data: dict):
    """Функція для перевірки відповіді сервера на запити
    :param endpoint: str: Назва ендпоінту
    :param query: dict: Запит
    :param status_code: int: Код статусу
    :param result_code: int: Код результату
    :param result_data: dict: Результат
    """
    person = requests.get(f'{server}/{endpoint}', params=query, headers=header)

    if IS_PRINT:
        # Вивід інформації про кожний тест на консоль (якщо включено)
        print('')
        print(person.url)
        print(f'Запит: {query}')
        print(f'Відповідь: {person.text}')

    assert person.status_code == status_code
    response = person.json()
    assert isinstance(response, dict)
    assert response.get('result_code') == result_code

    if person.status_code == 404:
        if result_code == 2:
            assert response.get('result_data') is not None
            response_result_data = response.get('result_data')
            assert isinstance(response_result_data, dict)
            if TEST_DATA:
                # Перевірка даних на рівність (якщо включено)
                assert response_result_data == result_data
        else:
            assert response.get('result_data') is None


# Запуск тестів при запуску скрипту
if __name__ == '__main__':
    import sys
    pytest.main(['-v', sys.argv[0]])
