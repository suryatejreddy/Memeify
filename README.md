# Memeify
This repository provides parts of the code and datasets for the paper - [Memeify: A Large Scale Meme Generation System](https://dl.acm.org/doi/abs/10.1145/3371158.3371403) published at [CODS-COMAD 2020](https://cods-comad.in/2020/). The code has been tested on Python 3.6.8 and Tensorflow 1.14.

## Datasets
The meme captions and images are made available [here](https://drive.google.com/drive/folders/16ppWgtSHELox1qHL9_CwqPk7U3SCE2XK?usp=sharing).

## Generation
The code for generating and sampling new memes can be found in the ``Memeify.ipynb`` notebook. For varying the quality of memes, please tune the ``temperature`` parameter in the code to modify the softmax distribution behaviour.

## Acknowledgements
Parts of the code have been used from this [repository](https://github.com/minimaxir/gpt-2-simple).

## Citation
If you found our work useful, please consider citing it as:
```
@incollection{vyalla2020memeify,
  title={Memeify: A Large-Scale Meme Generation System},
  author={Vyalla, Suryatej Reddy and Udandarao, Vishaal},
  booktitle={Proceedings of the 7th ACM IKDD CoDS and 25th COMAD},
  pages={307--311},
  year={2020}
}
```

In case of any queries, you can contact us:
- suryatej16102 [at] iiitd [dot] ac [dot] in
- vishaal16119 [at] iiitd [dot] ac [dot] in
