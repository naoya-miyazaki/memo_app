import sqlite3

def create_database():
    # SQLiteデータベースに接続（なければ新しく作成）
    conn = sqlite3.connect('memo_app.db')  # データベース名
    cursor = conn.cursor()

    # メモ用テーブルを作成
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        );
    ''')

    # 変更を保存
    conn.commit()

    # 接続を閉じる
    conn.close()

# 関数を呼び出してデータベースとテーブルを作成
create_database()

def save_memo(title, content):
    # SQLiteデータベースに接続
    conn = sqlite3.connect('memo_app.db')
    cursor = conn.cursor()

    # メモをデータベースに挿入
    cursor.execute('''
        INSERT INTO memos (title, content) VALUES (?, ?)
    ''', (title, content))

    # 変更を保存
    conn.commit()

    # 接続を閉じる
    conn.close()

# メモを保存
save_memo("タイトル1", "内容1")

def show_memos():
    # SQLiteデータベースに接続
    conn = sqlite3.connect('memo_app.db')
    cursor = conn.cursor()

    # メモを全て取得
    cursor.execute('SELECT * FROM memos')
    memos = cursor.fetchall()

    # メモを表示
    for memo in memos:
        print(f"ID: {memo[0]}, Title: {memo[1]}, Content: {memo[2]}")

    # 接続を閉じる
    conn.close()

# 保存されているメモを表示
show_memos()

def main():
    print("メモ帳アプリ")
    title = input("メモのタイトルを入力してください: ")
    content = input("メモの内容を入力してください: ")
    save_memo(title, content)
    print("メモが保存されました。")
    
    print("\n保存されたメモ:")
    show_memos()

# メイン関数を実行
main()


