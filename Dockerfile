#ローカルの環境をそのままdocker環境に作るイメージ
#fastAPIフォルダをそのままdockerに作るイメージ

FROM python:3.11-slim


#dockerFileにディレクトリ作成
#pythonは以下のWORKDIR構成が多い
WORKDIR /app

# ここでビルドに必要なライブラリを追加
# C言語の環境もなぜか必要だから入れる
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libffi-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

#dockerFileにコピーする
COPY requirements.txt .

#dockerファィルにで読み込ませる
RUN pip3 install --no-cache-dir -r requirements.txt

#ローカルの環境をdockerの/appにコピー
COPY ./src/ /app

#動かす環境をセット
EXPOSE 8000

#docker起動時に動かすコマンド
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

