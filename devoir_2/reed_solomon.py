import numpy as np
from binary_domain import *


class ReedSolomon:
    def __init__(self, k, n, x, pol):
        """
        Args:
            k (int): dimension des messages à transmettre.
            n (int): taille du bloc que l'on souhaite transmettre.
            x (liste de string de taille n): les points Xi.
            pol (string): polynome irréductible.
        """
        self.f = BinaryDomains()
        self.t = Translation()
        self.k = k
        self.n = n
        self.x = x
        self.pol = pol

    def _evaluate(self, polynome, x):
        y = polynome[-1]
        for i in range(len(polynome) - 2, -1, -1):
            y = self.f.add(self.f.multiply(y, x, self.pol), polynome[i])
        return y

    def encoding(self, message_original):
        """
        Encode le message à stocker sous la forme d'une liste comportant n bytes/octets.

        Args:
            message_original (string): Le message original à encoder.

        Returns:
            (liste de string de taille n): Le message encodé.
        """
        # BEGIN TODO
        polynome = self.t.translateToMachine(message_original)
        encoded_message = [self._evaluate(polynome, xi) for xi in self.x]
        return encoded_message
        # END TODO

    def gaussian_elimination(self, X, AX):
        """
        Ex: k = 4: retourne les coefficients (di) de la fonction A(Xi) = d0 + d1*Xi + d2*Xi^2 + d3*Xi^3
        en partant de 4 points (Xi,A(Xi)).

        Ce problème est généralisé pour tout k.
        Pour le résoudre -> Effectuer l'élimination de Gauss-Jordan sur le système Vx = a.
        Avec V la matrice de Vandermonde.

        Args:
            X (liste de string de taille k): Les points Xi.
            AX (liste de string de taille k): Les points A(Xi).

        Returns:
            (liste de string de taille k): Les coefficients (di) de l'interpolation.
        """
        # BEGIN TODO
        P = [""] * self.k
        for i in range(self.k):
            line = [""] * (self.k + 1)
            x = X[i]
            line[0] = "00000001"
            line[self.k] = AX[i]
            for j in range(1, self.k):
                line[j] = x
                x = self.f.multiply(x, X[i], self.pol)
            P[i] = line
        for i in range(self.k):
            for j in range(self.k):
                if i != j:
                    r = self.f.multiply(
                        P[j][i], self.f.inverse(P[i][i], self.pol), self.pol
                    )
                    for m in range(self.k + 1):
                        P[j][m] = self.f.add(
                            P[j][m], self.f.multiply(r, P[i][m], self.pol)
                        )

        return [
            self.f.multiply(P[i][self.k], self.f.inverse(P[i][i], self.pol), self.pol)
            for i in range(self.k)
        ]

        # END TODO

    def decoding(self, message_corrupted):
        """
        Décode le message corrompu sous la forme d'une liste comportant k bytes.

        Args:
            message_corrupted (liste de string de taille n): Le message 'corrompu' reçu.

        Returns:
            (bool): True s'il est possible de décoder le message corrompu, False sinon.
            (liste de string de taille n): Le message décodé. (si bool = False, alors retourner []).
        """
        # BEGIN TODO
        X = []
        AX = []
        for i, char in enumerate(message_corrupted):
            if "x" not in char:
                X.append(self.x[i])
                AX.append(char)

        if len(AX) < (self.k):
            return False, []
        decoded_bin = self.gaussian_elimination(X, AX)
        message = self.t.translateToHuman(decoded_bin)
        return True, message
        # END TODO
