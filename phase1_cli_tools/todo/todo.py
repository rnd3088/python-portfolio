todo_list = []  #辞書のリスト　例:{"task": "買い物", "done": False}

print("ToDoアプリ　タスクを入力して下さい \n(list: 一覧表示 / done 番号: 完了 /  undone 番号: 未完了 /delete 番号: 削除　/ exit: 終了)")

while True:
    command = input(">>> ").strip()

    if command == "exit":   #アプリ終了
        print("アプリを終了します。")
        break

    elif command == "list": #タスク一覧表示
        if not todo_list:
            print("エラー：登録されたタスクはありません。")
        else:
            print("タスク一覧:")
            for i, item in enumerate(todo_list, 1):
                status = "✔" if item ["done"] else " "
                print(f"{i}.[{status}] {item["task"]}")

    elif command.startswith("done"):    #タスク完了処理
        parts = command.split()
        if len(parts) == 2 and parts[1].isdigit():
            index = int(parts[1]) - 1
            if 0 <= index < len(todo_list):
                todo_list[index]["done"] = True
                print(f"タスク「{todo_list[index]['task']}」を完了にしました")
            else:
                print("エラー：その番号のタスクはありません")
        else:
            print("エラー：使い方: done 番号（例：done 2）")
    
    elif command.startswith("undone"):  #タスク未完了処理
        parts = command.split()
        if len(parts) == 2 and parts[1].isdigit():
            index = int(parts[1]) - 1
            if 0 <= index < len(todo_list):
                todo_list[index]["done"] = False
                print(f"タスク「{todo_list[index]['task']}」を未完了に戻しました")
            else:
                print("エラー：その番号のタスクはありません")
        else:
            print("エラー：使い方： undone 番号 (例：undone 2)")

    elif command.startswith("delete"):  #タスク削除処理
        parts = command.split()
        if len(parts) == 2 and parts[1].isdigit():
            index = int(parts[1]) -1 
            if 0 <= index < len(todo_list):
                removed = todo_list.pop(index)
                print(f"タスク「{removed['task']}」を削除しました")
            else:
                print("エラー：その番号のタスクはありません")
        else:
            print("エラー：使い方：　delete 番号 (例：delete 2)")
                
    else:
        todo_list.append({"task": command, "done": False})  #タスク追加処理
        print(f"タスク「{command}」を追加しました")
