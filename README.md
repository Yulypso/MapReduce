# Map Reduce

## Author

[![Linkedin: Thierry Khamphousone](https://img.shields.io/badge/-Thierry_Khamphousone-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/tkhamphousone/)](https://www.linkedin.com/in/tkhamphousone)

<br/>

## Getting Started

__Setup__
```bash
> git clone https://github.com/Yulypso/MapReduce.git
> cd MapReduce
```

__Run the code__

**WordCount**
```bash
> cd WordCount

# mapper
> cat sample.txt | python mapper.py

# mapper + reducer
> cat sample.txt | python mapper.py | python reducer.py
```