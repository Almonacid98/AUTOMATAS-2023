class Automata():
    def __init__(self, text):
        self.__text = text
    def table(self):
        print('|--------|----------------------|\n|        |  Simbolo de entrada  |\n| Estado |-----------|----------|\n|        |     a     |     b    |')
        print('|--------|-----------|----------|\n|  Q0    |    Q1     |    Q2    |\n|  Q1    |    Q3     |    Q4    |\n|  Q2    |    Q5     |    Q6    |')
        print('|  Q3    |    Q5     |    Q6    |\n|  Q4    |     -     |    Q7    |\n|  Q5    |    Q8     |    Q4    |\n|  Q6    |    Q5     |    Q6    |')
        print('|  Q7    |   Q10     |    Q4    |\n|  Q8    |    Q5     |    Q6    |\n|  Q9    |    Q5     |   Q11    |\n| Q10    |   Q10     |    Q4    |')
        print('| Q11    |    Q5     |    Q9    |\n|--------|-----------|----------|')
    def secuencias(self):
        aceptation = ['Q0', 'Q1', 'Q2', 'Q3', 'Q4', 'Q6', 'Q8', 'Q9', 'Q10', 'Q11']
        state = 'Q0'
        print('State:', state)
        for i in range(len(self.__text)):
            if state == 'Q0':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q0 to Q1')
                    state = 'Q1'
                if self.__text[i] == 'b':
                    print('Transition from Q0 to Q2')
                    state = 'Q2'
                elif state == 'Q1':
                    print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q1 to Q3')
                    state = 'Q3'
                if self.__text[i] == 'b':
                    print('Transition from Q1 to Q4')
                    state = 'Q4'
            elif state == 'Q2':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q2 to Q5')
                    state = 'Q5'
                if self.__text[i] == 'b':
                    print('Transition from Q2 to Q6')
                    state = 'Q6'
            elif state == 'Q3':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q3 to Q5')
                    state = 'Q5'
                if self.__text[i] == 'b':
                    print('Transition from Q3 to Q6')
                    state = 'Q6'
            elif state == 'Q4':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('No transition. Invalid string\n')
                if self.__text[i] == 'b':
                    print('Transition from Q4 to Q7')
                    state = 'Q7'
            elif state == 'Q5':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q5 to Q8')
                    state = 'Q8'
                if self.__text[i] == 'b':
                    print('Transition from Q5 to Q4')
                    state = 'Q4'
            elif state == 'Q6':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q6 to Q5')
                    state = 'Q5'
                if self.__text[i] == 'b':
                    print('Transition from Q6 to Q6')
                    state = 'Q6'
            elif state == 'Q7':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q7 to Q10')
                    state = 'Q10'
                if self.__text[i] == 'b':
                    print('Transition from Q7 to Q4')
                    state = 'Q4'
            elif state == 'Q8':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q8 to Q5')
                    state = 'Q5'
                if self.__text[i] == 'b':
                    print('Transition from Q8 to Q6')
                    state = 'Q6'
            elif state == 'Q9':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q9 to Q5')
                    state = 'Q5'
                if self.__text[i] == 'b':
                    print('Transition from Q9 to Q11')
                    state = 'Q11'
            elif state == 'Q10':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q10 to Q10')
                    state = 'Q10'
                if self.__text[i] == 'b':
                    print('Transition from Q10 to Q4')
                    state = 'Q4'
            elif state == 'Q11':
                print('Character:', self.__text[i])
                if self.__text[i] == 'a':
                    print('Transition from Q11 to Q5')
                    state = 'Q5'
                if self.__text[i] == 'b':
                    print('Transition from Q11 to Q9')
                    state = 'Q9'
            print('State:', state)

        if state in aceptation:
            print('ESTADO DE ACEPTACION ALCANZADO')
            return False
        else:
            print('NO SE ALCANZA A UN ESTADO DE ACEPTACIÓN. CADENA NO VÁLIDA.\n')
            return True

    def validacion(self):
        valid = ['a', 'b']
        for i in range(len(self.__text)):
            if not self.__text[i] in valid:
                print('CARACTER INVALIDO:', self.__text[i])
                return False
        return True
def main():
    text = input("INTRODUCIR CARACTER:")
    AFD = Automata(text)
    AFD.table()
    AFD.secuencias()
    AFD.validacion()
if __name__ == "__main__":
    main()
