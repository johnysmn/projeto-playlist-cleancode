from src.view.song_register_view import SongRegisterView

# SongRegisterView -> Pascal Case ('Classes')
# song_register_process -> Snake Case ('Métodos, funções, variáveis')

def song_register_process():
    song_register_view = SongRegisterView()
    # instância do controller
    new_song_informations = song_register_view.registry_song_initial()
    # enviar new_song_informations para controller
