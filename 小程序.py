import json
#做一个
# 定义一个全局变量来存储库存数据
inventory = {}

def load_inventory(filename):
    """从文件加载库存数据"""
    global inventory
    try:
        with open(filename, 'r') as file:
            inventory = json.load(file)
    except FileNotFoundError:
        inventory = {}

def save_inventory(filename):
    """保存库存数据到文件"""
    with open(filename, 'w') as file:
        json.dump(inventory, file)

def add_stock(item, quantity):
    """添加进货记录"""
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"进货：{item} +{quantity}")

def remove_stock(item, quantity):
    """添加出货记录"""
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"出货：{item} -{quantity}")
    else:
        print(f"库存不足：{item}")

def view_inventory():
    """查看当前库存"""
    print("当前库存：")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def main():
    filename = "inventory.json"
    load_inventory(filename)
    
    while True:
        print("\n请选择操作：")
        print("1. 添加进货记录")
        print("2. 添加出货记录")
        print("3. 查看当前库存")
        print("4. 退出")
        
        choice = input("输入选择(1/2/3/4): ")
        
        if choice == '1':
            item = input("输入货物名称: ")
            quantity = int(input("输入进货数量: "))
            add_stock(item, quantity)
        elif choice == '2':
            item = input("输入货物名称: ")
            quantity = int(input("输入出货数量: "))
            remove_stock(item, quantity)
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            save_inventory(filename)
            print("退出程序，数据已保存。")
            break
        else:
            print("无效选择，请重试。")

if __name__ == "__main__":
    main()
