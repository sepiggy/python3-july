## 一 基本类型
### 1. Number
1. int
    - 10, 2, 8, 16 进制表示法
        - 10 (十进制)
        - 0b10 (二进制)
        - 0o10 (八进制)
        - 0x10 (十六进制)
    - 进制转换
        - int() (转换为十进制)
        - bin() (转换为二进制)
        - oct() (转换为八进制)
        - hex() (转换为十六禁止)
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
 
### 2. String
1. 三种字符串表示法
    - 单引号 (单双引号表示字符时串需要成对出现)
    - 双引号
    - 三引号 (多行字符串)
    ```python
    "let 's go"
    'let "s go'
    ```
    
2. 转义字符
    - 无法 "看见" 的字符 `\n`
    - 与语言本身语法有冲突的字符 `\'`
    
3. 原始字符串 (所见即所得)
    ```python
    print(r"c:\northwind\northwest")
    ```
4. 字符串运算
    - 字符串拼接 `"hello" + "world"`
    - 字符串复制 `"hello" * 3`
    - 字符串截取
        - 截取单个字符 `"hello world"[3]`, `"hello world"[-1]`
        - 截取多个字符 (不包括终点) `"hello world"[2:-2]`

     
        
        
           
    