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
    elif opcao == 3:
        comando = "echo 'Saindo...'"

    if platform.system() == "Windows":
        os.system(f'cmd /c {comando}')
    else:
        os.system(comando)

def desenhar_botao(stdscr, y, x, texto, selecionado):
    largura = 20
    altura = 5

    if selecionado:
        stdscr.attron(curses.color_pair(1))

    # Desenha borda do botão
    for i in range(altura):
        stdscr.addstr(y + i, x, " " * largura)

    # Adiciona texto centralizado
    stdscr.addstr(y + altura // 2, x + (largura - len(texto)) // 2, texto)

    if selecionado:
        stdscr.attroff(curses.color_pair(1))

def mostrar_menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    menu = ["Opção 1", "Opção 2", "Opção 3", "Sair"]
    opcao_selecionada = 0
    num_colunas = 2

    # Habilita o uso do mouse em curses
    curses.mousemask(1)

    while True:
        stdscr.clear()

        # Desenha botões em uma grade 2x2
        for idx, opcao in enumerate(menu):
            y = 3 + (idx // num_colunas) * 6
            x = 5 + (idx % num_colunas) * 25
            desenhar_botao(stdscr, y, x, opcao, idx == opcao_selecionada)

        # Captura a entrada do usuário (teclado ou mouse)
        tecla = stdscr.getch()

        # Controle de navegação do teclado
        if tecla == curses.KEY_UP and opcao_selecionada >= num_colunas:
            opcao_selecionada -= num_colunas
        elif tecla == curses.KEY_DOWN and opcao_selecionada < len(menu) - num_colunas:
            opcao_selecionada += num_colunas
        elif tecla == curses.KEY_LEFT and opcao_selecionada % num_colunas > 0:
            opcao_selecionada -= 1
        elif tecla == curses.KEY_RIGHT and opcao_selecionada % num_colunas < num_colunas - 1:
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
                    y = 3 + (idx // num_colunas) * 6
                    x = 5 + (idx % num_colunas) * 25
                    if y <= mouse_y < y + 5 and x <= mouse_x < x + 20:
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
