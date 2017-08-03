# DitherCamera
DitherCamera for Raspberry Pi Zero W

# ディザカメラ（Dither Camera）の製作
[AS-289R2 Thermal Printer Shield](http://www.nada.co.jp/as289r2/)  
[Raspberry Pi Zero W](https://www.raspberrypi.org/)  
[Raspberry Pi Camera Module V2](https://www.raspberrypi.org/)  

# 配線
RPi Zero W (TxD) -> (RxD) AS-289R2  
RPi Zero W (GND) -- (GND) AS-289R2  
RPi Zero W (GPIO18) -- (N.O.) シャッターSW  
RPi Zero W (GND) -- (COM) シャッターSW  

# 処理
シャッターが押されるとカメラで撮影、画像の回転とリサイズを行いimage.jpgを生成します。  
次にimagemagickを使ってimage.jpgをグレースケールに変換、ディザリング処理により画像を2値化変換しimage.bmp(横384px、縦512px、1bpp)を生成します。  
最後にimage.bmpをAS-289R2に出力します。  

# imagemagickのインストール
```
sudo apt-get install imagemagick
```

# Lisence
Dither Camera for RPi Zero W  
NADA ELECTRONICS, LTD.  
Copyright (c) 2017 Takehiro Yamaguchi, MIT License  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software  
and associated documentation files (the "Software"), to deal in the Software without restriction,  
including without limitation the rights to use, copy, modify, merge, publish, distribute,  
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all copies or  
substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING  
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND  
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  