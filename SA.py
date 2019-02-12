# Filename: SA.py
# ALGORITME SIMULATED ANNEALING

# AWAL: Struktur Data Untung (4 ~ 130)
import random
import math

class nything:
    'class nything is a class that solve NythingProblem from fileInput'
    # attribute
    nNything = 0

    # method
    def __init__(self, fileInput):
        # put information in fileInput (in .txt) to attribute

        # init chess pieces counter and array of chess pieces
        self.nWhiteKnight = 0
        self.nWhiteBishop = 0
        self.nWhiteRook = 0
        self.nWhiteQueen = 0
        self.nBlackKnight = 0
        self.nBlackBishop = 0
        self.nBlackRook = 0
        self.nBlackQueen = 0
        self.chessPieces = []

        # read fileInput
        f = open("test/" + fileInput + ".txt", "r")
        lines = f.read().splitlines()
        # print(lines)
        f.close()

        # put into self attribute
        for line in lines:
            words = line.split(" ")
            if words[0] == "WHITE":
                if words[1] == "KNIGHT":
                    self.nWhiteKnight = int(words[2])
                    for i in range(self.nWhiteKnight):
                        self.chessPieces += "K"
                elif words[1] == "BISHOP":
                    self.nWhiteBishop = int(words[2])
                    for i in range(self.nWhiteBishop):
                        self.chessPieces += "B"
                elif words[1] == "ROOK":
                    self.nWhiteRook = int(words[2])
                    for i in range(self.nWhiteRook):
                        self.chessPieces += "R"
                elif words[1] == "QUEEN":
                    self.nWhiteQueen = int(words[2])
                    for i in range(self.nWhiteQueen):
                        self.chessPieces += "Q"
            elif words[0] == "BLACK":
                if words[1] == "KNIGHT":
                    self.nBlackKnight = int(words[2])
                    for i in range(self.nBlackKnight):
                        self.chessPieces += "k"
                elif words[1] == "BISHOP":
                    self.nBlackBishop = int(words[2])
                    for i in range(self.nBlackBishop):
                        self.chessPieces += "b"
                elif words[1] == "ROOK":
                    self.nBlackRook = int(words[2])
                    for i in range(self.nBlackRook):
                        self.chessPieces += "r"
                elif words[1] == "QUEEN":
                    self.nBlackQueen = int(words[2])
                    for i in range(self.nBlackQueen):
                        self.chessPieces += "q"
            # if it is not white nor black, it is ignored

        # add object counter
        nything.nNything += 1

    def printAttr(self):
        # print attribute
        print("nWhiteKnight : " + str(self.nWhiteKnight))
        print("nWhiteBishop : " + str(self.nWhiteBishop))
        print("nWhiteRook : " + str(self.nWhiteRook))
        print("nWhiteQueen : " + str(self.nWhiteQueen))
        print("nBlackKnight : " + str(self.nBlackKnight))
        print("nBlackBishop : " + str(self.nBlackBishop))
        print("nBlackRook : " + str(self.nBlackRook))
        print("nBlackQueen : " + str(self.nBlackQueen))
        print(self.chessPieces)
        for row in self.chessBoard:
            print(row)

    def randomize(self):
        # randomize chess pieces in matrix based on attributes

        # init chess' locator
        self.chessLocator = []

        # init chess board
        self.chessBoard = [
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."]
        ]

        # put chess piece to board
        for piece in self.chessPieces:
            r = random.randint(0,7) # index 0 - 7
            c = random.randint(0,7)
            self.chessBoard[r][c] = piece
            self.chessLocator.append((piece, r, c))

    def changePiece(piece1, piece2):
        # change piece at chessBoard
        # piece1 and piece2 are tuple of piece, row index, and column index
        x, r1, c1 = piece1
        y, r2, c2 = piece2
        # x and y are unused

        # move piece on board
        temp = self.chessBoard[r1][c1]
        self.chessBoard[r1][c1] = self.chessBoard[r2][c2]
        self.chessBoard[r2][c2] = temp
    
    def hValue(piece):
    # return height value of x position
        return 0
        
# AKHIR: Struktur Data Untung (4 ~ 130)

    def matrixOfNextState(state):
    # Mengembalikan senarai yang berisi kumpulan state selanjutnya yang memungkinkan
        nextState = []  # Variabel untuk menyimpan state selanjutnya
        
        def isValid(Angka1, Angka2):
        # Periksa keabsahan koordinat di jangkauan
            return ((Angka1 >= 0) and (Angka1 <= 7) and (Angka2 >= 0) and (Angka2 <= 7))
        
        def isEmpty(state, row, col):
        # Mencari keberadaan suatu bidak di posisi row col
            Kosong = True
            for bidak in state:
                if ((state[bidak][1] == row) and (state[bidak][2] == col)):
                    Kosong = False
                    break
                    
            return Kosong
        
        def newStateExcept(state, bidakLama, bidakBaru):
        # Menjadikan suatu senarai yang berisi satu state, tapi membuang state yang ada di parameter
            stateBaru = [i for i in state if i != bidakLama] 
            stateBaru.append(bidakBaru)
            return stateBaru
        
        # BENTENG BERJALAN
        def Benteng(state, bidak):
        # Mengisi state yang memungkinkan si benteng untuk berjalan ke arah yang dikehendaki
            Brs = bidak[1]
            Kol = bidak[2]
            
            # Tahap Berjalan ke Kiri
            for col in range(Kol, 0):
                if (isEmpty(state, Brs, col)):
                    nextState.append(newStateExcept( state, bidak, ('R', Brs, col) ))
                else:   # Ada penghalang, sehingga akhir dari perjalanan
                    break
            
            # Tahap Berjalan ke Kanan
            for col in range(Kol, 7):
                if (isEmpty(state, Brs, col)):
                    nextState.append(newStateExcept( state, bidak, ('R', Brs, col) ))
                else:   # Ada penghalang
                    break
                    
            # Tahap Berjalan ke Atas
            for row in range(Brs, 0):
                if (isEmpty(state, row, Kol)):
                    nextState.append(newStateExcept( state, bidak, ('R', row, Kol) ))
                else:   # Ada penghalang
                    break
            
            # Tahap Berjalan ke Bawah
            for row in range(Brs, 7):
                if (isEmpty(state, row, Kol)):
                    nextState.append(newStateExcept( state, bidak, ('R', row, Kol) ))
                else:   # Ada penghalang
                    break
            
        # KUDA BERJALAN
        def Kuda(state, bidak):
        # Mengisi state yang memungkinkan si kuda untuk berjalan ke arah yang dikehendaki
            Brs = bidak[1]
            Kol = bidak[2]
            Gerak1 = [-2, 2]
            Gerak2 = [-1, 1]
            for i in range(0, 1):
                for j in range(0, 1):
                    Baris = Brs + Gerak1[i]
                    Kolom = Kol + Gerak2[j]
                    if (isValid(Baris, Kolom)):
                        if (isEmpty(state, Baris, Kolom)):
                            nextState.append(newStateExcept( state, bidak, ('K', Baris, Kolom) ))

        # MENTERI BERJALAN
        def Menteri(state, bidak):
        # Mengisi state yang memungkinkan si benteng untuk berjalan ke arah yang dikehendaki
            Brs = bidak[1]
            Kol = bidak[2]
            
            # Tahap Berjalan ke Kanan Bawah
            for i in range(1, 7):
                Baris = Brs + i
                Kolom = Kol + i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('B', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
            # Tahap Berjalan ke Kiri Atas
            for i in range(1, 7):
                Baris = Brs - i
                Kolom = Kol - i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('B', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
                    
            # Tahap Berjalan ke Kanan Atas
            for i in range(1, 7):
                Baris = Brs - i
                Kolom = Kol + i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('B', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
            # Tahap Berjalan ke Kiri Bawah
            for i in range(1, 7):
                Baris = Brs + i
                Kolom = Kol - i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('B', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
        # RATU BERJALAN
        def Ratu(state, bidak):
        # Mengisi state yang memungkinkan si ratu untuk berjalan ke arah yang dikehendaki
            Brs = bidak[1]
            Kol = bidak[2]
            
            # PERGERAKAN MENYERUPAI "BENTENG"
            # Tahap Berjalan ke Kiri
            for col in range(Kol, 0):
                if (isEmpty(state, Brs, col)):
                    nextState.append(newStateExcept( state, bidak, ('Q', Brs, col) ))
                else:   # Ada penghalang, sehingga akhir dari perjalanan
                    break
            
            # Tahap Berjalan ke Kanan
            for col in range(Kol, 7):
                if (isEmpty(state, Brs, col)):
                    nextState.append(newStateExcept( state, bidak, ('Q', Brs, col) ))
                else:   # Ada penghalang
                    break
                    
            # Tahap Berjalan ke Atas
            for row in range(Brs, 0):
                if (isEmpty(state, row, Kol)):
                    nextState.append(newStateExcept( state, bidak, ('Q', row, Kol) ))
                else:   # Ada penghalang
                    break
            
            # Tahap Berjalan ke Bawah
            for row in range(Brs, 7):
                if (isEmpty(state, row, Kol)):
                    nextState.append(newStateExcept( state, bidak, ('Q', row, Kol) ))
                else:   # Ada penghalang
                    break
            
            # PERGERAKAN MENYERUPAI "MENTERI"
            # Tahap Berjalan ke Kanan Bawah
            for i in range(1, 7):
                Baris = Brs + i
                Kolom = Kol + i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('Q', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
            # Tahap Berjalan ke Kiri Atas
            for i in range(1, 7):
                Baris = Brs - i
                Kolom = Kol - i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('Q', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
                    
            # Tahap Berjalan ke Kanan Atas
            for i in range(1, 7):
                Baris = Brs - i
                Kolom = Kol + i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('Q', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
            # Tahap Berjalan ke Kiri Bawah
            for i in range(1, 7):
                Baris = Brs + i
                Kolom = Kol - i
                if (isValid(Baris, Kolom)):
                    if (isEmpty(state, Baris, Kolom)):
                        nextState.append(newStateExcept( state, bidak, ('Q', Baris, Kolom) ))
                    else:   # Ada penghalang
                        break
                else:       # Di luar jangkauan catur
                    break
            
        # ALGORITME LOKAL
        for pieces in state:
            if (pieces[0] == 'R'):      # Memasukkan pergerakan Benteng
                Benteng(state, pieces)
            elif (pieces[0] == 'K'):    # Memasukkan pergerakan Kuda
                Kuda(state, pieces)
            elif (pieces[0] == 'B'):    # Memasukkan pergerakan Menteri
                Menteri(state, pieces)
            elif (pieces[0] == 'Q'):    # Memasukkan pergerakan Ratu
                Ratu(state, pieces)
            
        return nextState
        

    def simulatedAnnealing(self, suhu, pendinginan):
    # Prosedur menjalankan algoritme Simulated Annealing
        def PeluangKonstan():
        # Mengembalikan nilai peluang yang dipilih langsung (nilai boleh diubah selama berada di jangkauan 0.000...1 ~ 0.999...)
            return 0.1

        def PeluangMenurun(P, Temperature):
        # Mengembalikan niai peluang yang menurun secara perlahan
            return P * Temperature

        def PeluangBoltzmann(e, ei, suhu):
        # Mengembalikan nilai hasil dari distribusi Boltzmann
            return math.exp((ei - e) / suhu)

        def PeluangAcak():
        # Mengembalikan nilai peluang secara acak
            return random.random()
        
        # 1. Tahap Inisialisasi (penempatan bidak secara acak)
        X = self.chessLocator
        
        # 2. Tahap Menghitung Nilai Heuristik Pertama dengan nama 'E' berdasarkan slide
        E = 0
        for bidak in X:
            E += hValue(bidak)
        
        while (suhu > 1):
            # 3. Tahap Menghitung Jumlah Kemungkinan Pergerakan untuk Seluruh Bidak
            i = matrixOfNextState(X)  # MENUNGGU KABAR
            
            # 4. Tahap Menghitung Nilai Heuristik Kedua dengan nama 'Ei' berdasarkan slide
            Ei = 0
            NomorAcak = random.randint(0, len(i))
            for bidak in i[NomorAcak]:
                Ei += hValue(bidak)
                
            # 5. Membandingkan Nilai Heuristik Satu Sama Lain
            if (E <= Ei):
                E = Ei
                X = i[NomorAcak]
            else:   # Menggunakan Peluang Konstan (dapat diganti dengan Boltzmann atau Pengurangan)
                if (PeluangAcak() < PeluangKonstan()):
                    X = i[NomorAcak]
                    E = Ei
                    
            suhu *= pendinginan
            
        return X

