import readchar

def main():
    while True:
        key = readchar.readkey()
        print(f'Tecla presionada: {key}')
        if key == '\x1b[A':
            print('¡Tecla UP presionada! Terminando el programa.')
            break

if __name__ == "__main__":
    main()
