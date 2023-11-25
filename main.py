import pandas as pd
import matplotlib.pyplot as plt
from os import system

orange_code = "\033[38;5;214m"
reset_code = "\033[0m"
cyan_code = "\u001b[36m"
red_code = "\033[31m"
green_code = "\033[32m"
yellow_code = "\u001b[33m"
geneDF = pd.read_csv("geneReport.csv")


def add_row(df: pd.DataFrame, valueList: list):
    df.loc[len(df)] = valueList
    print("\nRow added and database updated!")
    df.to_csv("geneReport.csv", index=False)
    print("\nNew state:")
    print(yellow_code, df)
    print("\n" + f"{cyan_code}={reset_code}" * 110)


def delete_row(df, index: list):
    print(index)
    for i in range(len(index)):
        index[i] = int(index[i])
    df.drop(index=index, axis=0, inplace=True)
    print("\nRow(s) deleted and database updated!")
    df.to_csv("geneReport.csv", index=False)
    print("\nNew state:")
    print(yellow_code, df)
    print("\n" + f"{cyan_code}={reset_code}" * 110)


def edit_values():
    system("cls")
    print("\n" + f"{cyan_code}={reset_code}" * 110)
    print(f"{red_code}EDITOR MODE{reset_code}")
    print(f"{cyan_code}={reset_code}" * 110)
    print("Current state:\n")
    print(green_code, geneDF, reset_code)
    index = int(input("\nEnter the index of the row to edit: "))
    field = input("Enter the field to edit: ").upper()

    if field in geneDF.columns:
        newValue = input(f"Enter the new value for {field}: ")
        geneDF.at[index, field] = newValue
        geneDF.to_csv("geneReport.csv", index=False)
        print("\nValue updated successfully & written to the database!")
        print("Updated state:\n")
        print(yellow_code, geneDF, reset_code)
        print("\n" + f"{cyan_code}={reset_code}" * 110)
    else:
        print(
            f"\n{red_code}Invalid field name. Please enter a valid field.{reset_code}"
        )
    ch = input("Edit again? [y/N]: ")
    if ch.lower() in ["y", "yes", "1", 1]:
        edit_values()


def chMkr(lvl: int):
    if lvl == 1:
        ch = input("\nEnter your command: ")
        print("\n" + f"{cyan_code}={reset_code}" * 110)
        if ch.lower() in ["1", "display", "log", "show"]:
            print("\nShowing data...\n")
            print(green_code, geneDF, reset_code)
            print("\n" + f"{cyan_code}={reset_code}" * 110)
        elif ch.lower() in ["2", "graph", "visualize", "plot"]:
            print("\nPlotting data")
            geneDF.set_index("GENEID").T.plot(marker="o", figsize=(10, 6))
            plt.title("Gene Expression under Different Treatments")
            plt.ylabel("Gene Expression Level")
            plt.xlabel("Treatments")
            plt.xticks(rotation=45)
            plt.legend(title="Genes", bbox_to_anchor=(1, 1), loc="upper left")
            plt.show()
            print(f"{green_code}Plotting successful.")
            print("\n" + f"{cyan_code}={reset_code}" * 110)
        elif ch.lower() in ["3", "manipulate", "change", "alter"]:
            chMkr(2)
        elif ch.lower() in ["4", "exit", "quit", "bye"]:
            print(
                f"{green_code}Thanks for visiting! B'bye!\n{reset_code}"
                + f"{cyan_code}={reset_code}" * 110
            )
            exit()
        else:
            print(f"{red_code}\nInvalid option, try again!{reset_code}")
            chMkr(1)
        chMkr(0)
    elif lvl == 2:
        print("\nSelect from the options below:")
        print("\n1. Add a row\n2. Delete a row\n3. Edit values\n")
        choice = input("Command: ")
        if choice.lower() in ["1", "add", "new"]:
            print("\nCurrent state:")
            print(green_code, geneDF, reset_code)
            gene_id = input("\nEnter Gene ID: ")
            control = float(input("Enter Control value: "))
            chemo = float(input("Enter Chemotherapy value: "))
            immuno = float(input("Enter Immunotherapy value: "))
            targeted = float(input("Enter Targeted Therapy value: "))
            valueList = [gene_id, control, chemo, immuno, targeted]
            add_row(geneDF, valueList)
        elif choice.lower() in ["2", "delete", "remove"]:
            print("\nCurrent state:")
            print(green_code, geneDF, reset_code)
            delIndex = input("\nEnter the index of the row to delete: ").split()
            delete_row(geneDF, delIndex)
        elif choice.lower() in ["3", "edit", "value"]:
            edit_values()
    else:
        ch = input("\nReturn to main menu? [Y/n] ")
        if ch.lower() in ["no", "n", "0", 0]:
            print("\n" + f"{cyan_code}={reset_code}" * 110)
            print(
                f"{green_code}Thanks for visiting! B'bye!\n{reset_code}"
                + f"{cyan_code}={reset_code}" * 100
            )
            exit()
        else:
            main()


def main():
    geneDF = pd.read_csv("geneReport.csv")
    system("cls")
    print("\n" + f"{cyan_code}={reset_code}" * 110)
    print(
        orange_code,
        r"""
   ____                    _                     ____  _       _   _             _           _         
  / __ \                  | |                   |  _ \(_)     | \ | |           | |         | |        
 | |  | |_   _  __ _ _ __ | |_ _   _ _ __ ___   | |_) |_  ___ |  \| | _____  __ | |     __ _| |__  ___ 
 | |  | | | | |/ _` | '_ \| __| | | | '_ ` _ \  |  _ <| |/ _ \| . ` |/ _ \ \/ / | |    / _` | '_ \/ __|
 | |__| | |_| | (_| | | | | |_| |_| | | | | | | | |_) | | (_) | |\  |  __/>  <  | |___| (_| | |_) \__ \
  \___\_\\__,_|\__,_|_| |_|\__|\__,_|_| |_| |_| |____/|_|\___/|_| \_|\___/_/\_\ |______\__,_|_.__/|___/ 
""",
        reset_code,
    )
    print(
        r"""                     __  __       _         __  __                  
                    |  \/  |     (_)       |  \/  |                 
                    | \  / | __ _ _ _ __   | \  / | ___ _ __  _   _ 
                    | |\/| |/ _` | | '_ \  | |\/| |/ _ \ '_ \| | | |
                    | |  | | (_| | | | | | | |  | |  __/ | | | |_| |
                    |_|  |_|\__,_|_|_| |_| |_|  |_|\___|_| |_|\__,_|
                                                     
    """
    )
    print(f"{cyan_code}={reset_code}" * 110)
    print("1. DISPLAY DATA\n2. VISUALIZE DATA\n3. DATA MANIPULATION\n4. EXIT")
    print(f"{cyan_code}={reset_code}" * 110)
    chMkr(1)


main()
