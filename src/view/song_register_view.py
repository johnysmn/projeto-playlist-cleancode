import os

class SongRegisterView:
    def registry_song_initial(self) -> dict:
        self.__clear()
        print("Implementar Nova Música \n\n")

        title = input("Determine o nome da música: ")
        artist = input("Determine o nome do artista: ")
        year = input("Determine o ano de publicacao: ")

        new_song_informations = {
            'title' : title, 'artist' : artist, 'year' : year
        }

        return new_song_informations

    def registry_song_success(self, controller_response: dict) -> None:
        self.__clear()

        message = '''
            Música cadastrada com sucesso!
            * Título: {}
            * Quantidade: {}
        '''.format(
            controller_response['atributtes']['title'], 
            controller_response['count']
        )
        print(message)

    def registry_song_fail(self, controller_response: dict) -> None:
        self.__clear()

        message = '''
            Falha ao registrar música!
            * Erro: {}
        '''.format(
            controller_response['error']
        )
        print(message)
        
    def __clear(self):
        os.system("cls||clear")