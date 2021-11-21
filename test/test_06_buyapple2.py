# 输入苹果的单价
price_str = float(input("苹果的单价："))
# 输入苹果的重量
weight_str = float(input("苹果的重量："))
# 计算支付的总金额
money = price_str * weight_str
print("苹果的单价为%.02f元/斤，苹果的重量为%.02f斤，您需要支付%.02f元。"
      % (price_str, weight_str, money))

student_no = 2
print("我叫小明，我的学号是：%04d" % student_no)

scale = 0.23
print("数据比例是:%.2f%%" % (scale * 100))
