from src.view.song_register_view import SongRegisterView
from src.controllers.song_register_controller import SongRegisterController

# SongRegisterView -> Pascal Case ('Classes')
# song_register_process -> Snake Case ('Métodos, funções, variáveis')

def song_register_process():
    song_register_view = SongRegisterView()
    song_register_controller = SongRegisterController()
    
    new_song_informations = song_register_view.registry_song_initial()
    response = song_register_controller.insert(new_song_informations)

    if response['success']:
        return song_register_view.registry_song_success(response)
    else:
        return song_register_view.registry_song_fail(response)
