#!/usr/bin/env python
#coding:utf-8

prices={
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

p1={key:value for key,value in prices.items() if value > 200}

tech_names={'AAPL','IBM','HPQ','MSFT'}
p2={key:value for key,value in prices.items() if key in tech_names}
print(p1)
print(p2)

p1=dict((key,value) for key,value in prices.items() if value>200)
print(p1,type(p1))

p2=( (key,value) for key,value in prices.items())
print(dict(p2),type(p2))

p2={key:prices[key] for key in prices.keys() & tech_names}
print(p2)