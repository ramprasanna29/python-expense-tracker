import csv
import os
FILE_NAME="expenses_csv.csv"
#create file if not exists
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,mode='w',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(["Date","Category","Amount"])
#add expenses
def add_expense():
    date=input("Enter the date(DD-MM-YYYY):")
    category=input("Enter the type of category(travel,medical,etc...):")
    amount=input("enter the amount in rupees:")
    with open(FILE_NAME,mode='a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([date,category,amount])
    print("Expense successfully added")
#View expenses
def view_expenses():
    with open(FILE_NAME,mode='r') as file:
        reader=csv.reader(file)
        for rows in reader:
            print(rows)
#Total expenses
def tot_expenses():
    total=0
    with open(FILE_NAME,mode='r') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            total+=float(row[2])
    print(f"Total Expense:{total}")
#main menu
def main():
    create_file()
    while True:
        print("\n----Expense Tracker----")
        print("1.Add expense")
        print("2.View expense")
        print("3.Total expense")
        print("4.Exit")
        choice=input("Enter your choice:")
        if choice=='1':
            add_expense()
        elif choice=='2':
            view_expenses()
        elif choice=='3':
            tot_expenses()
        elif choice=='4':
            print("Exiting")
            break
        else:
            print("Invalid choice")
if __name__=="__main__":
    main()