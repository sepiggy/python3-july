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
    