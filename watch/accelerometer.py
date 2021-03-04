import watch, time

a = watch.accelerometer()
while True:
    print( "%d %d %d" % a.read() )
    time.sleep( 0.1 )
