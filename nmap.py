import nmap

# Создаем объект сканера
scanner = nmap.PortScanner()

# Указываем IP-адрес или диапазон IP-адресов
target = str(input("Введите ip на подобии 111.111.111.111: ")) # Замените на ваш IP-адрес или диапазон

# Определяем сканируемые порты
ports = '22,80,443' # Замените на нужные порты

# Выполняем сканирование
scanner.scan(hosts=target, arguments='-p ' + ports)

# Выводим результаты
print("-" * 60)
print("Nmap Scan Report")
print("-" * 60)

print('Host: {}'.format(scanner.all_hosts()))
print('State: {}'.format(scanner[target]['status']['state']))

# Проверяем, есть ли открытые порты
if scanner[target].has_tcp():
    print('Порты TCP:')
    for port in scanner[target]['tcp'].keys():
        print('Порт {}: {}'.format(port, scanner[target]['tcp'][port]['state']))

if scanner[target].has_udp():
    print('Порты UDP:')
    for port in scanner[target]['udp'].keys():
        print('Порт {}: {}'.format(port, scanner[target]['udp'][port]['state']))

print("-" * 60)

# Выводим более подробную информацию о порте 22 (SSH)
if '22' in scanner[target]['tcp']:
    print("Информация о порте 22 (SSH):")
    print(scanner[target]['tcp'][22])
