from threading import Thread, Semaphore
from pathlib import Path
from PIL import Image
import sys



class Error(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Message:

    erro_argumentos = "Argumentos inválidos."
    argumentos = f"Argumentos: <pasta ou arquivo> <suffix1> <suffix2>"
    erro = "Não foi possível converter as imagens"


class Log:

    erro_converter_imagem = lambda name, erro : print(f"Erro ao converter a imagem {name}. Erro -> {erro}")
    imagem_convertida = lambda name : print(f"Imagem {name} convertida com sucesso!")


class Constants:

    valid_suffix = {".png", ".jpg"}
    max_threads = 15


class Globals:

    semaphore = Semaphore(value=Constants.max_threads)


class UserInput:

    def __init__(self, source: Path, suffix1: str, suffix2) -> None:
        self.__source = source
        self.__suffix1 = suffix1
        self.__suffix2 = suffix2
    
    @staticmethod
    def validate(source: Path, suffix1: str, suffix2: str) -> bool:
        return (
            (source.is_file() or source.is_dir()) and
            len(Constants.valid_suffix.intersection([suffix1, suffix2])) == 2
        )
    
    @property
    def source(self) -> Path:
        return self.__source
    
    @property
    def suffix1(self) -> str:
        return self.__suffix1
    
    @property
    def suffix2(self) -> str:
        return self.__suffix2

    
class FilesToConvert:
    
    def __init__(self, user_input: UserInput) -> None:
        self.__user_input = user_input
        self.__files: list[Path] = self.__filter(self.__user_input.source)
        self.__name_list = "\n".join([f.name for f in self.__files])
    
    @property
    def files(self) -> list[Path]:
        return self.__files
    
    def __filter(self, source: Path) -> list[Path]:
        if source.is_dir():
            source: list[Path] = source.iterdir()
        else:
            source: list[Path] = [source]
        return [f for f in source if f.suffix == self.__user_input.suffix1]
    
    def __str__(self) -> str:
        return self.__name_list
    

class Convert(Thread):

    def __init__(self, image: Path, suffix1: str, suffix2: str) -> None:
        self.__image = image
        self.__suffix1 = suffix1
        self.__suffix2 = suffix2
        super().__init__(
            target = lambda : self.__convert()
        )
    
    @staticmethod
    def convert(files: FilesToConvert, user_input: UserInput) -> None:
        s1, s2 = user_input.suffix1, user_input.suffix2
        threads: list[Convert] = []
        for img in files.files:
            threads.append(Convert(img, s1, s2))
            threads[-1].start()
        [t.join() for t in threads]
    
    def __rename_image(self, image: Path) -> None:
        return image.replace(
            image.__str__().replace(self.__suffix1, self.__suffix2)
        )
    
    def __convert(self) -> None:
        Globals.semaphore.acquire()
        try:
            im: Image = Image.open(self.__image)
            new_image_name: Path = self.__rename_image(self.__image)
            im.save(new_image_name)
        except Exception as erro:
            Log.erro_converter_imagem(self.__image.name, erro)
        else:
            Log.imagem_convertida(self.__image.name)
        Globals.semaphore.release()


def get_user_input() -> UserInput:
    
    def add_dot(suffix: str) -> str:
        if suffix[0] != ".":
            return "." + suffix
        return suffix
        
    try:
        source = Path(sys.argv[1])
        suffix1 = add_dot(sys.argv[2])
        suffix2 = add_dot(sys.argv[3])
        if not UserInput.validate(source, suffix1, suffix2):
            raise IndexError
        return UserInput(source, suffix1, suffix2)
    except IndexError:
        print(Message.erro_argumentos)
        print(Message.argumentos)
        raise Error

    
def main() -> None:
    try:
        user_input: UserInput = get_user_input()
        files_to_convert: FilesToConvert = FilesToConvert(user_input)
        Convert.convert(files_to_convert, user_input)
    except Error as e:
        print(Message.erro)


if __name__ == "__main__":
    main()