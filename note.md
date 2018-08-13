### py学习碎片

---
* sys.argv[]

sys.argv[] 从外部获取参数，得到一个列表

sys.argv[0] 代码本身文件路径

sys.argv[1] 命令行中输入的第一个参数

sys.argv[2] 命令行中输入的第二个参数

以此类推...

sys.argv[2:] 可以用分片操作来得到所有输入的参数

---
* zip() 函数

用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。

我们可以使用 list() 转换来输出列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

<pre><code>>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]

>>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，*zip 可理解为解压，返回二维矩阵式

>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
>>>
</code></pre>

> Reference：http://www.runoob.com/python3/python3-func-zip.html

---
* sort 与 sorted 区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

> Reference：http://www.runoob.com/python/python3-func-sorted.html
