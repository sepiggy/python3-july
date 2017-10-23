## 一 基本类型
### 1. 数字 (4种)
1. int
    - 10, 2, 8, 16 进制表示法
        - `10` (十进制)
        - `0b10` (二进制)
        - `0o10` (八进制)
        - `0x10` (十六进制)
    - 进制转换
        - `int()` (转换为十进制)
        - `bin()` (转换为二进制)
        - `oct()` (转换为八进制)
        - `hex()` (转换为十六禁止)
2. float
    - `1/2` vs `1//2`
3. bool
    - 取值为 `True` vs `False` (首字母大写)
    - int(True) vs int(False) 
    - bool(1) vs bool(0)
    - 非 0 表示 True; 0 表示 False
    - bool(0b11), bool(0x1A)
    - bool('abc') vs bool(")
    - bool([1 ,2, 3]) vs bool([])
    - 非空表示 True; 空表示 False
    - bool(None)
4. complex
 
### 2. 序列 (3种)
1. str (字符串)
    - 三种字符串表示法
        - 单引号 (单双引号表示字符时串需要成对出现)
        - 双引号
        - 三引号 (多行字符串)
        ```python
        "let 's go"
        'let "s go'
        ```
    
    - 转义字符
        - 无法 "看见" 的字符 `\n`
        - 与语言本身语法有冲突的字符 `\'`
    
    - 原始字符串 (所见即所得)
        ```python
        print(r"c:\northwind\northwest")
        ```
        
    - 字符串运算
        - 字符串拼接 `"hello" + "world"`
        - 字符串复制 `"hello" * 3`
        - 字符串截取
            - 截取单个字符 `"hello world"[3]`, `"hello world"[-1]`
            - 截取多个字符 (不包括终点) `"hello world"[2:-2]`
        
2. list (列表)
    - list 的元素类型可以是任意元素, 列表本身也可以嵌套列表, 且可以混用
        ```python
        ["hello", 123, True]
        [["I", "Me"], [True, False, 1234]]
        ```
    - list 的基本操作
        - 列表的截取 (类比字符串)
            ```python
            ["Java", "Python", "Ruby", "CSS"][2]
            ["Java", "Python", "Ruby", "CSS"][1:-1]
            ```
        - 列表的拼接 (类比字符串)
            ```python
            ["Java", "Python"] + ["Ruby", "CSS"]
            ```
            
        - 列表的重复 (类比字符串)
            ```python
            ['Java'] * 4
            ```
            
3. tuple (元组)
    - tuple 的元素类型可以是任意元素, 包括元组类型本身, 且可以混用
        ```python
        (1,2,3,4,5)
        (1, "-1", True)
        (1, )
        ()
        ```
        
    - tuple 的基本操作
        - 元组的截取 (类比字符串)
        ```python
        (1,2,3,4)[0]
        (1,2,3,4)[0:2]
        ```
    
        - 元组的拼接 (类比字符串)
        ```python
        (1,2,3) + (4,5,6)
        ```
        
        - 元组的重复 (类比字符串)
        ```python
        (1,2,3) * 3
        ```
        
4.  序列小结
    - 序列的每个元素都有相应的序号
    
    - str, list, tuple 都是序列
    
    - 序列操作小结
        - 序列的截取操作称为`切片`
        
        - 序列都可以通过 `+` 进行拼接; 通过 `*` 进行重复
        
        - 判断某个元素是否在序列中
        ```python
        3 in [1,2,3,4,5,6]
        3 not in [1,2,3,4,5,6]
        ```
        
        - 获取序列长度, 即序列中的元素个数
        ```python
        len("hello world")
        ```
        
        - 获取序列中的最大值, 最小值
        ```python
        max('hello world')
        min([1,2,3,4,5,6])
        ```

### 3. 非序列 (2种)
1. 集合
    - 集合的表示, 集合中可以包含任意类型的元素, 且可以混用

        ```python
        {1,2,3,4,5}
        set() (空集)
        ```
    
    - 集合的两大特性
        - 无序
        - 不重复
    
    - 集合的操作
        - 获取集合长度, 即集合中的元素个数
        ```python
        len({1,2,3})
        ```
        
        - 判断某个元素是否在集合中
        ```python
        1 in {1,2,3}
        4 not in {1,2,3}
        ```
        
        - 求两个集合的差集
        ```python
        {1,2,3,4,5,6} - {3,4}
        ```
        
        - 求两个集合的交集
        ```python
        {1,2,3,4,5,6} & {3,4}
        ```
        
        - 求两个集合的并集
        ```python
        {1,2,3,4,5,6} | {3,4,7}
        ```

2. 字典 (dict)
    - 字典的表示, 其中 key 不能重复且是不可变类型; value 的值可以是任意类型, 包括 dict 本身
        ```python
        dict qop = {'D': '暗影突袭', 'B': '闪烁', 'F': '尖叫', 'W': '冲击波'}
        {}  (空的字典)
        ```
        
    - 字典的操作
        - 通过 key 得到 value
        ```python
        {'D': '暗影突袭', 'B': '闪烁', 'F': '尖叫', 'W': '冲击波'}['D']
        ```
        
## 二 变量 
1. 什么是变量?
    - 变量是名字
    
    - 定义变量 `=`
    
2. 变量的命名规则
    - 只能由字母, 数字, 下划线组成, 并且首位不能是数字
    
    - 保留字不能用作变量名    eg. `and`, `if`
    
    - 系统常用关键字不能用作变量名    eg. `type`
    
    - 变量名区分大小写
    
    - 变量类型不固定 (动态语言)
    
3. 值类型与引用类型
    - 值类型是不可变的, 引用类型是可变的
    
    - int float bool complex str tuple 是值类型, 不可变
    
    - list set dict 是引用类型, 可变
    
## 三 运算符
1. 算数运算符
    - 操作数: 不限于数字类型
    
    - 结果: 与操作数同类型
    
    - `+` `-` `*` `**` `/` `//` `%`
    
    - 例子
        ```python
        'hello' + ' world'
        [1,2,3] * 3
        {1,2,3} - {1}
        ```
        
2. 赋值运算符
    - 为变量赋值
    
    - 操作数: 任意类型
    
    - 结果: 与操作数同类型
    
    - `=` `+=` `*=` `/=` `%=` `**=` `//=`
    
3. 比较(关系)运算符
    - 比较两个类型变量的关系
    
    - 操作数: 任意类型
    
    - 结果: bool 类型
    
    - `==` `!=` `>` `<` `>=` `<=`
    
    ```python
    [1,2,3] < [2,3,4]
    (1,2,3) < (1,3,2)
    "hello" >= "world"
    ```

4. 逻辑运算符
    - 操作数: bool 类型
    
    - 结果: bool 类型
    
    - `and`, `or`, `not`
    
    - int, float 类型数值参与逻辑运算时, `0 被转换为 False, 非 0 被转换为 True`
    
    - str 类型数值参与逻辑运算时, `空字符串被转换为 False, 非空字符串被转换为 True`
    
    - list 类型数值参与逻辑运算时, `空的列表被转换为 False, 非空列表被转换为 True`
    
    - tuple, set, dict 类型数值与上同理
    
    - 当 `and`, `or` 运算符的操作数是非 bool 类型时, 其结果相应的根据上述规则被转换为操作数对应的类型
        ```python
        [1] or []      # [1]
        [] and [1]     # []
        # 短路规则的应用:
        1 and 2        # 2
        2 and 1        # 1
        1 or 2         # 1
        2 or 1         # 2
        ```
    
5. 成员运算符
    - 判断一个元素是否在一组元素里
    
    - `in` `not int`
    
    - 操作数: 任意类型
    
    - 结果: bool 类型
    
    - 例子
        ```python
        1 in [1,2,3,4,5]
        'H' not in 'Hello world'
        [1,2] in [[1,2], 3, [4,5,6]]
        1 in {4,5,6}
        # dict 的成员运算判断的是 key
        'a' in {'c':1}        # False
        1 in {'c':1}          # False
        'c' in {'c':1}        # True
        ```
        
6. 身份运算符
    - 操作数: 任意类型
    
    - 结果: bool 类型
    
    - `==` 比较的是两个变量的值是否相等, `is` 比较的是两个变量在内存中的地址是否相等
        ```python
        a = 1
        b = 1.0
        a == b        # True
        a is b        # False
        a not is b    # True
  
        a = {1,2,3}
        b = {2,1,3}
        a == b        # True
        a is b        # False
  
        c = (1,2,3)
        d = (2,1,3)
        c == d        # False
        c is d        # False
        ```
        
    - 对象的三个特征
        - 值 (value)
            - `=` 操作符可以为变量赋值
            - `==` 操作符可以判断两个变量的值是否相等
        
        - 身份 (id)
            - `id()` 函数可以返回变量的内存地址
            - `is` 操作符可以判断两个变量的内存地址是否相等
    
        - 类型 (type)
            - `type()` 函数可以返回变量的类型
            - `isinstance()` 函数可以判断某个变量是否是某个类型

7. 位运算符
    - 操作数: 二进制的 int 类型

    - 结果: 二进制的 int 类型

    - `&(按位与)` `|(按位或)` `^(按位异或)` `~(按位取反)` `<<(左移)` `>>(右移)`

    - 其它进制的 int 类型的操作数使用位运算符时, 会被转换为二进制, 同时其结果返回操作数的进制
        ```python
        2 & 3     # 2
        2 | 3     # 3
        2 ^ 3     # 1
        ```
    
## 四 流程控制
1. 表达式
    - 表达式 (Expression) 是运算符 (Operator) 和操作数 (Operand) 所构成的序列
        ```python
        1 + 2 * 3         # 这是一个表达式
        a = 1 + 2 * 3     # 这同样也是一个表达式, = 要当成赋值运算符
        c = a and b or c  # 这是一个表达式
        c = int('1') + 2  # 表达式可以包括函数调用, 函数调用 () 也是属于运算符
        ```
        
    - 表达式的优先级
        - `=` 运算符是右结合; 其它运算符都是左结合
        
        - `()` 可以打破算数运算符默认的优先级
        
        - 优先级: `not` > `and` > `or`
        
2. 分支
    - 解决选择性问题
    
    - 格式
        - if 可以单独使用, 但是 else 必须和 if 配对使用
            ```python
            if bool类型的变量或表达式:
                  代码块
        
            if bool类型的变量或表达式:
                  代码块
            else:
                  代码块
            ```
            
        - if-else 里面还可以嵌套 if-else 代码块
        
        - elif = else + if
            
    - 常量
        - python 中没有常量的概念, 其本质还是变量, python 没有机制保证其值不会变
        
        - 常量名一般用全大写英文字母表示

3. 循环
    - while
        - 用途: 递归算法
        
        - 格式
            ```python
            while bool类型的变量或表达式:
                  代码块
            else:
                  代码块
            ```
        
        - 避免"非刻意的" while 死循环
            - while 后面不要使用常量做判断, 因为常量是永远不会改变的, 除非你真的需要一个死循环
            
            - while 后面使用变量做判断, 且 while 内部的代码块中存在影响条件判断的语句, 可以避免 while 死循环
            
        - python 中的 while 可以和 else 一起使用, 类似于 if-else
    
    - for
        - 用途
            - 遍历序列, 集合和字典
            - 重复执行确定次数的代码块
        
        - 格式
            ```python
            # 遍历序列, 集合和字典
            for target_list in expression_list:
                  代码块
            else:
                  代码块
            
            # 重复执行 times 次数的代码块
            for i in range(times):
                  代码块
            ```
        
        - python 中的 for 可以和 else 一起使用, 当 for 遍历完所有的元素之后, else 中的代码块就会被执行
        
    - break 和 continue 的用法类比于 Java
        - break 不会执行 for-else 中的 else 子语句, 而 continue 则会执行 for-else 中的 else 子语句
        
## 五 包 模块 
1. python 项目的组织结构
    - 包 (表现形式: 文件夹)
    - 模块 (表现形式: 文件)
    - 类
    - 函数, 变量
    
2. 包
    - 包含 `__init__.py` 的文件夹称为 `包`
        
    - `__init__.py` 本身也是一个模块
        - 当一个包被导入时, 其 `__init__.py` 首先被自动执行
            
        - `__init__.py` 模块的 `__all__` 变量可以决定该包下的哪些模块可以被导入
            
        - `__init__.py` 模块中添加 `import` 语句导入一些模块, 则可实现批量导入模块的功能
            
    - 包和模块是不会被重复导入的
        
    - 避免包和模块的循环导入
    
3. 模块
    - 模块分类
        - 入口模块
        - 普通模块
            - 普通模块必须存在一个包中
            
    - 当导入另一个模块时, 就会执行其模块中的代码, 其代码会且只会执行一次
        - 在一个模块中, 可以使用 `import` 关键字导入另一个`包, 模块`
        - 在一个模块中, 可以使用 `from ... import ...` 关键字导入另一个模块中的`模块, 变量或函数`
        - 例子
            ```python
            import t.c7
            print(t.c7.a)

            from t.c7 import a
            print(a)

            from t import c7
            print(c7.a)

            from t.c7 import *
            print(a)
            print(d)
            print(c)
            ```
        
    - 模块的内置变量
        - dir() 函数
            - dir() 可以返回一个 list, 其表示模块中所有变量的名字, 包括模块的内置变量和我们自己定义的变量
            - dir(module_name) 返回指定模块的变量名 list
        
        - 以 `__` 开头和结尾的变量名所代表的变量是 Python 模块的内置变量 `__doc__` `__file__`
        
        - 常用的模块内置变量
            - __name__
                - 如果一个模块作为普通模块, 其 `__name__` 变量的值为其模块名
                - 如果一个模块作为入口模块, 其 `__name__` 变量的值为 `__main__`
                - `__name__` 的经典应用: `Make a script both importable and executable`
                    ```python
                      if __name__ == '__main__':
                          pass
                    ```
                
            - __package__
                - 如果一个模块作为普通模块, 其 `__package__` 变量的值为其包名
                - 如果一个模块作为入口模块, 其 `__package__` 变量的值为 `None`
                
            - __doc__ 
                - 模块的文档说明
                
            - __file__
                - 其取值与执行 python 命令的所在目录是有关系的
                
## 六 函数

            
        
    
    





        
    
    
        

     
        
        
           
    