from telas.TelaSistema import TelaSistema
from controles.ControladorUsuario import ControladorUsuario


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__tela_usuario = ControladorUsuario()

    def inicia_sistema(self):
        self.abre_tela()

    def cadastra_usuario(self):
        self.__tela_usuario.cadastro_usuario()

    def login_usuario(self):
        pass

    def encerra(self):
        exit(0)

    def abre_tela(self):
        funcao_escolhida = self.__tela_sistema.mostra_opcoes()
        if funcao_escolhida == 1:
            self.__tela_usuario.cadastro_usuario()
            self.inicia_sistema()
        elif funcao_escolhida == 2:
            #self.login_usuario()
            print('AINDA NÃO ESTÁ DISPONIVEL')
            self.inicia_sistema()
        elif funcao_escolhida == 0:
            self.encerra()
        else:
            print('ESSA NÃO É UMA OPÇÃO VÁLIDA')
            self.inicia_sistema()