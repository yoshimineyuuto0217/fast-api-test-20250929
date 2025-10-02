## fast-api-test-20250929

fastAPI のテストコードと作成の注意点を分かりやすくまとめたもの

## ダミーデータを入れるための長れ

- 1.generate_csv.py を作りダーミーデータを入れる処理書く
- 2.generate_csv.py があるフォルダ内で python3 generate_csv.py
- 3.csv ファイルができてるはず
- 4.Docker にコピーする 『docker cp <コピーするファイルの位置を指定 (絶対パスで)> <移動先のコンテナ名>:<コンテナのパス>』
- <例> docker cp /Users/yoshimineisamuto/Redux/fastAPI/src/products.csv fastapi-fast-api-db-1:/tmp/products.csv
- 5.copy までできたら DB に入れ込み作業
- <例> \COPY product(product_id, product_name, product_weight, product_height, product_temperature, product_quantity, created_at, updated_at)
  FROM '/tmp/products.csv' DELIMITER ',' CSV HEADER;

## 500 エラーの解決の注意点

- docker-compose.yml に書いてる DB 情報と database.py に書いてる情報が違う
- どこかのファイルでインデントミスを起こしてエラー出てる
- 単純に Model の定義ミス
- src フォルダ外に python のファイルはない

## FastAPI で構築の流れ

- １.database.py 作成
- ２.model の定義
- ３.schemas でレスポンス・リクエストの設定
- ４.cruds で DB 操作をする
- ５.routes の設定

## その他

- SwaggerUI は main.py を読み込み表示させる
  > > > > > > > master
