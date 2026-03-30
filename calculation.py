from fastapi import FastAPI, Depends, HTTPException  # new
import numpy as np
import re
import copy


pattern_operands = re.compile(r'^\d+$')
pattern_operators = re.compile(r'-\+\*/=')

stack = ['1','2','-']

def calc_RPN(stack0: list, a = 0.0, b = 0.0): #calculates from a stack using reverse poland notation
    stack = copy.deepcopy(stack0)
    result = 0.0
    e = stack[0]
    if e.isnumeric:
        calc_RPN(stack,float(e))
    if e == '+':
        return e + a  
    if e == '-':
        c = a - b
    if e == '/':
        c = a / b
    if e == '*':
        c = a * b

def calc_simple(a: float, b: float, operator: str):
    result = 0.0
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b
    else:
        return float('nan')

print(calc_simple(1,2,""))


def calc_default(stack: list): #MDAS (multi, div, add, sub)
    equation = ''
    for e in stack: 
        if verify(e) != 'invalid':
            equation += e
    return eval(equation)


def verify(c: str):
    # pattern_operands = re.compile(r'^\d+$')
    # pattern_operators = re.compile(r'-\+\*/=')
    if pattern_operands.match(c) is not None:
        return 'operand'

    if pattern_operators.match(c) is not None:
        return 'operator'

    return 'invalid'