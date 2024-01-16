#get the shuixianhua number
for I in range (100,1000) :
    if ( I // 100 ) ** 3 + (( I // 10 ) % 10 ) ** 3 + ( I % 10 ) ** 3 == I :
        print (I)