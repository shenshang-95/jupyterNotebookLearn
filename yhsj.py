# 5.综上所列，其总的函数应该是
def masterTri(tier):
    '杨辉三角生成函数：'
    '''
    参数 tier：要生成的矩阵高度，为正整数，比如3；
       其中，模块的运行速度有很大的提高空间；
       输出也可以美化。
    '''

    def print_figure(listPr):
        for values in listPr:
            space = len(listPr) - len(values)
            # print(space)
            if len(values) == 1:
                print(" " * (5 * space - 1), end="")
                print(1, end="   ")
                print("   ", end="")
            else:
                print(" " * 5 * space, end="")
                if len(values) == 2:
                    for i in values:
                        print(i, end="    ")
                        print("   ", end="")
                else:
                    for i in values:
                        print(i, end="    ")
                        print(" ", end="")
            print("\n")

    def yangHuiT(tier):
        printContent = []
        for i in range(1, tier + 1):
            printContent.append(listRow(i))
        return printContent

    def listRow(num_oneline):
        numRow = []
        if num_oneline == 1:
            return [1]
        if num_oneline == 2:
            return [1, 1]
        else:
            num_oneline = num_oneline - 1
            for i in range(num_oneline + 1):
                result = factorial(num_oneline) / (factorial(i) * factorial(num_oneline - i))
                numRow.append(result)
        return numRow

    def factorial(n):
        # start=time.time()
        s = 1
        for i in range(1, n + 1):
            if n == 1:
                return 1
            else:
                s = s * i
        # end=time.time()
        # useTime=end-start
        return s  # ,useTime,

    print_figure(yangHuiT(tier))

def factorial(n):
    #start=time.time()
    s=1
    for i in range(1,n+1):
        if n==1:
            return 1
        else:
            s=s*i
    #end=time.time()
    #useTime=end-start
    return s #,useTime,

def listRow(num_oneline):
    numRow=[]
    if num_oneline==1:
        return [1]
    if num_oneline==2:
        return [1,1]
    else:
        num_oneline=num_oneline-1
        for i in range(num_oneline+1):
            result=factorial(num_oneline)/(factorial(i)*factorial(num_oneline-i))
            numRow.append(result)
    return numRow

def yangHuiT(tier):
    printContent=[]
    for i in range(1,tier+1):
        printContent.append(listRow(i))
    return printContent