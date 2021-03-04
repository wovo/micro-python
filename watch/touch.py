import watch, time

print( "touch demo - touch the display!" )
t = watch.touch()
while True:
    v = t.read()
    if v:
        print( v )
    time.sleep( 0.1 )