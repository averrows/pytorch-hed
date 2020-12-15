# pytorch-hed
This is a personal reimplementation of Holistically-Nested Edge Detection [[1]](#references) using PyTorch based on the previous pytorch implementation by [sniklaus](https://github.com/sniklaus) [2](). If you would like to use of this work, please cite the paper accordingly. Also, make sure to adhere to the licensing terms of the authors. Moreover, if you will be making use of this particular implementation, please acknowledge the present [[3]](#references) implementation.

<a href="https://arxiv.org/abs/1504.06375" rel="Paper"><img src="http://www.arxiv-sanity.com/static/thumbs/1504.06375v2.pdf.jpg" alt="Paper" width="100%"></a>

|   |GitHub|Ref|
|---|---|---|
|Original version based on Caffe | https://github.com/s9xie/hed | [[1]](#references) |
|Another reimplementation based on Caffe | https://github.com/zeakey/hed |
|Original reimplementation based on PyTorch | https://github.com/sniklaus/pytorch-hed | [[2]](#references)|

## Usage
To run it on your own image, use the following command. Please make sure to see their paper / the code for more details.

```
python run.py --model bsds500 --in ./images/sample.png --out ./out.png
```

## References
```
[1]  @inproceedings{Xie_ICCV_2015,
         author = {Saining Xie and Zhuowen Tu},
         title = {Holistically-Nested Edge Detection},
         booktitle = {IEEE International Conference on Computer Vision},
         year = {2015}
     }
```

```
[2]  @misc{pytorch-hed,
         author = {Simon Niklaus},
         title = {A Reimplementation of {HED} Using {PyTorch}},
         year = {2018},
         howpublished = {\url{https://github.com/sniklaus/pytorch-hed}}
    }
```


```
[3]  @misc{pytorch-hed-2,
         author = {Davide Lanza},
         title = {A New Reimplementation of {HED} Using {PyTorch}},
         year = {2020},
         howpublished = {\url{https://github.com/Davidelanz/pytorch-hed}}
    }
```
