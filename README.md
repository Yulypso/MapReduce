# Map Reduce

## Author

[![Linkedin: Thierry Khamphousone](https://img.shields.io/badge/-Thierry_Khamphousone-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/tkhamphousone/)](https://www.linkedin.com/in/tkhamphousone)

<br/>

## Getting Started

__Setup__
```bash
> git clone https://github.com/Yulypso/MapReduce.git
> cd MapReduce

# for MacOs/Linux
> source .venv/bin/activate

#for Windows
> py -3 -m venv .venv
> .venv\scripts\activate

# to install requirements 
> pip3 install -r requirements.txt
```

__Run the code__

**WordCount**
```bash
> cd Project/WordCount

# mapper
> cat sample.txt | python3 mapper.py

# mapper + reducer
> cat sample.txt | python3 mapper.py | python3 reducer.py
```

**TotalProfit/Countries**
```bash
> cd Project/TotalProfit

# mapper
> python3 mapper.py

# mapper + reducer
> python3 mapper.py | python3 reducer.py
```

**TotalProfit Mean from TotalProfit/Countries**
```bash
> cd Project/TotalProfit

# mapper
> python3 mapper.py | python3 reducer.py | python3 TotalProfitMean/mapper.py

# reducer
> python3 mapper.py | python3 reducer.py | python3 TotalProfitMean/mapper.py | python3 TotalProfitMean/reducer.py
```