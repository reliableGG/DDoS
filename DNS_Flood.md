DNS_Flood攻击


UDP：用户数据报协议：
UDP检验和覆盖UDP首部和UDP数据，不同于IP首部的检验和，它只覆盖IP的首部---并不覆盖IP数据报中的任何数据
UDP和TCP在首部中都有覆盖他们首部和数据的检验和，UDP的检验和是可选的，而TCP的检验和是必需的


UDP和TCP检验和的基本计算方法：16bit字的二进制反码和

不同的是： UDP数据报的长度可以为奇数字节，但是检验和算法是把若干个16bit字相加。解决方法是必要时在最后增加填充字节0.这只是为了检验和的计算（也就是说，可能增加的填充字节不被发送）


