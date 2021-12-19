import matplotlib.pyplot as plt
import subprocess as sbp
from scipy.signal import savgol_filter


def funcGraph(tx, t1y, t2y, name):
    t1y = savgol_filter(t1y, 51, 3)
    t2y = savgol_filter(t2y, 51, 3)
    plt.figure(name[-1], figsize = (5, 5))
    plt.title(name)
    plt.plot(tx, t1y, 'b', label = 'Naive Algorithm')
    plt.plot(tx, t2y, 'r', label = 'KMP Algorithm')
    plt.legend()
    plt.show()

def case1():
    needle = 'ab'
    haystack = 'ab'
    tx = []
    t1y = []
    t2y = []
    for i in range(1, 1001, 10):
        exe = sbp.run(r"C:\Users\LocalAdm\source\repos\StringAlgorithms\Release\StringAlgorithms.exe" + " 1 " + needle + " " + haystack + " " + str(i), stdout = sbp.PIPE)
        res = str(exe.stdout)
        print(res)
        tx.append(i)
        t1y.append(float(res[2 : res.find(' ')]))
        t2y.append(float(res[res.find(' ') + 1 : len(res) - 1]))
    funcGraph(tx, t1y, t2y, "Experiment #1")

def case2():
    needle = 'a'
    haystack = 'ab'
    tx = []
    t1y = []
    t2y = []
    for i in range(1, 1000001, 10000):
        exe = sbp.run(r"C:\Users\LocalAdm\source\repos\StringAlgorithms\Release\StringAlgorithms.exe" + " 2 " + needle + " " + haystack + " " + str(i), stdout = sbp.PIPE)
        res = str(exe.stdout)
        print(res)
        tx.append(i)
        t1y.append(float(res[2 : res.find(' ')]))
        t2y.append(float(res[res.find(' ') + 1 : len(res) - 1]))
    funcGraph(tx, t1y, t2y, "Experiment #2")

def case3():
    needle = 'aaaaa'
    haystack = 'aaaaab'
    tx = []
    t1y = []
    t2y = []
    for i in range(1, 1000001, 10000):
        exe = sbp.run(r"C:\Users\LocalAdm\source\repos\StringAlgorithms\Release\StringAlgorithms.exe" + " 3 " + needle + " " + haystack + " " + str(i), stdout = sbp.PIPE)
        res = str(exe.stdout)
        print(res)
        tx.append(i)
        t1y.append(float(res[2 : res.find(' ')]))
        t2y.append(float(res[res.find(' ') + 1 : len(res) - 1]))
    funcGraph(tx, t1y, t2y, "Experiment #3")

def case4():
    needle = ""
    haystack = ""
    print("Enter the needle value: ")
    needle = input()
    print("Enter the haystack value: ")
    haystack = input()
    tx = []
    t1y = []
    t2y = []
    for i in range(1, 100001, 1000):
        exe = sbp.run(r"C:\Users\LocalAdm\source\repos\StringAlgorithms\Release\StringAlgorithms.exe" + " 4 " + needle + " " + haystack + " " + str(i), stdout = sbp.PIPE)
        res = str(exe.stdout)
        print(res)
        tx.append(i)
        t1y.append(float(res[2 : res.find(' ')]))
        t2y.append(float(res[res.find(' ') + 1 : len(res) - 1]))
    funcGraph(tx, t1y, t2y, "Experiment #4")

case1()
case2()
case3()
case4()