# DIP-Homework4

### 数字图像处理 第四次作业

如有疑问，请联系：guoyb17@mails.tsinghua.edu.cn

## 依赖

程序需要Python 3支持，另外通过`pip3 install -r requirements.txt`安装依赖的包。

## 运行

程序接受形如下列的指令：

```shell
python3 main.py -i Lena-gray.jpg -m 1
```

也可以通过`-h`或`--help`获得简要帮助。其中，`-i`参数是输入图片，要求是方形2的幂次像素边长，建议使用仓库自带的`Lena-gray.jpg`；`-m`参数是任务模式，1对应Exp1的`（1）What if only using 1/4,1/16, 1/64 DCT coefficients?`，2对应Exp1的`（2）What if changing the size of blocks in 2D-DCT trial?`。

目前**仅实现**了`Exp1: Are they equivalent in effect?`。
