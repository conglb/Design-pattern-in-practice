""" 
Sound Manager in program
"""

class MP3(object):
    """
    Play MP3 type file
    """
    def play(self):
        pass

class SoundManager(object):
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if SoundManager.__instance is not None:
            raise Exception("SoundManager class is singleton!")
        else:
            SoundManager.__instance = self

    @staticmethod 
    def getInstance():
        """ Return instance exsist, otherwise construct """
        if SoundManager.__instance is not None:
            return SoundManager.__instance
        else:
            return SoundManager()

    @staticmethod
    def playEnemyDieSound():
        return MP3().play()

if __name__ == "__main__":
    print(SoundManager.getInstance())
    print(SoundManager.getInstance())
    print(SoundManager.playEnemyDieSound())

