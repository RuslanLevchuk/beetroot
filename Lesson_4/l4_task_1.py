import random

break_flag = 0                      #Прапорець для виходу з програми, по дефолту \0\, значить програма працює
generate_int_flag = 0               #Прапорець потре генерувати число, щоб згенерувати нове число якщо програємо
tries = 3                           #Кількість спроб
# Головний цикл
while 1:
    # якщо прапорець == 1, то закінчуємо гру
    if break_flag == 1:
        print('Good luck!')
        break

    # прапорець генератора 0, значить число ще не згенероване, генеруємо його і встановлюємо прапорець в 1,
    # щоб наступного разу згенерувати, коли програємо
    if generate_int_flag == 0:
        secret_number = random.randint(1, 10)
        generate_int_flag = 1
        #print(secret_number) #розкоментувати тут, якщо дуже хочеться побачити секретне число на початку гри

    # отримуємо число (або не число) від юзера
    my_value = input(f'Guess the number from 1 to 10 that I guessed. You have {tries} try/tries (type \'q\' to quit): ')

    # якщо введені дані - числа, то переводимо дані в інтежер
    if my_value.isdigit():
        my_value = int(my_value)

        if my_value == secret_number: # перевіряємо чи відповідає секретне число нашому
            my_value = input(f"Yes, the number {secret_number} is true! You win! Wanna again? (y/n): ")
            generate_int_flag = 0
            # ми виграли і одразу встановили прапор генератора у 0
            # щоб знову згенеувати число в подальшому при згоді юзера грати
            # також питаємо в юзера чи граємо далі, чи ні:
            if my_value == 'y' or my_value == 'Y':
                generate_int_flag = 0       #якщо граємо, то прапор генератора 0, щоб знову генерувати число
            elif my_value == 'n' or my_value == 'N':
                break_flag = 1 # якщо ні, то прапор виходу = 1, значить буде брейк з циклу
            #якщо відповіддю буде якась хєрня,
            #то ми задовбемо користувача питаннями, що все ж він хоче зробити
            # для цього використаємо нескінченний цикл із постійними питанням
            # і залежно від відповіді встановлюємо відповідні прапорці на кшталт вище
            else:
                while 1:
                    my_value = input('I will ask you until I don\'t get correct command: '
                                     'Do you want to play again? (y/n): ')
                    print(my_value)
                    if my_value == 'y' or my_value == 'Y':
                        break
                    elif my_value == 'n' or my_value == 'N':
                        break_flag = 1
                        break
        # якщо відповідаємо невірно, то прінтуємо це і відмінумовуємо одну спробу
        else:
            print('Wrong!')
            tries -= 1
            # якщо спроб не залишилось, то пишемо, що юзер програв, і показуємо секретне число
            # ну і питаємо, що робити у нескінченному циклі, поки не отримаємо вірну команду
            if tries == 0:
                print(f'You lose! The secret number was {secret_number}.')
                while 1:
                    my_value = input('What to do? Continue (\'c\') or Quit (\'q\'): ')
                    if my_value == 'q' or my_value == 'Q':
                        break_flag = 1
                        break
                    elif my_value == 'c' or my_value == 'C':
                        generate_int_flag = 0
                        tries = 3
                        break

        # якщо отримане від юзера значення як Q
    elif my_value == 'q' or my_value == 'Q':
        break_flag = 1
    #тут якщо не отримуємо q або число, то матюкаємось, що тре ввести число
    else:
        print('I told you that number, not text! Try again! ')

