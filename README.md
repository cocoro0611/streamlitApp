## Streamlitを用いた環境構築
1. 仮想環境の構築とアクティブ化と停止
```bash
# 仮想環境をインストール
$ python3 -m venv [.任意の名前]

# ターミナルが(.venv)となり仮想環境が立ち上がる
$ source [.任意の名前]/bin/activate 

# 仮想環境を停止させる
$ deactivate 
```

2. Streamlitを環境にインストールとサンプリアプリの立ち上げ
```bash
# Streamlitのインストール
$ pip install streamlit

# サンプルアプリの起動
$ streamlit hello
```


## Streamlitを用いた簡単なアプリケーションの作成
1. 新しい環境を使うときは、その都度、仮想環境を停止させる必要がある
```bash
$ deactivate 
```

2. `[.任意の名前]` と同じ階層に `app.py` ファイルを作成する
```python
import streamlit as st
st.write("Hello world")
```

3. 改めて仮想環境を立ち上げる
```bash
$ source [.任意の名前]/bin/activate
```

4. Streamlit アプリを実行する
```bash
$ streamlit run app.py
```

## Streamlitのデプロイ手順
1. `requirements.txt`ファイルを作成して、指定のバージョンがインストールされるようにする
```bash
$ pip freeze > requirements.txt
```
2. `.gitignore`ファイルの準備
```

```

3. GUIにてデプロイ

## その他ライブラリなどの環境構築
### Prisma
1. Prismaのインストール
```bash
# Prismaのインストール
$ pip install prisma

# Prismaの初期化
$ prisma init

# Prismaの操作
$ prisma generate
$ prisma migrate dev --name init
```
2. `schema.prisma`ファイルの作成例
```
datasource db {
provider = "postgresql"
url      = env("DATABASE_URL")
}

generator client {
provider = "prisma-client-py"
recursive_type_depth = -1  // Pythonの型サポートを改善
}

model User {
id        Int      @id @default(autoincrement())
email     String   @unique
name      String?
createdAt DateTime @default(now())
}
```


## 参考リンク
- [公式ドキュメントの環境構築](https://docs.streamlit.io/get-started/installation/command-line)
- [公式チュートリアル](https://docs.streamlit.io/develop/tutorials)
- [サンプルアプリの例](https://gihyo.jp/article/2024/10/monthly-python-2410)