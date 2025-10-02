import csv
import random
from faker import Faker
from datetime import datetime, timezone

fake = Faker("ja_JP")

# 製品名リスト
product_names = ["製品1", "製品2", "製品3", "製品4", "製品5"]

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # ヘッダー行を JSON のキーに合わせる
    writer.writerow(
        [
            "product_id",
            "product_name",
            "product_weight",
            "product_height",
            "product_temperature",
            "product_quantity",
            "created_at",
            "updated_at",
        ]
    )

    for i in range(1, 20000000):
        writer.writerow(
            [
                i,
                random.choice(product_names),
                f"{fake.random_int(100, 5000)}mg",
                f"{fake.random_int(500, 2000)}mm",
                f"{fake.random_int(0, 2000)}℃",
                fake.random_int(1, 100),
                datetime.now(timezone.utc).isoformat(),
            ]
        )

print("products.csv を生成しました！")
