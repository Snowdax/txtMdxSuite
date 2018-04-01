# txtMdxSuite
# 纯文本 mdx 套件


### 输入文件要求：复制双列 Word 或 Excel 表格（左列为词头，右列为释义）至文本编辑器，存为 txt 文本文件（即 TAB 连接的纯文本表格）。请查看示例文件 [水果.txt](https://raw.githubusercontent.com/Snowdax/txtMdxSuite/master/水果.txt)

### tab2mdx
功能：将双列表格转为 MdxBuilder 可用格式  
输出：可用于 MdxBuilder 的文件。文件名为：原文件名_forMdxBuilder.txt  
[输出文件示例](https://raw.githubusercontent.com/Snowdax/txtMdxSuite/master/水果_forMdxBuilder.txt)  
[Windows 可执行文件下载](https://github.com/Snowdax/txtMdxSuite/raw/master/tab2mdx.exe)

### entryEXcontent
功能：交换词头和释义  
输出：TAB 连接的纯文本表格。文件名为：原文件名_exchanged.txt  
[输出文件示例](https://raw.githubusercontent.com/Snowdax/txtMdxSuite/master/水果_exchanged.txt)  
[Windows 可执行文件下载](https://github.com/Snowdax/txtMdxSuite/raw/master/entryEXcontent.exe)

### entryEXcontent_plus
功能：交换词头和释义，并添加至未交换数据内  
输出：TAB 连接的纯文本表格。文件名为：原文件名_exchanged_plus.txt  
[输出文件示例](https://raw.githubusercontent.com/Snowdax/txtMdxSuite/master/水果_exchanged_plus.txt)  
[Windows 可执行文件下载](https://github.com/Snowdax/txtMdxSuite/raw/master/entryEXcontent_plus.exe)

### tab2mdx_plus
功能：将双列表格转为 MdxBuilder 可用格式，既包含原词头，也包含从释义转换过去的词头  
输出：可用于 MdxBuilder 的文件。文件名为：原文件名_forMdxBuilder_plus.txt  
[输出文件示例](https://raw.githubusercontent.com/Snowdax/txtMdxSuite/master/水果_forMdxBuilder_plus.txt)  
[Windows 可执行文件下载](https://github.com/Snowdax/txtMdxSuite/raw/master/tab2mdx_plus.exe)

## 源代码
[tab2mdx](https://github.com/Snowdax/txtMdxSuite/blob/master/tab2mdx.py)  
[entryEXcontent](https://github.com/Snowdax/txtMdxSuite/blob/master/entryEXcontent.py)  
[entryEXcontent_plus](https://github.com/Snowdax/txtMdxSuite/blob/master/entryEXcontent_plus.py)  
[tab2mdx_plus](https://github.com/Snowdax/txtMdxSuite/blob/master/tab2mdx_plus.py)
