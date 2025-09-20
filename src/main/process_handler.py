from src.view.first_view import introduction_page
from .constructor.song_register_constructor import song_register_process
from .constructor.playlistc_creator_constructor import playlist_creator_proccess

def start() -> None:
    while True:
        command = introduction_page()
        if command == '1':
            song_register_process()
        elif command == '2':
            playlist_creator_proccess()
        elif command == '5': exit()
        else:
            print("\nComando não encontrado, tente novamente... \n")


            
        
