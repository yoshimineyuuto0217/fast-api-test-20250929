from enum import Enum


class ErrorMessages(Enum):
    """
    1~100: 共通定数
    101~: 機能毎に10ずつ割り振っています。
    """
    # common
    MESSAGE_001 = "内部サーバーエラーが発生しました。"
    MESSAGE_002 = "データベースエラーが発生しました。"
    MESSAGE_003 = "認証が必要です"
    MESSAGE_004 = "アクセス権限がありません"
    MESSAGE_005 = "指定されたデータが見つかりません"

    # article
    MESSAGE_101 = "記事が見つかりません"

    # auth
    MESSAGE_111 = "Could not validate credentials"
    MESSAGE_112 = "Incorrect username or password"
    MESSAGE_113 = "Inactive user"
    MESSAGE_114 = "Admin privileges required"
    MESSAGE_115 = "Please verify your email before logging in."

    # category
    MESSAGE_121 = "指定されたカテゴリが存在しません"
    MESSAGE_122 = "カテゴリ名はすでに存在します。"

    # chatgpt
    MESSAGE_131 = "Invalid UUID value"
    MESSAGE_132 = "Invalid Binary value"
    MESSAGE_133 = "OpenAI API error"
    MESSAGE_134 = "Conversation not found"

    # goal
    MESSAGE_141 = "指定された目標は登録されていません。"

    # user
    MESSAGE_151 = "Email address already registered"
    MESSAGE_152 = "User not found"
    MESSAGE_153 = "現在のパスワードが正しくありません"

    # scraper
    MESSAGE_161 = "Failed to save image URL"

    # schedule
    MESSAGE_171 = "開始時刻は終了時刻より前に設定してください。"
    MESSAGE_172 = "開始時刻は現在より後に設定してください。"
    MESSAGE_173 = "タイトルを入力してください。"
    MESSAGE_174 = "スケジュールが見つかりません。"

    # study_time
    MESSAGE_181 = "指定された学習時間は登録されていません。"
    MESSAGE_182 = "本日の学習時間は既に登録されています"

    # course
    MESSAGE_191 = "指定されたコースは登録されていません。"

    #saved_item
    MESSAGE_201 = "指定された保存項目は登録されていません。"
    MESSAGE_202 = "指定された保存項目はすでに存在します。"