from src.view.first_view import introduction_page
from .constructor.song_register_constructor import song_register_process

def start() -> None:
    while True:
        command = introduction_page()
        if command == '1':
            song_register_process()
        elif command == '2':
            print("Adicionando playlist")
        elif command == '5': exit()
        else:
            print("\nComando não encontrado, tente novamente... \n")


            
        
