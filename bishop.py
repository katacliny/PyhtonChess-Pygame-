from pice import Piece
from move import up, down, rigth, left, bishopDownRigth, bishopDownLeft, bishopUpRigth, bishopUpLeft

class Bishop(Piece):
    
    def __init__(self, posx, posy, color, table_map):
        super(Bishop, self).__init__(posx, posy, table_map, "B", move=[bishopDownRigth, bishopDownLeft, bishopUpRigth, bishopUpLeft]  )
        self.posy = posx
        self.posx = posy
        self.color = color
        self.rangelen = 8