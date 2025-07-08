# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# выйти из программы.


from selenium import webdriver
from selenium.webdriver import Keys  # Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By  # Библиотека с поиском элементов на сайте
import random
import time

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org")

zapr = input("Введите ваш запрос для поиска на Википедии: ")

search_box = browser.find_element(By.NAME, "search")
search_box.send_keys(zapr)
search_box.send_keys(Keys.RETURN)

time.sleep(2)

try:
    first_link = browser.find_element(By.CSS_SELECTOR, ".mw-search-result-heading a")
    first_link.click()
    time.sleep(2)  # Ждем загрузки статьи
except:
    print("Статья не найдена. Показываю текущую страницу.")

while True:
    print("\nВыберите действие: ")
    print("1 - листать параграфы текущей статьи")
    print("2 - перейти на одну из связанных страниц")
    print("3 - выйти из программы")
    n = int(input("Введите число для поиска: "))

    if n == 1:
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            if paragraph.text.strip():
                print(paragraph.text)

                user_input = input("Нажмите Enter для следующего параграфа или 'q' для выхода в меню: ")
                if user_input.lower() == "q":
                    break
        input("Нажмите Enter для возврата в меню.")



    elif n == 2:

        links = browser.find_elements(By.CSS_SELECTOR, "#bodyContent a")
        for i, link in enumerate(links[:10], start=1):  # Показываем только первые 10 ссылок для удобства
            print(f"{i}. {link.text} -> {link.get_attribute('href')}")
        choice = int(input("Введите номер ссылки для перехода: "))

        if 1 <= choice <= len(links[:10]):
            links[choice - 1].click()

            time.sleep(2)

    elif n == 3:
        break

    else:

        print("Неверный ввод. Попробуйте снова.")
browser.quit()