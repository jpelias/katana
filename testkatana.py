# -*- coding: utf-8 -*-
#"ぐ"  12352    

import random
        
salida = ""
key = 1542 -32 
f = 0

tabla = random.sample(range(key,key+256), 256)


#tabla = [20159, 20220, 20050, 20087, 20073, 20145, 20093, 20040, 20098, 19981, 20019, 20024, 20032, 20038, 20123, 20181, 20090, 20095, 20025, 20022, 20102, 20213, 20135, 20033, 20168, 20044, 20001, 20170, 19992, 20166, 20076, 20167, 20078, 19999, 20048, 19985, 20149, 20113, 20035, 20173, 20209, 19982, 20070, 20211, 20129, 20071, 20036, 19996, 20115, 20000, 20148, 20205, 19986, 20052, 20085, 20197, 20057, 20017, 20153, 20118, 20037, 19971, 20182, 20198, 19994, 20169, 20103, 20016, 20051, 20178, 20120, 20075, 20088, 20091, 20218, 20072, 20206, 20009, 20042, 20074, 20180, 20082, 20116, 20015, 20012, 20141, 20208, 20111, 20151, 20108, 20007, 20193, 20083, 20127, 20152, 20105, 20210, 20158, 20207, 20084, 20029, 19980, 20013, 20080, 20027, 20023, 20137, 19976, 20089, 19970, 20020, 20217, 20053, 20101, 20004, 20065, 20219, 20106, 20191, 20156, 20201, 19969, 20039, 20122, 20162, 20128, 20068, 20008, 20179, 20131, 20150, 19975, 20130, 20056, 20161, 20107, 20030, 19998, 20132, 20069, 20077, 20196, 20059, 20028, 20043, 20125, 20174, 19984, 20067, 20094, 20011, 20005, 20124, 20112, 20188, 20110, 20222, 20202, 20157, 20147, 20081, 20216, 20172, 20097, 19990, 20138, 20002, 20144, 20189, 20031, 19978, 20003, 20139, 20203, 20064, 20200, 19979, 20109, 20192, 20195, 20186, 20221, 20066, 20171, 19977, 20060, 20114, 19972, 20223, 20079, 20185, 20104, 20062, 20177, 20187, 20199, 20194, 19988, 20121, 20063, 20117, 20092, 20155, 20045, 20164, 20146, 19997, 20140, 19974, 20041, 20160, 19993, 19989, 20126, 19991, 20184, 20049, 19983, 20214, 20047, 20014, 20099, 19973, 19987, 20100, 20154, 20183, 20142, 20034, 20055, 20136, 20061, 20215, 20204, 20143, 20006, 20165, 20175, 20010, 20176, 20018, 20058, 20086, 20133, 20096, 20134, 20119, 19968, 20026, 20046, 20190, 19995, 20212, 20163, 20054, 20021]

for s in range(32,256):

    f = s

    if (s > key): 
        #f = s - key
        f = tabla.index(s)
    if ( s < 256 ) & ( s > 31): 
        if ( s < 127 ) or ( s > 159): 
            f = s + key
            #f = tabla[s] 
            print s,unichr(s),f,unichr(f),tabla[s],unichr(tabla[s]) 
            
#print random.sample(range(19968,19968+256), 256)
