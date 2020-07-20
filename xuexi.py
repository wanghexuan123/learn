"""本节目标：
1.Python安装: python官网下载 需要注意两点 一：python安装的路径 二：设置环境变量(勾选add python 3.7 to path；手动添加环境变量)
2.安装pycharm 一直默认安装就行 需要记住pycharm安装到什么地方     选择python的安装路径
3.pycharm：菜单栏(file，run)，项目管理模块，系统终端(windows，mac系统命令终端)，python控制台(python指令)
python基础语法：
4.打印：print('')  运行：run 菜单；三角形；命令行(python 文件名.py)
5.# 单行注释 三个引号表示多行注释
6.缩进：tab    input控制台输入
变量命名规则：字母，数字，_组成，不能以数字开头；不能使用python的内置函数；
变量规范：见名知意；下划线连接
本节目标：
标识符：在python里面自己命名的东西就叫标识符
变量定义以后一定要赋值；
字符串数据的左右两边必须加引号；如果字符串内部有双引号/单引号，那么外面就用单引号/双引号表示字符串
如果想要用字符串表示Windows系统下面的路径，在字符串前面添加一个r
数据类型：整型，字符串，浮点型(小数)，布尔类型Boolean(True/False)，列表(列表不等于数组)，元祖，字典
查看数据类型：type(变量名)
字符串拼接：+ ；字符串重复多次：*；判断字符串的长度：len(变量名)；获取数据索引是从0开始；获取多个字符(切片：name【start: end: step:】取头不去尾)
字符串的格式化输出：.format函数
字符串的转化：int(变量名)，str(变量名)
本节目标：
转化成大/小写：.upper();lower()  大小写的转化：.swapcase()
查找：.find()；当查找不到的时候，find会返回-1；当find找到指定的元素时候，返回开始的字母的索引值；必须是连续的字符
index和find的作用类似：找不到报ValueError
替换 .replace() ，字符串一旦定义，除非重新赋值，不然不会发生变化
统计.count()，字符串里面字段出现的次数
字符串拼接，正规方式的+ .join(【】)，
字符串的分割.split()
*去掉左右两边的指定字符串.strip()；如果左右两边不一样.lstrip(),.rstrip()
*判断是否是一个正整数.isdigit()
列表：存储很多数据；变量：存储数据
列表里面可以存储不同的数据类型的数据
如果想取出其中的某个元素，通过索引获取某个元素，和字符串类似/获取多个用切片/如果子元素当中是列表，继续通过索引获取，切片也可以
字符串不能修改；列表可以修改，可变数据类型，列表长.len()
添加新的元素：.append()；添加多个.extend()
往指定位置添加.insert(索引位置，添加的内容)  一次添加一个
删除：.remove(删除指定的值) ；删除指定的索引，弹出(有返回值) .pop()，没有参数，索引，默认就是删除最后一个；删除所有的元素.clear()；不要去用 del(从内存当中直接清除)
逆序：.reverse()   *排序：.sort() 数字排序，字母排序 """
