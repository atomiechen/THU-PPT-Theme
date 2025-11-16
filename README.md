> [!NOTE]
> 每到答辩季我就会喜获stars，谢谢大家的支持！欢迎推广传播本repo（[https://github.com/atomiechen/THU-PPT-Theme](https://github.com/atomiechen/THU-PPT-Theme)），也欢迎贡献[变体](variants/README.md)，提供更多选择🤠

# 清华简约主题PPT模板

[![GitHub Repo stars](https://img.shields.io/github/stars/atomiechen/THU-PPT-Theme?style=for-the-badge&logo=github&label=THU-PPT-Theme)](https://github.com/atomiechen/THU-PPT-Theme)

2020年春夏之交，答辩期间很多同学都在寻找清华主题的答辩模板。一方面有使用LaTeX制作Beamer的模板（见Overleaf上的模板[THU Beamer Theme](https://www.overleaf.com/latex/templates/thu-beamer-theme/vwnqmzndvwyb)），另一方面民间也存在着一些PPT模板。很多人可能不适应Beamer的使用（主要是内容和排版设计不是可见即所得，定制有门槛），以及我找到的PPT模板也都不太好使（要么图案设计太复杂、不好看，要么没有制作成PPT母版导致每次使用都要复制粘贴+微调，不方便）。

我制作了清华简约主题的PPT模板，后续有新的设计我会逐渐加入，也欢迎有兴趣有想法的朋友们添砖加瓦！

## 内容

所有模板均为 `.pptx` 文件。
此外也提供转换脚本用于 [Pandoc自动生成PPTX](#pandoc-支持)。

各个版本的修改历史见 [CHANGELOG.md](CHANGELOG.md)。


## 下载

推荐直接从 [GitHub Releases](https://github.com/atomiechen/THU-PPT-Theme/releases) 下载[最新发布版](https://github.com/atomiechen/THU-PPT-Theme/releases/latest)。

也可以在 [Github 仓库](https://github.com/atomiechen/THU-PPT-Theme) 单独下载所需文件。


## 效果

16:9比例，v1留边、v1顶边、v3留边白底、v3顶边白底：

![demo](pic/demo.png)



16:9比例，其他风格模板：v1扁平、v2扁平、v1暗光

![demo2](pic/demo2.png)



其他变体设计参见 [variants/README.md](variants/README.md)。



## 使用方式

可以基于所提供的文件自行修改内容，也可以在新建的PPT文稿中应用该模板。

后者在 MS Office 2019 For Mac 的 PowerPoint 里的具体使用方式为：首先选择幻灯片尺寸为16:9或4:3→点击设计→打开下拉菜单→点击浏览主题→选择你想使用的模板文件。

![image-20200609202001002](pic/select_from_design.jpg)

本模板通过编辑幻灯片母版来设计制作。如需定制，可自行编辑幻灯片母版。



## Pandoc 支持

可以将本仓库某模板作为 Pandoc 的 PPTX 模板使用，但前提是先跑转换脚本，将文件中母版中所有版式（layout）中文名改为 [Pandoc 支持的英文名](https://pandoc.org/demo/example33/10.1-structuring-the-slide-show.html#powerpoint-layout-choice)：

```sh
# 运行前需先安装依赖
pip install python-pptx
```

```sh
# 将某模板转换为 Pandoc 兼容的模板
python3 layouts.py rename "v3顶边白底16-9.pptx" template.pptx
```

```sh
# 运行 Pandoc，例如
pandoc input.md -t pptx -o output.pptx --reference-doc=template.pptx
```



## License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/atomiechen/THU-PPT-Theme">THU-PPT-Theme</a> © 2020 by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/atomiechen">Atomie CHEN</a> under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;"> CC BY-NC-SA 4.0 <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a></p>
