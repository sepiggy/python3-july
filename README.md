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
    
4. 全局变量与局部变量
    - `global` 关键字可以在函数体中声明一个全局变量
    
    - `nonlocal` 关键字可以在函数体中强制声明一个变量不是本地局部变量
    
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
1. 函数的特点
    - 功能性
    - 隐藏细节
    - 避免编写重复的代码
    
2. 函数的定义
    - 定义一个函数需要指明 `函数名` `参数列表` `返回值`
        ```python
          def 函数名(参数列表):
              return 返回值
        ```
    - 说明
        - 函数名的定义规则与变量名相同
        
        
3. 函数的返回值
    - 函数的定义中不用且不能指明函数返回值的类型, 因为 Python 是动态语言
    
    - 在函数体中, 可以使用 `return` 语句返回函数结果; 若没有 `return` 语句则函数的返回值为 `None`
    
    - 在函数体中, 单独的 `return` 关键字出现在函数中, 表示函数终止, 且 `return` 后的语句不会执行
    
    - 函数可以返回任意类型的值, eg. int, str, list, tuple and function etc.
    
    - 函数可以返回任意数量的值, eg. return r1, r2; 多返回值的函数默认返回一个 `tuple`, 不用强制加`()`
    
    - 序列解包与链式赋值
        - a,b,c = 1,2,3
        - 序列解包可以用在函数多返回值的处理上
            ```python
              def func(x1, x2):
                  return x1 + x2, x1 - x2
        
              result1, result2 = func(1, 2)
            ```
4. 函数的参数
    - 参数列表中不用且不能指明变量类型, 这不同于编译型语言
    
    - 参数列表可以为空, 即该函数不需要参数
    
    - 有关参数的几个概念
        - 形式参数
        
        - 实际参数
        
        - 必须参数
            - 默认函数定义中的参数都必须提供实参, 否则抛出异常
        
        - 关键字参数
            - 关键字参数是函数调用时的概念
            
            - 使用关键字参数进行函数调用时可以不用考虑函数定义时的参数顺序
            
            - 在函数调用时可以明确指定调用的是哪个形参
                ```python
                   def add(x,y):
                      return x+y;
        
                   c = add(y=3,x=2)
                ```
                
            - 关键字参数提高了代码的可读性
            
        - 默认参数
            - 默认参数是函数定义时的概念
            
            - 在函数定义时可以为形参提供一个默认值, 使函数在调用时, 若不提供实参, 则用该形参的默认值
                ```python
                def print_student_files(name, gender='男', age=18, college='人民路小学'):
                    print('我叫' + name)
                    print('我今年' + str(age) + '岁')
                    print('我是' + gender + '生')
                    print('我在' + college + '上学')
                ```
                
            - 在函数定义时若没有为函数形参提供默认值, 则其为必须参数, 即在函数调用时必须为其提供实参, 否则抛出异常
            
            - 函数定义的参数列表中, 默认参数应在必须参数之后, 否则抛出异常
            
            - 在函数调用时, 若要改变默认参数的默认值, 最好配合关键字参数指明要更改的参数
                ```python
                  print_student_files('果果', age=17)
                ```
                
        - 可变参数
            - 可变参数是函数定义时的概念
            
            - 函数定义时, 在变量名之前加 `*` , 则这个参数就是可变参数
                ```python
                  def demo(*param):
                      pass
                ```
            
            - 可变参数的类型实质是 `tuple`, 因此可以向拥有可变参数的函数传递任意数量, 任意类型的参数
            
            - 若在函数调用时向可变参数的函数传入的不是多个参数, 而是 `tuple` 或 `list`, 则需要在实参前加 `*`
                ```python
                  demo(*(1,2,3,4,5))
                ```
            - 在函数体中, 可以使用 `for-each` 遍历代表可变参数的 `tuple`
                
            - 在函数定义时, 可变参数应在必须参数之后和默认参数之前
            
            - 在函数调用时, 若参数列表既有可变参数, 又有默认参数, 则必须使用关键字参数进行显示调用, 否则有歧义
            
            - 可变参数列表的实参可以为空
            
        -  关键字可变参数
            - 关键字可变参数是函数定义时的概念
            
            - 函数定义时, 在参数名之前加 `**` , 则这个参数就是关键字可变参数
                ```python
                  def demo(**param):
                      pass    
                ```
                
            - 关键字可变参数的类型实质是 `dict`, 因此可以向拥有关键字可变参数的函数传递多个 `key:value`
            
            - 若在函数调用时向关键字可变参数的函数传入的不是多个 `key:value`, 而是 `dict`, 则需要在实参前加 `**`
            
            - 在函数体中, 可以使用 `for-each` 遍历代表关键字可变参数的 `dict`
                ```python
                  def city_temp(**param):
                      for key, value in param.items():
                          print(key, ':', value)
                ```
                
            - 关键字可变参数列表的实参可以为空
            
    - 变量的作用域
        - 在整个应用程序中都能引用的变量, 称为 `全局变量`
        
        - 在某个函数体内都能引用的变量, 称为 `局部变量`
        
        - `global` 关键字可以使函数中的 `局部变量` 转换为 `全局变量`
        
        - Python 中只有 `全局作用域` 和 `函数作用域`, 没有 `块级作用域`
        
        - `在 for 循环的外部可以引用 for 循环内部的变量`, 因为在 Python 中*没有* `块级作用域`
        
        - 作用域具有链式特性, 称为`作用域链`
        
## 七 面向对象
1. 类的定义
    - 类的定义
        - `类是现实世界或思维世界中的实体在计算机中的反映`
        
        - `类将数据以及这些数据上的操作封装在一起`
        
        - `数据` 对应 `数据成员`; `操作` 对应 `方法`
        
    - 类的基本作用
        - `封装`: `变量` 和 `函数` 被封装在 `类` 中
        
    - 类的定义语法
        - 使用关键字 `class` 来定义类
        
        - 类名推荐使用 `驼峰命名法`, 同 `Java`
        
        - 在类中可以定义 `变量` 和 `函数`
            ```python
            class Student():
               name = ''
               age = 0
            
               def print_file(self):
                   pass
            ```
        
    - 方法和函数的区别
        - 类中定义的函数通常称为 `方法`
        
        - `方法`是`设计层面`的称谓; 而`函数`是`程序运行, 过程式`的一种称谓
        
        - 实例方法的参数列表的第一个参数必须是 `self`
        
    - 数据成员和变量的区别
        - 类中定义的变量通常称为 `数据成员`
        
        - `数据成员`是`设计层面`的称谓; 而`变量`是`程序运行, 过程式`的一种称谓
        
2. 类与对象
    - 类是实体的`模板`, 对象是具体的实体
    
    - 类使用 `构造函数` 来对自己进行实例化
    
    - 构造函数
        - 构造函数用来初始化类的特征
        
        - 每个类的构造函数, 强制命名为 `__init__`
        
        - 构造函数里不能显示地 `return` 除了 `None` 之外的类型
        
        - 利用构造函数可以初始化对象的属性
    
    - 类的`定义`, `实例化` 和 `调用` 应该分别写在两个不同的`模块`中
    
3. 类变量, 实例变量
    - 类变量
        - 与类相关联的变量
        - 定义在类的开头处
        - 类变量只能被类方法访问
        - 类变量可以使用 `类名.类变量名` 或 `对象名.__class__.类变量名` 访问
    
    - 实例变量
        - 与对象实例相关联的变量
        - 使用 `self` 和 `.` 运算符可以定义实例变量
        - 实例变量可以被实例方法, 类方法和静态方法访问
        - 实例变量只可以使用 `实例变量.实例变量名` 访问
        
    - `a.b` 的变量查找顺序
        - 先从 a 的实例变量里查找变量名为 b 的变量
        
        - 若没找到, 再从 a 的类变量里查找名为 b 的变量
        
        - 若还没找到, 会从 a 所在类的父类里查找名为 b 的变量
        
    - 例子
        ```python
        class Student():
          # 这里定义了两个类变量 
          name = 'qiyue'
          age = 0
   
          def __init__(self, name, age):
              # 这里定义了两个实例变量
              self.name=name
              self.age=age
        
          def do_something(self):
              pass
        ```
        
4. 类方法与实例方法以及静态方法
    - 类方法
        - 与类相关联的方法, 其参数代表类 (cls)
        
        - 使用装饰器 @classmethod 标注在一个实例方法上, 这个方法就变为类方法, 这里的 `cls` 代表调用类方法的类
            ```python
            @classmethod
            def plus_sum(cls):
              pass
            ```
        - 在类方法内部可以访问类变量, 不能访问实例变量
            
        - 通过类和对象都可以调用类方法
    
    - 实例方法
        - 与对象实例相关联的方法, 其参数代表实例 (self)
        
        - 实例方法参数列表的第一个参数必须是代表调用该方法的对象, Python 推荐使用 `self` 代表这个变量
            ```python
            def do_homework(self):
              pass
            ```
        
        - 构造函数是特殊的实例方法
        
        - 在实例方法内部访问实例变量与类变量
            - 在实例方法内部访问实例变量, 使用 `self.实例变量名` 进行访问, 而不能直接使用 `实例变量名` 访问, 否则会出现访问到实例方法形参的情况
            
            - 通过 `类名.类变量名` 或 `self.__class__.类变量名` 可以访问类变量
            
        - 只能通过对象调用实例方法
        
    - 静态方法
        - 通过装饰器 `@staticmethod` 修饰的实例方法
            ```python
            @staticmethod
            def add(x,y):
              pass
            ```
            
        - 静态方法参数列表的第一个参数不必强制指定, 这一点与实例方法和类方法都不同
        
        - 在静态方法的内部可以访问类变量, 不能访问实例变量
        
        - 静态方法可以通过 `类名.方法名` 和 `对象名.方法名` 的方式被调用
        
5. 成员的可见性
    - public
        - 变量名和方法名不以 `__` 开头
        
    - private
        - 变量名和方法名只以 `__` 开头
        
        - 若变量名和方法名以 `__` 开头和结尾, 则认为其成员可见性为 `public` 而不是 `private`, 比如 `构造函数`
        
        - Python 中的 `private` 机制是通过改名实现的, 它将私有变量改名为 `_类名__变量名` 的形式, 例如 `_Student__score`, 这样通过 `实例.变量名` 的形式就读不到这个变量了
        
6. 继承
    - 面向对象的三大特性
        - 封装性
        - 继承性
        - 多态性
        
    - 继承的作用
        - 避免重复定义方法和变量
        - 模拟现实世界
        
    - Python 通过在定义类时把父类写在 `()` 里, 来实现继承语法; 同时, Python 支持 `多继承`
        ```python
        # Student 类继承自 People 类
        class Student(People):
          pass
        ```
        
    - 子类构造函数调用父类构造函数 (不推荐使用, 使用 super 代替!)
        ```python
        class Student(Human):
              def __init__(self, school, name, age):
                  self.school = school
                  # 通过类名调用实例方法 (特例), 因此 Python 不知道调用这个构造函数的是哪个实例 
                  # 所以, 这里需要给 Python 提供这个对象, 即通过 `self` 参数
                  Human.__init__(self, name, age)
        ```
    
    - 子类方法调用父类方法
        - 使用 `super` 关键字可以调用父类方法, 不限于构造函数
            ```python
            def __init__(self, name, age, school):
                # Human.__init__(self, name, age)
                self.school = school
                super(Student, self).__init__(name, age)
            ```
            
## 八 正则表达式与JSON
### 1. 正则表达式
1. 初始
    - 定义
        - 特殊的字符序列, 用来检测一个`字符`是否与我们设定的字符序列相匹配
        
    - 作用
        - 检索文本
        - 替换文本
    
    - 正则表达式的关键是 `规则`
    
2. 普通字符与元字符
    - 普通字符 
        - 普通字符通常起到 `定界` 的作用
        - 一个例子, `a[\d]c`, 其中 a 和 c 是普通字符, 起到定界作用
        
    - 元字符 
        - 字符集
            - `[abc]`:  匹配 a, b 或 c
            - `^[abc]`: 匹配不是 a, b 或 c
            - `[a-e]`:  匹配 a, b, c, d 或 e
            
        - 概括字符集
            - 定义: 概括一类字符的元字符
            
            - 常见的概况字符集
                - `\d`: 匹配数字, 等价于 `[0-9]`
                - `\D`: 匹配非数字, 等价于 `[^0-9]`
                - `\w`: 匹配数字, 字母或下划线, 等价于 `[0-9A-Za-z_]`
                - `\W`: 匹配非数字, 字母或下划线, 等价于 `[^0-9A-Za-z_]`
                - `\s`: 匹配空白字符
                - `\S`: 匹配非空白字符
                - `.`: 匹配除 `\n` 之外的其他所有字符
                
        - 数量词
            - 作用: 借助于 `数量词`, 正则表达式可以匹配多个字符
            
            - 形式
                - `字符{min, max}`, 匹配最少 `min` 个字符, 最多 `max` 个字符
                    - 贪婪
                        - 规则: 尽可能多地匹配字符, 直到超出 `max`, 或某个字符不满足匹配条件
                        - 表示: `字符{min, max}` [**默认**]
                        
                    - 非贪婪
                        - 规则: 尽可能少地匹配字符, 从 `min` 开始匹配, 直到获得一个成功的匹配就结束
                        - 表示: `字符{min, max}?`
                        
                - `字符*`, 匹配 `0个或无限多个` 字符
                - `字符+`, 匹配 `1个或无限多个` 字符
                - `字符?`, 匹配 `0个或1个` 字符
                
3. 边界匹配
    - 形式: `^字符$`, 匹配完整字符串
        - `^` 表示从字符串开始处匹配
        - `$` 表示从字符串结尾处匹配
        
4. 组
    - 形式: 多个字符用 `()` 包裹起来当作一个字符进行匹配
    
5. `re` 模块`
    - re.findall() [**常用**]
    
    - re.sub() [**常用**]
    
    - re.search()
        - group() 分组
    
    - re.match()
        - group() 分组

### 2. JSON
1. JSON 的几个相关概念
    - 定义: JavaScript Object Notation
    
    - 本质: JSON 是一种轻量级的数据 `交换格式` (JSON 作为中间数据类型的格式可以起到桥梁作用, 用来联结两种不同语言的数据类型格式, 以达到交换数据的目的)
    
    - 表现形式(载体): 字符串是 JSON 的表现形式 (载体)
    
    - JSON 字符串
        - 符合 JSON 格式的字符串叫做 JSON 字符串
            ```python
            '{"name": "qiyue"}'
            ```
            
        - JSON 规范约定, JSON 字符串里的 key 都要加`双引号`; 而 value 的值若是字符串也要加`双引号`, 若是数字和布尔类型不加`双引号`
        
        - 常见 JSON 字符串的形式
            - 使用 JSON 字符串表示单个 JSON 对象, eg. `{"name":"qiyue", "age":18}`
            - 使用 JSON 字符串表示多个 JSON 对象, 即 JSON 对象数组, eg. `[{"name":"qiyue", "age":18, "flag":false}, {"name":"bayue", "age":20}]`
            
    - `JSON`, `JSON对象`, `JSON字符串` 三个概念比较
        - `JSON` 是一种数据交换格式, 是一种规范
        - `JSON对象` 是指 JSON 的数据类型中的对象 (JSON 有自己的数据类型, 虽然它和 Javascript 的数据类型有些相似)
        - `JSON字符串` 是指 JSON 的表现形式
        
2. JSON 的优点
    - 易于阅读
    - 易于解析
    - 网络传输效率高
    - **适合跨语言交换数据** (以不同语言写的程序作为一个服务, 服务与服务之间使用 JSON 交换数据)
    
3. JSON 常见应用场景
    - 浏览器通过 AJAX 请求网站后台, 其返回 JSON 格式的数据, 然后将其中的数据通过 HTML 展现出来
    - 不同语言的 API 服务通过 JSON 交换数据
    
4. 序列化与反序列化
    - JSON 数据类型与 Python 数据类型的对照
    
        JSON   | Python
        :----: | :----:
        object | dict
        array  | list
        string | str
        number | int
        number | float
        true   | True
        false  | False
        null   | None
        
    - 序列化
        - 某种语言特定类型 --> 字符串    
        - 通过 `json.dumps(Python数据类型)` 函数可以将一个 Python 类型转换为 JSON 字符串
            - 对于 Python 中的 `dict`, `list` 等类型都将转换为 JSON 字符串
        
    - 反序列化
        - 字符串 --> 某种语言特定类型
        - 通过 `json.loads(JSON字符串)` 函数可以将一个 JSON 字符串转换为 Python 对应的类型
            - 对于单个 JSON 对象字符串, 将转换为 Python 中的 `dict` 类型
            - 对于多个 JSON 对象字符串, 即 JSON 对象数组字符串, 将转换为 Python 中的 `list`, 其中每个元素又是一个 `dict`
            
## 九 Python 的高级语法
### 1. 枚举
1. 为何引入枚举?
    - 现实世界中 `类型` 的概念在 Python 中使用 `枚举` 这种机制来描述
    
2. Python 中的 `枚举` 机制是通过继承 `enum.Enum` 类来实现的
    ```python
    class VIP(Enum):
        # 大写表示常量
        YELLOW = 1
        GREEN = 2
        BLACK = 3
        RED = 4
    ```
    
3. 继承 `enum.Enum` 类实现枚举的优势
    - 数据不可变
    - 可以防止枚举标签相同
    
4. 枚举操作
    - 获取枚举类型, eg. `VIP.YELLOW`
    - 获取枚举标签名, eg. `VIP.YELLOW.name`
    - 获取枚举值, eg. `VIP.YELLOW.value` 或 `VIP['YELLOW']`
    - 遍历枚举类型, eg.
        ```python
        for v in VIP:
          print(v)
        ```
    - 比较运算
        - 枚举类型只能跟枚举类型进行比较运算; 不能跟其他类型进行比较运算
        - 枚举类型之间只能通过 `==` 进行 `等值` 比较; 不能通过 `>` 和 `<` 进行 `大小` 比较
    - 身份运算
        - 枚举类型可以使用 `is` 运算符进行身份运算
    - 类型转换
        - 通过枚举类型的构造函数可以将其他类型转换为对应数值的枚举类型, eg. `VIP(1)` 可以转换为 `VIP.YELLOW`
        
5. Python 中的枚举类型是单例模式, 不能够对其实例化
        
### 2. 闭包
1. 函数是对象
    - Python 中一切皆对象, `函数也是对象`
    - Python 中, `函数可以赋值给一个变量`
    - Python 中, `函数可以作为另一个函数的参数`
    - Python 中, `函数可以作为另一个函数的返回结果`
    
2. 闭包定义
    - `闭包 = 函数 + 环境变量 (函数定义时候)`
        ```python
        def curve_pre():
            a = 25
            def curve(x):
                return a * x * x
            # 下面的返回值, 不仅返回了函数, 还返回了环境变量 (实际返回一个闭包)
            return curve
        ```
        
    - Python 中, 闭包可以通过 `函数名.__closure__` 来获取
    
    - Python 中, 闭包的环境变量可以通过 `函数名.__closure__[0].cell_contents` 来获取

3. 闭包的实质: `保存函数调用时的现场`

### 3. 函数式编程
1. 匿名函数
    - 匿名函数的定义
        - 使用 `lambda` 关键字定义匿名函数
        - 匿名函数没有函数名和 `return` 语句
        - 格式: `lambda parameter_list: expression`, 这里只能是 expression (表达式), 不能是语句, 更不能是代码块
        ```python
        lambda x,y: x + y
        ```
        
    - 匿名函数的调用
        - 将匿名函数赋值给一个变量, 通过变量进行调用
        ```python
        f = lambda x,y: x+y
        f(1,2)
        ```
        
    - 三元表达式
        - `x if x > y else y`, 这是 Python 中的三元表达式, 类比于其他语言的 `x > y ? x : y`
        - 因为 Python 中的匿名函数只能使用表达式, 因此三元表达式用在 Python 匿名函数的情况比较多
        
2. 高阶函数
    - map
        - map 是一个类
        - 通过 map 的构造函数可以创建集合的一个映射, 其中的映射规则由我们定义的函数来实现
        - map 的映射规则多由匿名函数来定义, 即 map 多与 lambda 表达式结合使用
        
    -  reduce
        - reduce 是一个函数
        - 连续计算, 连续调用 lambda 表达式
        - 上一次 lambda 表达式的计算结果参与到下一次的 lambda 表达式的计算
        
    - filter
        - filter 是一个类

### 4. 装饰器
1. 装饰器的几个关键点
    - 装饰器是一种 `设计模式`: `在不改变函数具体实现的前提下, 改变函数的行为` 
    - 装饰器体现了软件工程中的 `开闭原则`
    - 装饰器体现了 `代码复用` 的原则
    - 装饰器体现的思想是 `AOP`
    - 装饰器的表现形式是 `函数`

2. 装饰器的定义 (装饰器就是一个函数, 其定义方式与函数的定义是相同的)
    - 装饰器的定义类比与函数的定义, 因为装饰器本身就是函数
        ```python
        def decorator(func):
            def wrapper():
                print(time.time())
                func()

            return wrapper
        ```
    
    - 通过 `可变参数` 定义装饰器, 以实现一个装饰器可以装饰多个函数, 且这些函数的参数个数不相同
        ```python
        def decorator(func):
           def wrapper(*args):
               print(time.time())
               func(*args)

           return wrapper
        ```
    
    - 通过 `可变参数` 和 `关键字可变参数` 定义装饰器, 以实现一个装饰器可以装饰多个函数, 且这些函数的参数列表是任意形式
        ```python
        def decorator(func):
            def wrapper(*args, **kw):
                  print(time.time())
                  func(*args, **kw)
            
            return wrapper
        ```
        
    - 在 Python 中 `func(*args, **kw)` 的形式可以代表任意参数类型的函数
    
    - 一个装饰器可以用在多个函数上; 一个函数也可以添加多个装饰器

3. 装饰器的使用
    - 通过语法糖 `@装饰器` 调用装饰器, 这样可以不用改变原来函数的调用方式
     ```python
     @decorator
     def f1():
       print('This is a function')
    ```
    
### 5. 未归类

## 十 爬虫实战
1. 爬虫前奏
    - 明确目的
    - 找到数据对应的网页
    - 分析网页的结构找到数据所在的标签位置
    
2. 爬虫步骤
    - 模拟 HTTP 请求, 向服务器发送这个请求, 获取到服务器返回给我们的 HTML
    - 用正则表达式提取我们要的数据 (名字, 人气)
    
    


            
        
            

