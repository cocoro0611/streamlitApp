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

# alembicの初期化
$ alembic init migrations      # 初期化

# migrations/env.pyファイルの編集
import os                         # osのimportを追加
from src.database.models import Base   # modelsを参照を追加   

config.set_main_option('sqlalchemy.url', os.getenv("DATABASE_URL"))  # configの下にこれを追加
target_metadata = Base.metadata   # target_metadataにこれを設定

# migrationの実行
$ alembic revision --autogenerate -m "first-migrate"  # migrationsファイルの作成
$ alembic upgrade head         # migrationsの実行
```

### エラー対応

```bash
# DBにアクセルして「DROP TABLE alembic_version;」を削除する
> ERROR [alembic.util.messaging] Can't locate revision identified by 'f457c1606a58'
```

### pgAdminの設定
- ホスト名／アドレス：`postgres`
- ポート番号　　　　：`5432`
- 管理用データベース：`test_python`
- ユーザ名　　　　　：`cocoro`
- パズワード　　　　：`Pa55word`

## Streamlitのデプロイ手順
1. `requirements.txt` の作成 (指定のバージョンがインストールされるようにする)
```bash
$ pip freeze > requirements.txt
```
1. `.gitignore` の準備
   - vscodeからは上げるファイルのチャックボックスを外せば自動でgitignoreファイルが生成される
   - .venvなどの仮想環境に関係するファイルは上げる必要はない
2. GUIにてデプロイしたいGithubのディレクトリを選択する
3. 環境変数を設定するために、Sttings/Secretsに `DATABASE_URL` などを入力する(RenderのPostgreSQLの場合はhostnameの後ろに.oregon-postgresが必要)

## 参考リンク
- [公式ドキュメントの環境構築](https://docs.streamlit.io/get-started/installation/command-line)
- [公式チュートリアル](https://docs.streamlit.io/develop/tutorials)
- [サンプルアプリの例](https://gihyo.jp/article/2024/10/monthly-python-2410)