from datetime import datetime, timedelta
import json
from elasticsearch import Elasticsearch
from requests_aws4auth import AWS4Auth
from tqdm import tqdm
import elastic_config
from datetime import datetime

# Elasticsearch 엔드포인트 설정
es_endpoint = elastic_config.es_endpoint
es_username = elastic_config.es_username
es_password = elastic_config.es_password

# Elasticsearch에 연결
es = Elasticsearch([es_endpoint], basic_auth=(es_username, es_password))

# 인덱스 이름 설정
today = datetime.today() + timedelta(hours=9)
yesterday = today - timedelta(days=1)
index_today_name = "elastic_everytime"+today.strftime("%m%d")
index_yesterday_name = "elastic_everytime" + yesterday.strftime("%m%d")


# 인덱스 생성
es.indices.create(index=index_today_name)

rows = []

with open("everytime_computer_data.json", 'r', encoding='UTF-8') as f:
    for line in f:
        rows.append(json.loads(line))

for index in tqdm(range(len(rows)), desc="Adding documents to Elasticsearch"):
    json_object = {
        "title": rows[index]["title"],
        "detail": rows[index]["detail"],
        "likes": rows[index]["likes"],
        "comments_count": rows[index]["comments_count"],
        "scraps": rows[index]["scraps"],
        "url": rows[index]["url"],
        "comments": rows[index]["comments"],
        "timestamp": rows[index]["timestamp"]
    }

    es.index(index=index_today_name, body=json.dumps(json_object))

alias_name = "elastic_everytime_alias"
es.indices.put_alias(index=index_today_name, name=alias_name)

print("Success: All documents added to elastictest index.")

es.indices.delete(index=index_yesterday_name, ignore=[400, 404])
print("Index", index_yesterday_name, "deleted successfully.")
