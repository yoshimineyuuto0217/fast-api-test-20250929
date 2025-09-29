## 500エラーの解決の注意点

- docker-compose.ymlに書いてるDB情報とdatabase.pyに書いてる情報が違う
- どこかのファイルでインデントミスを起こしてエラー出てる
- 単純にModelの定義ミス
- srcフォルダ外にpythonのファイルはない

## FastAPIで構築の流れ

- １.database.py作成
- ２.modelの定義
- ３.schemasでレスポンス・リクエストの設定
- ４.crudsでDB操作をする
- ５.routesの設定


## その他

- SwaggerUIはmain.pyを読み込み表示させる