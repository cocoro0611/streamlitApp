## Streamlitを用いた環境構築
### 仮想環境の構築とアクティブ化と停止
```bash
# 仮想環境をインストール
$ python3 -m venv .venv   #.venvは任意の名前で良いが隠しフォルダの方がいい

# ターミナルが(.venv)となり仮想環境が立ち上がる
$ source .venv/bin/activate 

# 仮想環境を停止させる
$ deactivate 
```

### Streamlitの導入と操作
```bash
# Streamlitのインストール
$ pip install streamlit

# サンプルアプリの起動
$ streamlit hello

# 作成したアプリの起動（app.py）
$ streamlit run app.py
```

### DBの設定(SQLAlchemy + Alembic)
```bash
# ORMなどのインストール
pip install sqlalchemy         # ORMの本体
pip install psycopg2-binary    # PostgreSQLドライバ
pip install python-dotenv      # 環境変数管理
pip install alembic            # マイグレーション管理

# alembicの操作
$ alembic init migrations      # 初期化
$ alembic revision             # migrationsファイルの作成
$ alembic upgrade head         # migrationsの実行

# (任意の名前のmigrationsファイルを作成するとき)
$ alembic revision --autogenerate -m "first-migrate" 
```

## Streamlitのデプロイ手順
1. `requirements.txt` の作成 (指定のバージョンがインストールされるようにする)
```bash
$ pip freeze > requirements.txt
```
1. `.gitignore` の準備
   - vscodeからは上げるファイルのチャックボックスを外せば自動でgitignoreファイルが生成される
   - .venvなどの仮想環境に関係するファイルは上げる必要はない
2. GUIにてデプロイ(publicにしないとできない)

## 参考リンク
- [公式ドキュメントの環境構築](https://docs.streamlit.io/get-started/installation/command-line)
- [公式チュートリアル](https://docs.streamlit.io/develop/tutorials)
- [サンプルアプリの例](https://gihyo.jp/article/2024/10/monthly-python-2410)