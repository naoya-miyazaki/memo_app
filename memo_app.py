import sqlite3

# SQLiteのデータベースを作成・接続
conn = sqlite3.connect('memo_app.db')
cursor = conn.cursor()

# メモテーブルを作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS memos (
    id INTEGER PRIMARY KEY,
    content TEXT
)
''')

# メモを追加する関数
def add_memo(content):
    cursor.execute("INSERT INTO memos (content) VALUES (?)", (content,))
    conn.commit()
    print("メモが保存されました。")

# メモを表示する関数
def show_memos():
    cursor.execute("SELECT * FROM memos")
    memos = cursor.fetchall()
    if memos:
        for memo in memos:
            print(f"ID: {memo[0]}, メモ: {memo[1]}")
    else:
        print("保存されたメモはありません。")

# メモを編集する関数
def edit_memo(id, new_content):
    cursor.execute("UPDATE memos SET content = ? WHERE id = ?", (new_content, id))
    conn.commit()
    print("メモが更新されました。")

# メモを削除する関数
def delete_memo(id):
    cursor.execute("DELETE FROM memos WHERE id = ?", (id,))
    conn.commit()
    print("メモが削除されました。")

# メニュー
def menu():
    while True:
        print("\nメモ帳アプリ")
        print("1. メモを追加")
        print("2. メモを表示")
        print("3. メモを編集")
        print("4. メモを削除")
        print("5. 終了")
        
        choice = input("選択してください: ")
        
        if choice == '1':
            content = input("メモの内容を入力: ")
            add_memo(content)
        elif choice == '2':
            show_memos()
        elif choice == '3':
            show_memos()
            id = int(input("編集するメモのIDを入力: "))
            new_content = input("新しい内容を入力: ")
            edit_memo(id, new_content)
        elif choice == '4':
            show_memos()
            id = int(input("削除するメモのIDを入力: "))
            delete_memo(id)
        elif choice == '5':
            break
        else:
            print("無効な選択です。")

# メニューの表示
menu()

# データベース接続を閉じる
conn.close()
