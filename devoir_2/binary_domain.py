import numpy


class Translation:

    def toBinary(self, n):
        """
        Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

        Args:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        Returns:
            str_bin (string): Forme binaire de l'entier en string.
        """
        str_bin = "".join(str(1 & int(n) >> i) for i in range(8)[::-1])
        return str_bin

    def toInt(self, str_bin):
        """
        Convertit un string contenant la séquence sur un octet (ou 8 bits) en un entier n.

        Args:
            str_bin (string): Forme binaire de l'entier en string.
        Returns:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        """
        n = int(str_bin, 2)
        return n

    def translateToMachine(self, phrase):
        """
        Convertit une phrase (encodée comme un string) en une liste de strings d'octets (ou 8 bits).

        Args:
            phrase (string): Phrase en français ou en anglais.
        Returns:
            phrase_bin (list of strings): Liste de strings, chaque string représente un octet/8 bits
        """
        phrase_bin = [self.toBinary(ord(char)) for char in phrase]
        return phrase_bin

    def translateToHuman(self, bin_phrase):
        """
        Convertit une liste de strings d'octets (ou 8 bits) en une phrase (encodée comme un string).

        Args:
            bin_phrase (list of strings): Liste de strings, chaque string représente un octet/8 bits
        Returns:
            phrase (string): Phrase en français ou en anglais.
        """
        phrase = ""
        for bin_str in bin_phrase:
            phrase += chr(self.toInt(bin_str))
        return phrase


class BinaryDomains:

    def toBinary(self, n):
        """
        Convertit un entier n en un string contenant la séquence sur un octet (ou 8 bits).

        Args:
            n (int): L'entier à convertir en représentation binaire 8 bits.
        Returns:
            string: Forme binaire de l'entier en string.
        """
        return "".join(str(1 & int(n) >> i) for i in range(8)[::-1])

    def add(self, x, y):
        """
        Additionne deux séquences binaires (x+y) reçues sous la forme de string.

        Example : "10111001" + "10010100" = "00101101".

        Args:
            x (string): Premier élément de l'addition.
            y (string): Deuxième élément de l'addition.

        Returns:
            string: Résultat de l'addition x+y en binaire.
        """

        sum = ""
        for i in range(8):
            if x[i] == y[i]:
                sum += "0"
            else:
                sum += "1"
        return sum

    def multiply(self, a, b, pol):
        """
        Multiplie deux séquences binaires (x*y) reçues sous la forme de string, en utilisant
        le polynôme irréductible choisi pour le corps.

        Example : "10111001" * "10010100" = "10110010" avec comme polynôme irréductible ""

        Args:
            x (string): Premier élément de la multiplication.
            y (string): Deuxième élément de la multiplication.
            pol (string): Polynome irréductible

        Returns:
            string: Résultat de la multiplication x*y en binaire.
        """
        mult = "00000000"
        while b != "00000000":
            if b[-1] == "1":
                mult = self.add(mult, a)
            # a = a(X)X mod P(X)
            ax = a[1:] + "0"
            if a[0] == "1":
                a = self.add(ax, pol[1:])
            else:
                a = ax

            b = "0" + b[0:-1]

        return mult

    def inverse(self, a, pol):
        """
        Inverse un élément (x^(-1)) du corps donné sous la forme d'une séquence binaire.

        Example : ("10111001")^(-1) = "10001110" avec comme polynôme irréductible ""

        Args:
            x (string): Elément à inverser.
            pol (string): Polynome irréductible

        Returns:
            string: Résultat de l'inversion en binaire.
        """
        a = self.multiply(a, a, pol)
        inverse = a
        for i in range(6):
            a = self.multiply(a, a, pol)
            inverse = self.multiply(a, inverse, pol)
        return inverse
