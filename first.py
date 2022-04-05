# kate = 8
# maks = 7
#
# if kate != maks:
#    print("Result_1 = " + str(kate) + " > " + str(maks))
# elif kate == maks:
#    print("Result_2 = " + str(kate) + " = "  + str(maks))
# elif kate > maks:
#    print("Result_3 = " + str(kate) + " < "  + str(maks))

#if kate:
#    print("kate = " + str(kate))
#else:
#    print("NOT_kate = " + str(kate))


count = 0
while count <= 10:
    if count < 5:
        print("1Result <5 = " + str(count))
    if count == 5:
       print("2Result ==5 = " +  str(count))
    if count > 6 and count <= 8:
       print("3Result 7-8 = " +  str(count))
    if count == 10:
        print("4Result 10 = " + str(count))
    print("count = " + str(count))
    count += 1
    print ('==================')
