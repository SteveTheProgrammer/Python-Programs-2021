import math
from colorama import Fore
from colorama import Style

def display_menu():
    print()
    print()
    print(f'{Fore.MAGENTA}⚫ 𝐒𝐡𝐚𝐩𝐞𝐬 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐨𝐫 𝟐𝟎𝟐𝟏 🔶{Style.RESET_ALL}')
    print()
    print(f'{Fore.RED}𝗬𝗼𝘂𝗿 𝗢𝗽𝘁𝗶𝗼𝗻𝘀: {Style.RESET_ALL}')
    print(f'{Fore.CYAN}𝑶𝒑𝒕𝒊𝒐𝒏 1 ➜ 𝐂𝐢𝐫𝐜𝐥𝐞 ⚫{Style.RESET_ALL}')
    print(f'{Fore.CYAN}𝑶𝒑𝒕𝒊𝒐𝒏 2 ➜ 𝐅𝐨𝐮𝐫 𝐒𝐢𝐝𝐞𝐝 ⬛{Style.RESET_ALL}')
    print(f'{Fore.CYAN}𝑶𝒑𝒕𝒊𝒐𝒏 3 ➜ 𝐓𝐫𝐢𝐚𝐧𝐠𝐥𝐞 🔺{Style.RESET_ALL}')
    print(f'{Fore.CYAN}𝑶𝒑𝒕𝒊𝒐𝒏 0 ➜ 𝑬𝒙𝒊𝒕 🚪 {Style.RESET_ALL}')

def display_submenu():
    print()
    print(f'{Fore.RED}𝗬𝗼𝘂𝗿 𝗢𝗽𝘁𝗶𝗼𝗻𝘀: {Style.RESET_ALL}')
    print(f'{Fore.CYAN}𝑶𝒑𝒕𝒊𝒐𝒏 1 ➜ 𝐑𝐞𝐜𝐭𝐚𝐧𝐠𝐥𝐞 █{Style.RESET_ALL}')
    print(f'{Fore.CYAN}𝑶𝒑𝒕𝒊𝒐𝒏 2 ➜ 𝐓𝐫𝐚𝐩𝐞𝐳𝐢𝐮𝐦 ⏢{Style.RESET_ALL}')
    print(f'{Fore.CYAN}𝑶𝒑𝒕𝒊𝒐𝒏 0 ➜ 𝐁𝐚𝐜𝐤 𝐭𝐨 𝐦𝐞𝐧𝐮 🢀{Style.RESET_ALL}')
    
def input_value():
    value = input(f'{Fore.GREEN}𝑃𝑙𝑒𝑎𝑠𝑒 𝑔𝑖𝑣𝑒 𝑎 𝑣𝑎𝑙𝑢𝑒: {Style.RESET_ALL}')
    while value.isdigit() == False or int(value) < 0:
        value = input(f'{Fore.RED}𝑇ℎ𝑖𝑠 𝑖𝑠 𝑎𝑛 𝑖𝑛𝑣𝑎𝑙𝑖𝑑 𝑣𝑎𝑙𝑢𝑒! 𝑃𝑙𝑒𝑎𝑠𝑒 𝑔𝑖𝑣𝑒 𝑎 𝑣𝑎𝑙𝑖𝑑 𝑜𝑛𝑒: {Style.RESET_ALL}') 
    return int(value)

def input_choice(focus_menu):
    if focus_menu:
        num_choices = 3
    else:
        num_choices = 2
    value = input(f'{Fore.GREEN}𝑃𝑙𝑒𝑎𝑠𝑒 𝑔𝑖𝑣𝑒 𝑎 𝑐ℎ𝑜𝑖𝑐𝑒 (0 - ' + str(num_choices) + f'): {Style.RESET_ALL}')
    while value.isdigit() == False or int(value) < 0 or int(value) > num_choices:
        value = input(f'{Fore.RED}𝑇ℎ𝑖𝑠 𝑖𝑠 𝑎𝑛 𝑖𝑛𝑣𝑎𝑙𝑖𝑑 𝑐ℎ𝑜𝑖𝑐𝑒! 𝑃𝑙𝑒𝑎𝑠𝑒 𝑔𝑖𝑣𝑒 𝑎 𝑣𝑎𝑙𝑖𝑑 𝑐ℎ𝑜𝑖𝑐𝑒 (0 - ' + str(num_choices) + f'): {Style.RESET_ALL}') 
    return int(value)

class Shape:
    def __init__(self):
        print(f'{Fore.CYAN}𝑺𝒉𝒂𝒑𝒆 𝑪𝒓𝒆𝒂𝒕𝒆𝒅!{Style.RESET_ALL}')
    def __str__(self):
        pass
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius = 1):
        Shape.__init__(self)
        print(f'{Fore.CYAN}𝑪𝒊𝒓𝒄𝒍𝒆 𝑪𝒓𝒆𝒂𝒕𝒆𝒅{Style.RESET_ALL}')
        self.pi = math.pi
        self.radius = radius
    def __str__(self):
        return '{}Radius = {}\nArea = {}\nCircumference = {}{}'.format(Fore.CYAN, self.get_radius(), self.calc_area(), self.calc_circumference(), Style.RESET_ALL)
    def get_radius(self):
        return self.radius
    def calc_area(self):
        return self.pi * self.radius ** 2
    def calc_circumference(self):
        return 2 * self.pi * self.radius

class Four_Sided(Shape):
    def __init__(self):
        print(f'{Fore.CYAN}𝑭𝒐𝒖𝒓 𝑺𝒊𝒅𝒆𝒅 𝑺𝒉𝒂𝒑𝒆 𝑪𝒓𝒆𝒂𝒕𝒆𝒅!{Style.RESET_ALL}')
    def __str__(self):
        pass
    def calc_area(self):
        pass
    def calc_perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c, height):
        print(f'{Fore.CYAN}𝑻𝒓𝒊𝒂𝒏𝒈𝒍𝒆 𝑪𝒓𝒆𝒂𝒕𝒆𝒅!{Style.RESET_ALL}')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.height = height
    def __str__(self):
        return '{}Side A = {}\nSide B = {}\nSide C = {}\nHeight = {}\nPerimeter = {}\nArea = {}{}'.format(Fore.CYAN, self.side_a, self.side_b, self.side_c, self.height, self.calc_perimeter(), self.calc_area(), Style.RESET_ALL)
    def get_side_a(self):
        return self.side_a
    def get_side_b(self):
        return self.side_b
    def get_side_c(self):
        return self.side_c
    def get_height(self):
        return self.height
    def calc_perimeter(self):
        return self.side_a + self.side_b + self.side_c
    def calc_area(self):
        return (self.side_a * self.height)/2

class Trapezium(Four_Sided):
    def __init__(self, small_base, big_base, height):
        self.small_base = small_base
        self.big_base = big_base
        self.height = height
    def __str__(self):
        return '{}Small Base = {}\nBig Base = {}\nHeight = {}\nArea = {}{}'.format(Fore.CYAN, self.small_base, self.big_base, self.height, self.calc_area(), Style.RESET_ALL)
    def get_small_base(self):
        return self.small_base
    def get_big_base(self):
        return self.big_base
    def get_height(self):
        return self.height
    def calc_area(self):
        return (self.big_base + self.small_base)*self.height/2

class Rectangle(Four_Sided):
    def __init__(self, side_a, side_b, height):
        self.side_a = side_a
        self.side_b = side_b
        self.height = height
    def __str__(self):
        return '{}Side A = {}\nSide B = {}\nHeight = {}\nArea = {}\nPerimeter = {}{}'.format(Fore.CYAN, self.side_a, self.side_b, self.height, self.calc_area(), self.calc_perimeter(), Style.RESET_ALL)
    def get_side_a(self):
        return self.side_a
    def get_side_b(self):
        return self.side_b
    def get_height(self):
        return self.height
    def calc_area(self):
        return self.side_a * self.height
    def calc_perimeter(self):
        return self.side_a * 2 + self.side_b * 2


#___________________________________MAIN_______________________________________



while True:
    display_menu()
    choice_menu = input_choice(True)
    if choice_menu == 1:
        print(Circle(input_value()))
    elif choice_menu == 2:
        display_submenu()
        choice_submenu = input_choice(False)
        if choice_submenu == 1:
            print(Rectangle(input_value(), input_value(), input_value()))
        elif choice_submenu == 2:
            print(Trapezium(input_value(), input_value(), input_value()))
    elif choice_menu == 3:
        print(Triangle(input_value(), input_value(), input_value(), input_value()))
    elif choice_menu == 0:
        break
print(f'{Fore.CYAN}Thanks for playing!{Style.RESET_ALL}')
