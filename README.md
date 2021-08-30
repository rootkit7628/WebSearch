# WebSearch

> Python module allowing you to do various searches for links on the Web.


[![Python application](https://github.com/iTeam-S/WebSearch/actions/workflows/python-test.yml/badge.svg)](https://github.com/iTeam-S/WebSearch/actions/workflows/python-test.yml)
[![Publish](https://github.com/iTeam-S/WebSearch/actions/workflows/pip-upload.yml/badge.svg)](https://github.com/iTeam-S/WebSearch/actions/workflows/pip-upload.yml)

[![PyPI - Version](https://img.shields.io/pypi/v/websearch-python?style=for-the-badge)](https://pypi.org/project/websearch-python/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/websearch-python?label=DOWNLOADS&style=for-the-badge)](https://pypi.org/project/websearch-python/)



## Installation

```sh
pip3 install websearch-python
```

## Use

### Quick Start

```python
from websearch import WebSearch as web
for page in web('iTeam-$').pages[:2]:
   print(result)
```

```
[RESULTS]

 https://iteam-s.mg/
 https://github.com/iTeam-S
```
__________________________

### Initialization

```python
from websearch import WebSearch
web = WebSearch('Gaetan Jonathan BAKARY')
```

### Webpages results

```python
webpages = web.pages
for wp in webpages[:5]:
   print(wp)
```

```
[RESULTS]

   https://mg.linkedin.com/in/gaetanj
   https://portfolio.iteam-s.mg/?u=gaetan
   https://github.com/gaetan1903
   https://medium.com/@gaetan1903
   https://gitlab.com/gaetan1903
```


### Images results

```python
webimages = web.images
for wp in webimages[:5]:
   print(wp)
```

```
[RESULTS]

   https://tse3.mm.bing.net/th?id=OIP.-K25y8TqkOi9UG_40Ti8bgAAAA
   https://tse1.mm.bing.net/th?id=OIP.yJPVcDx6znFSOewLdQBbHgHaJA
   https://tse3.mm.bing.net/th?id=OIP.7rO2T_nDAS0bXm4tQ4LKQAHaJA
   https://tse2.mm.bing.net/th?id=OIP.IUIEkGQVzYRKaDA7WeeV7QHaEF
   https://tse3.explicit.bing.net/th?id=OIP.OmvVnMIVu2ZdNZHZzJK_hgAAAA
```


### PDF results

```python
from websearch import WebSearch
web = WebSearch('Math 220')
pdfs = web.pdf
for pdf in pdfs[:5]:
   print(pdf)
```

```
[RESULTS]

   https://www.coconino.edu/resources/files/pdfs/registration/curriculum/course-outlines/m/mat/mat_220.pdf
   https://www.jmu.edu/mathstat/Files/ALEKSmatrix.pdf
   https://www.jjc.edu/sites/default/files/Academics/Math/M220%20Master%20Syllabus%20SP18.pdf
   https://www.sonoma.edu/sites/www/files/2018-19cat-11math.pdf
   https://www.svsd.net/cms/lib5/PA01001234/Centricity/Domain/1009/3.3-3.3B-Practice-KEY.pdf
```


## LICENSE

MIT License

Copyright (c) 2021 [iTeam-$](https://iteam-s.mg)

