#!python3
clients = ['Raul','Fernando']


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += [client_name]
        print(f'Client {client_name} added to the list')
    else:
        print('Client already in the clients list')


def delete_client(client_name):
    global clients
    if client_name in clients:
        client_index = clients.index(client_name)
        del(clients[client_index])
        print(f'{client_name} deleted from the list')
    else:
        print('Client not in the list')


def list_clients():
    global clients
    print(clients)


def _welcome():
    print('Welcome to this wonderful program!')
    print('*'*50+'\n')
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')
    print('[L]ist clients')
    print('[E]xit')


def _quick_menu():
    print('Please, enter a command:')
    print('[C]reate client | [D]elete client | [L]ist clients | [E]xit')


if __name__ == '__main__':
    _welcome()
    while True:
        command = input()
        if command == 'C':
            client_name = input('Name: ')
            create_client(client_name)
            _quick_menu()
        elif command == 'D':
            client_name = input('Name: ')
            delete_client(client_name)
            _quick_menu()
        elif command == 'L':
            print('This is the list of clients:')
            list_clients()
            _quick_menu()
        elif command == 'E':
            print('Thank you for using this program! Until the next time :)')
            break
        else:
            print('Command not found')