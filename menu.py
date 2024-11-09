import curses
import os
import platform

def executar_comando(opcao):
    if opcao == 0:
        comando = "echo 'Executando opção 1'"
    elif opcao == 1:
        comando = "echo 'Executando opção 2'"
    elif opcao == 2:
        comando = "echo 'Executando opção 3'"
    else:
        comando = ""
    
    if platform.system() == "Windows":
        os.system(f'cmd /c {comando}')
    else:
        os.system(comando)

def mostrar_menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    menu = ["Opção 1", "Opção 2", "Opção 3", "Sair"]
    opcao_selecionada = 0

    # Habilita o uso do mouse em curses
    curses.mousemask(1)

    while True:
        stdscr.clear()

        # Exibe as opções de menu como "botões" em ASCII
        for idx, opcao in enumerate(menu):
            x = 5
            y = 3 + idx * 3

            if idx == opcao_selecionada:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, f"[ {opcao} ]")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, f"[ {opcao} ]")

        # Captura a entrada do usuário (teclado ou mouse)
        tecla = stdscr.getch()

        # Controle de navegação do teclado
        if tecla == curses.KEY_UP and opcao_selecionada > 0:
            opcao_selecionada -= 1
        elif tecla == curses.KEY_DOWN and opcao_selecionada < len(menu) - 1:
            opcao_selecionada += 1
        elif tecla == curses.KEY_ENTER or tecla in [10, 13]:  # Enter
            if opcao_selecionada == len(menu) - 1:
                break
            else:
                executar_comando(opcao_selecionada)

        # Controle de navegação pelo mouse
        elif tecla == curses.KEY_MOUSE:
            _, mouse_x, mouse_y, _, mouse_state = curses.getmouse()
            if mouse_state & curses.BUTTON1_PRESSED:
                for idx in range(len(menu)):
                    if 5 <= mouse_x <= 15 and (3 + idx * 3) == mouse_y:
                        opcao_selecionada = idx
                        if opcao_selecionada == len(menu) - 1:
                            return
                        else:
                            executar_comando(opcao_selecionada)
        
        stdscr.refresh()

def main():
    curses.wrapper(lambda stdscr: curses.start_color() or curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) or mostrar_menu(stdscr))

if __name__ == "__main__":
    main()