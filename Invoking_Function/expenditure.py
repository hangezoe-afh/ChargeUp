import json

class expenditure:
    def __init__(self) -> None:
        # 初始化读取json文件赋值给data
        with open('expenditrue.json', 'r') as file:
            self.data = json.load(file)

    def ed(self,date:str, money: int, type_:str):
        '''
        ed():将记账信息写入json文件
        date:记账的日期
        money:记账的金额
        type_:此金额的用途或来源
        '''
        # data: [['9.31',3],...]
        # date对应列表中存放列表，列表的第一个元素为日期date，第二个元素为相同日期有几笔记账
        if self.data["date"] != None and date == self.data[-1][0]:       # 此次记账与最后一次记账日期相同
            self.data[-1][1] += 1                                        # 相同日期记账数量 + 1
        elif self.data["date"] != None and date != self.data[-1][0]:     # 此次记账与最后一次记账日期不同
            if int(date) > int(self.data[-1][0]):                        # 此次记账是新一天的记账
                self.data.append([date,1])
            else:
                pass
            
    def amend(self,date:str):
        date_list = self.data["date"]

        left = 0
        right = len(date_list) - 1
        mid = 0

        while(left < right):
            center = (left + right) // 2
            if left == center:
                mid = left
                break
            if int(date_list[center][0]) > int(date):
                right = center
            elif int(date_list[center][0]) < int(date):
                left = center
            else:
                mid = center
                break

        


    