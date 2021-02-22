from m5stack import lcd

lcd.clear()
lcd.print( 'hello world', 0, 0 )

fibo_max = 150
fibo1 = 1
fibo2 = 2
y = 20

while ( fibo1 < fibo_max ):
    lcd.print( str(fibo1), 50, y )
    y += 20
    suivant = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = suivant

lcd.rect( 3, 46, 314, 194, 0x0000AA )
lcd.circle( 160, 143, 97, 0x0000AA )
