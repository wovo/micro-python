import watch, time

r = watch.rtc()
while True:
    print( "%02d:%02d:%02d" % r.read() )
    time.sleep( 1 )