# mnzipcode
mnzipcode is a simple library for querying Mongolian zip codes.

  - Video introduction: [YOUTUBE](https://www.youtube.com/watch?v=vml3CxglLko)
  - PYPI: [MNZIPCODE](https://pypi.org/project/mnzipcode/)

### Installation

mnzipcode is available on PyPi:
```
# python -m pip install mnzipcode
```

### Example usage:

```python
>>> import mnzipcode 


>>> mnzipcode.matching_by_zipcode(11000)
{
  'stat': 'capital', 
  'mnname': 'Улаанбаатар', 
  'name': 'Ulaanbaatar', 
  'year_established': 1942, 
  'area': 4704.4, 
  'population': 1539810, 
  'density': 327, 
  'zipcode': '11000'
}


>>> mnzipcode.filter(mnname='Дархан-Уул')
[
  {
    'stat': 'province', 
    'mnname': 'Дархан-Уул', 
    'name': 'Darkhan-Uul', 
    'year_established': 1994, 
    'area': 3275.0, 
    'population': 107018, 
    'density': 33, 
    'zipcode': '45000', 
    'capital': 'Darkhan', 
    'capitalmn': 'Дархан'}, 
  {
    'mnname': 'Дархан-Уул', 
    'zipcode': '81041'
  }, 
  {
    'mnname': 'Дархан-Уул', 
    'zipcode': '81063'
  }
]

>>> mnzipcode.is_real(11000)
True

>>> mnzipcode.similar_to(8501)
[
  {'mnname': 'Зүүнхангай', 
  'zipcode': '85010'
  }, 
  {
    'mnname': 'Даланбулаг', 
    'zipcode': '85011'
  }, 
  {
    'mnname': 'Хайрхан', 'zipcode': '85013'
  }, 
  {
    'mnname': 'Жаргалант', 
    'zipcode': '85015'
  }, 
  {
    'mnname': 'Баянгол', 
    'zipcode': '85017'
  }
]
```