from turtle import exitonclick


frase = []
trad = []
trad2 = []
print('*-'*50)
print('SEJA BEM-VINDO(A) AO CONVERSOR DE CÓDIGO MORSE.\n')
print('*-'*50)

while True:
    choice = str(input('\n[1] - Traduzir para o código morse.\n[2] - Traduzir do código morse.\n[0] - Sair >>> ')).strip()
    if choice == '1':
        frase = str(input('Digite a frase >> ')).upper()
        conv = frase
        for c in conv:
            if c == ' ':
                trad.append(' /')
                
            elif c == '1':
                trad.append(' .----')
                
            elif c == '2':
                trad.append(' ..---')
                
            elif c == '3':
                trad.append(' ...--') 
                
            elif c == '4':
                trad.append(' ....-')  
                
            elif c == '5':
                trad.append(' .....')  
                
            elif c == '6':
                trad.append(' -....')  
                
            elif c == '7':
                trad.append(' --...')  
                
            elif c == '8':
                trad.append(' ---..')  
                
            elif c == '9':
                trad.append(' ----.') 
                
            elif c == '0':
                trad.append(' -----')
                
            elif c == 'A':
                trad.append(' .-')  
                
            elif c == 'B':
                trad.append(' -...') 
                
            elif c == 'C':
                trad.append(' -.-.')
                
            elif c == 'D':
                trad.append(' -..') 
                
            elif c == 'E':
                trad.append(' .') 
                
            elif c == 'F':
                trad.append(' ..-.')
                
            elif c == 'G':
                trad.append(' --.')   
                
            elif c == 'H':
                trad.append(' ....')  
                
            elif c == 'I':
                trad.append(' ..')  
                
            elif c == 'J':
                trad.append(' .---')  
                
            elif c == 'K':
                trad.append(' -.-')  
                
            elif c == 'L':
                trad.append(' .-..')  
                
            elif c == 'M':
                trad.append(' --')  
                
            elif c == 'N':
                trad.append(' -.')  
                
            elif c == 'O':
                trad.append(' ---')  
                
            elif c == 'P':
                trad.append(' .--.')  
                
            elif c == 'Q':
                trad.append(' --.-')  
                
            elif c == 'R':
                trad.append(' .-.')  
                
            elif c == 'S':
                trad.append(' ...')  
                
            elif c == 'T':
                trad.append(' -')  
                
            elif c == 'U':
                trad.append(' ..-')  
                
            elif c == 'V':
                trad.append(' ...-')  
                
            elif c == 'W':
                trad.append(' .--')  
                
            elif c == 'X':
                trad.append(' -..-')  
                
            elif c == 'Y':
                trad.append(' -.--')  
                
            elif c == 'Z':
                trad.append(' --..')   
            
        for ln in trad:
            print(ln, end='') 
        
    
        
    elif choice == '2':
        frase = str(input('Digite a frase em código morse (separar as letras por espaço e as palavras por barras [/]) >> '))
        conv = frase.split()
        for c in conv:
            if c == '/':
                trad2.append(' ')
                
            elif c == '.----':
                trad2.append('1')
                
            elif c == '..---':
                trad2.append('2')
                
            elif c == '...--':
                trad2.append('3') 
                
            elif c == '....-':
                trad2.append('4')  
                
            elif c == '.....':
                trad2.append('5')  
                
            elif c == '-....':
                trad2.append('6')  
                
            elif c == '--...':
                trad2.append('7')  
                
            elif c == '---..':
                trad2.append('8')  
                
            elif c == '----.':
                trad2.append('9') 
                
            elif c == '-----':
                trad2.append('0')
                
            elif c == '.-':
                trad2.append('A')  
                
            elif c == '-...':
                trad2.append('B') 
                
            elif c == '-.-.':
                trad2.append('C')
                
            elif c == '-..':
                trad2.append('D') 
                
            elif c == '.':
                trad2.append('E') 
                
            elif c == '..-.':
                trad2.append('F')
                
            elif c == '--.':
                trad2.append('G')   
                
            elif c == '....':
                trad2.append('H')  
                
            elif c == '..':
                trad2.append('I')  
                
            elif c == '.---':
                trad2.append('J')  
                
            elif c == '-.-':
                trad2.append('K')  
                
            elif c == '.-..':
                trad2.append('L')  
                
            elif c == '--':
                trad2.append('M')  
                
            elif c == '-.':
                trad2.append('N')  
                
            elif c == '---':
                trad2.append('O')  
                
            elif c == '.--.':
                trad2.append('P')  
                
            elif c == '--.-':
                trad2.append('Q')  
                
            elif c == '.-.':
                trad2.append('R')  
                
            elif c == '...':
                trad2.append('S')  
                
            elif c == '-':
                trad2.append('T')  
                
            elif c == '..-':
                trad2.append('U')  
                
            elif c == '...-':
                trad2.append('V')  
                
            elif c == '.--':
                trad2.append('W')  
                
            elif c == '-..-':
                trad2.append('X')  
                
            elif c == '-.--':
                trad2.append('Y')  
                
            elif c == '--..':
                trad2.append('Z')     
        
        for ln in trad2:
            print(ln, end='') 
        
    elif choice == '0':
        print('Programa finalizado com sucesso.')
        break

final = input('Aperte [ENTER] para finalizar.')