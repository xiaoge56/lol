# from collections import deque
# import zlib
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# blink='\n'


# def main():
#     t=[[u'Zz\u4e28Aunty\u4e36yiNg', u'\u9ed1\u6697\u4e4b\u5973', u'7.2', u'218', u'1', u'4', u'0', u'9', u'0', u'3', u'1', u'0', u'2314', u'192901', u'20771', u'26817', u'724', u'25441', u'652'], [u'Zz\u4e28Uncle\u4e36shaN', u'\u9b42\u9501\u5178\u72f1\u957f', u'5.9', u'60', u'3', u'0', u'0', u'39', u'6', u'0', u'1', u'0', u'3640', u'59277', u'40965', u'8741', u'1188', u'7343', u'210'], [u'cArry\u827e\u5c3c\u7ef4\u4e9a', u'\u51b0\u6676\u51e4\u51f0', u'11.1', u'218', u'36', u'0', u'0', u'16', u'0', u'7', u'2', u'1673', u'18012', u'303250', u'42836', u'57700', u'1432', u'55046', u'1222'], [u'Zz\u4e28Uncle\u4e36yaNg', u'\u96ea\u4eba\u9a91\u58eb', u'11.4', u'111', u'61', u'0', u'0', u'5', u'3', u'5', u'1', u'0', u'21540', u'226981', u'60843', u'12365', u'1363', u'10552', u'449'], [u'Zz\u4e28Gucci\u4e36ViruS', u'\u6218\u4e89\u5973\u795e', u'11.3', u'421', u'70', u'5', u'2', u'7', u'1', u'7', u'3', u'1863', u'5429', u'580311', u'31967', u'68418', u'62619', u'3203', u'2595'], [u'\u53d1\u75af\u7684\u5c0f\u8349\u5e3d', u'\u4ea1\u7075\u6218\u795e', u'7.1', u'177', u'7', u'0', u'0', u'12', u'0', u'2', u'1', u'0', u'37183', u'166746', u'66636', u'29913', u'18460', u'11452', u'0'], [u'\u4e09\u7eb7\u7ee3\u6c14', u'\u865a\u7a7a\u5148\u77e5', u'8.1', u'195', u'33', u'0', u'0', u'9', u'2', u'5', u'2', u'0', u'389', u'231287', u'33265', u'52869', u'5145', u'46168', u'1556'], [u'YUMIKOOO', u'\u751f\u5316\u9b54\u4eba', u'5.2', u'57', u'90', u'0', u'0', u'11', u'2', u'0', u'1', u'0', u'36281', u'185452', u'51670', u'18388', u'394', u'17889', u'104'], [u'\u4ffa\u7528\u82de\u7c73\u6345\u4f60\u83ca\u82b1', u'\u66d9\u5149\u5973\u795e', u'6.4', u'65', u'0', u'1', u'0', u'31', u'4', u'0', u'1', u'0', u'2854', u'34687', u'38003', u'9070', u'2150', u'6920', u'0'], [u'\u5927\u82de\u7c73', u'\u76ae\u57ce\u5973\u8b66', u'11.7', u'335', u'12', u'1', u'0', u'10', u'3', u'4', u'2', u'1633', u'3201', u'351521', u'22950', u'49559', u'40053', u'9055', u'451']]
#     for m in t:
#         print ''.join(m)
#     with open('./test.txt','a+') as f:
#         for i in t:
#             m='||'.join(i)
#             f.write(m+blink)
#     f.close()
#     print 'aaa'
# if __name__=='__main__':
#     print 'aaa'
#     main()
    

# print 'a'


import os
import sys
import math
import string

def leapyear(year):
    if ((year%4 == 0) and (year%100 != 0))or((year%4 == 0) and (year%100 ==0)):
        return True
        #print 'This year is leap year!'
    else:
        return False
        #print 'This year is not leap year!'

if __name__ == '__main__':
    #raw_input('Please input your number:
    y = [1992,1996,2000,1967,1900,2400]
    #s = 'This year is leap year!'
    leap = []
    for year in y:
        if leapyear(year) == 1:
            leap.append(year)
    print 'The leap years are'
    print leap   
