# Proxy classes often evoke the is-a versus has-a debate
# Problems: have many player play a multiplayer game
# each player is an instant of Player class
# Player own a method which send message to others player over the internet
# and return a others player's acknowledge
# This code nearly just saw in server-side.

class Player(object):
    
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        """ Return player's name """
        return self.name

    def sendInstantMessage(self, inMessage):
        """ Sends an instant message to the player over the network and returns the reply as a string. Network connectivity is required """
        if inMessage == 'You have won! Play again?':
            # Yes if player click play again, otherwise
            # it was sent from client
            return 'yes' # change it for testing

class PlayerProxy(Player):
    def sendInstantMessage(self, inMessage):
        hasNetworkConnectivity = True # change this variable's value to test
        if hasNetworkConnectivity:
            return super().sendInstantMessage(inMessage)
        else:
            return "The player counld not be contacted."

# Server class
def informWinner(inPlayer):
    result = inPlayer.sendInstantMessage('You have won! Play again?')
    if result == 'yes':
        print(inPlayer.getName() + ' wants to play again')
    else:
        print(inPlayer.getName() + ' does want to play again')

if __name__ == "__main__":
    p1 = PlayerProxy('Winnerahihi')
    p2 = PlayerProxy("LuBo")
    p3 = PlayerProxy("DieuThuyen")
    informWinner(p1)