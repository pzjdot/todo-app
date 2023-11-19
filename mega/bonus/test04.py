waiting_list = ["sen", "ben", "john"]
waiting_list.sort()  # 默认升序
waiting_list.sort(reverse=True)  # reverse 是反转的意思，sort方法是默认reverse为False，手动改成True，排序就是降序了

for index, item in enumerate(waiting_list, start=1):
    print(f"{index}.{item.capitalize()}")

buttons = [('John', 'Sen', '1', '2'), ('Lin', 'Ajay', 'Filip', '1')]
for first, second, third, fourth in buttons:
    print(first, second, third, fourth)

