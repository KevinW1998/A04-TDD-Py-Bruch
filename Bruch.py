

class Bruch(object):
    """
    The Bruch-Class represents a fraction with a integer-divisor and
    a integer-dividend. Nearly all operators can be used with this class.
    """

    def __init__(self, divisor_or_bruch, dividend = None):
        """
        Creates a new Bruch-Object (fraction) containing a divisor and a dividend

        :param divisor_or_bruch: The divisor or a Bruch-Instance to copy
        :param dividend: The dividend or None if the Bruch should represent a full number by the divisor
        :type divisor_or_bruch: int
        :type divisor_or_bruch: Bruch A Bruch-Instance to copy
        :type dividend: int
        :type dividend: None The divisor is represented as a full number (the dividend is 1)
        """
        if type(divisor_or_bruch) == Bruch:
            self.zaehler = divisor_or_bruch.zaehler
            self.nenner = divisor_or_bruch.nenner
        else:
            # If dividend is None, then the dividend is 1
            if dividend is None:
                dividend = 1

            if type(divisor_or_bruch) != int:
                raise TypeError("Divisor (Zaehler) has the wrong type")
            if type(dividend) != int:
                raise TypeError("Dividend (Nenner) has the wrong type")

            if dividend == 0:
                raise ZeroDivisionError("Dividend (Nenner) must not be zero")

            # If both are negative, then we can flip it!
            if divisor_or_bruch < 0 and dividend < 0:
                divisor_or_bruch = -divisor_or_bruch
                dividend = -dividend

            self.zaehler = divisor_or_bruch
            self.nenner = dividend

    # == Utils ==
    def __calc(self):
        return float(self.zaehler) / float(self.nenner)

    # == Make Bruch Factory ==
    @staticmethod
    def __makeBruch(value):
        return Bruch(value)

    # == To string ==
    def __repr__(self):
        """
        Converts the fraction to a string

        :return: A string representing the fraction
        """
        if self.nenner == 1:
            return "(%d)" % self.zaehler
        return "(%d/%d)" % (self.zaehler, self.nenner)

    # == Comparing ==
    def __eq__(self, other):
        """
        Compares if the fraction is equal with a int or a Bruch

        :param other: value to compare
        :type other: int
        :type other: Bruch
        :return: If it is equal
        """
        return self.__calc() == float(other)

    def __le__(self, other):
        """
        Compares if the fraction is lesser or equal with a int or a Bruch

        :param other: value to compare
        :type other: int
        :type other: Bruch
        :return: If it is lesser or equal
        """
        return self.__calc() <= float(other)

    def __ge__(self, other):
        """
        Compares if the fraction is greater or equal with a int or a Bruch

        :param other: value to compare
        :type other: int
        :type other: Bruch
        :return: If it is greater or equal
        """
        return self.__calc() >= float(other)

    def __lt__(self, other):
        """
        Compares if the fraction is less than a int or a Bruch

        :param other: value to compare
        :type other: int
        :type other: Bruch
        :return: If it is lesser
        """
        return self.__calc() < float(other)

    def __gt__(self, other):
        """
        Compares if the fraction is greater than a int or a Bruch

        :param other: value to compare
        :type other: int
        :type other: Bruch
        :return: If it is greater
        """
        return self.__calc() > float(other)

    def __ne__(self, other):
        """
        Compares if the fraction is not equal with a int or a Bruch

        :param other: value to compare
        :type other: int
        :type other: Bruch
        :return: If it is not equal
        """
        return self.__calc() != float(other)

    # == Arithmetic ==
    def __iadd__(self, other):
        """
        Adds a Bruch or a int to the fraction

        :param other: value to add
        :type other: int
        :type other: Bruch
        :return: The given instance
        """
        if type(other) == int:
            self += Bruch(other)
            return self

        if type(other) != Bruch:
            raise TypeError("Value to add must be int or Bruch")

        # Calc the same nenner
        same_nenner = self.nenner * other.nenner
        self.zaehler = self.zaehler * (same_nenner // self.nenner) + other.zaehler * (same_nenner // other.nenner)
        self.nenner = same_nenner
        return self

    def __add__(self, other):
        """
        Adds a the fraction and a Bruch or a int

        :param other: value to add
        :type other: int
        :type other: Bruch
        :return: A new Bruch-Instance
        """
        out = Bruch(self.zaehler, self.nenner)
        out += other
        return out

    def __radd__(self, other):
        """
        Adds a the fraction and a Bruch or a int

        :param other: value to add
        :type other: int
        :type other: Bruch
        :return: A new Bruch-Instance
        """
        return self + other

    def __isub__(self, other):
        """
        Subtracts a Bruch or a int from the fraction

        :param other: value to subtract
        :type other: int
        :type other: Bruch
        :return: The given instance
        """
        self += -other
        return self

    def __sub__(self, other):
        """
        Subtracts a Bruch or a int from the fraction

        :param other: value to subtract
        :type other: int
        :type other: Bruch
        :return: A new Bruch-Instance
        """
        out = Bruch(self.zaehler, self.nenner)
        out -= other
        return out

    def __rsub__(self, other):
        """
        Subtracts the fraction from an int or a Bruch

        :param other: value from which it should be subtracted from
        :type other: int
        :type other: Bruch
        :return: A new Bruch-Instance
        """
        return -self + other


    def __imul__(self, other):
        """
        Multiplies the fraction with an int or a Bruch

        :param other: value to multiply
        :type other: int
        :type other: Bruch
        :return: The given instance
        """
        if type(other) == int:
            self *= Bruch(other)
            return self

        if type(other) != Bruch:
            raise TypeError("Value to multiply must be int or Bruch")

        self.zaehler *= other.zaehler
        self.nenner *= other.nenner
        return self

    def __mul__(self, other):
        """
        Multiplies the fraction with an int or a Bruch

        :param other: value to multiply
        :type other: int
        :type other: Bruch
        :return: A new Bruch-Instance
        """
        out = Bruch(self.zaehler, self.nenner)
        out *= other
        return out

    def __rmul__(self, other):
        """
        Multiplies the fraction with an int or a Bruch

        :param other: value to multiply
        :type other: int
        :type other: Bruch
        :return: A new Bruch-Instance
        """
        return self * other

    def __itruediv__(self, other):
        """
        Divides the fraction with an int or a Bruch

        :param other: value to divide
        :type other: int
        :type other: Bruch
        :return: The given instance
        """
        if type(other) == int:
            self *= Bruch(1, other)
            return self

        if type(other) != Bruch:
            raise TypeError("Value to divide must be int or Bruch")

        self *= Bruch(other.nenner, other.zaehler)
        return self

    def __truediv__(self, other):
        """
        Divides the fraction with an int or a Bruch

        :param other: value to divide
        :type other: int
        :type other: Bruch
        :return: A new Bruch-Instance
        """
        out = Bruch(self.zaehler, self.nenner)
        out /= other
        return out

    def __rtruediv__(self, other):
        """
        Divides an int or a Bruch with the fraction

        :param other: value to with the fraction should be divided
        :type other: int
        :type other: Bruch
        :return: A new Bruch-Instance
        """
        out = Bruch(self.nenner, self.zaehler)  # reciprocal
        out *= other
        return out

    def __invert__(self):
        """
        Inverts the fraction by swapping the divisor and the dividend

        :return: A new Bruch-Instance
        """
        return Bruch(self.nenner, self.zaehler)

    def __pow__(self, power, modulo=None):
        """
        Raises the fraction by the given power

        :param power: The given power
        :return: A new Bruch-Instance
        """
        if type(power) != int:
            raise TypeError("Power must be int")
        return Bruch(self.zaehler ** power, self.nenner ** power)

    def __abs__(self):
        """
        Returns the absolute value of the fraction

        :return: A new Bruch-Instance
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __neg__(self):
        """
        Negates the fraction

        :return: A new Bruch-Instance
        """
        return Bruch(-self.zaehler, self.nenner)

    # == Conversions ==
    def __int__(self):
        """
        Calculates the fraction to a floating-point number and then floors the value to an int

        :return: A int representing the fraction
        """
        return int(self.__calc())

    def __float__(self):
        """
        Converts the fraction to a floating-point number

        :return: A floating-point number representing the fraction
        """
        return float(self.__calc())

    def __complex__(self):
        """
        Converts the fraction to a complex number

        :return: A complex number representing the fraction
        """
        return complex(self.__calc())


    # == Other ==

    def __len__(self):
        return 2

    def __iter__(self):
        """
        Returns a iterator with divisor and dividend

        :return: A iterator with the divisor and dividend
        """
        return iter([self.zaehler, self.nenner])

