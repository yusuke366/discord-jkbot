# Google Cloud Storage (GCS) にアバター画像を公開する手順

## 1. バケットを作成

バケット名は全世界で一意である必要があります。

例:

```bash
gcloud storage buckets create gs://denkitv \
  --location=asia-northeast1
```

確認:

```bash
gcloud storage buckets list
```

期待例:

```text
gs://denkitv
```

---

## 2. フォルダ構成

ローカル

```text
avatars/
├── aya.png
├── misaki.png
├── rin.png
├── yui.png
├── nagisa.png
└── kotone.png
```

---

## 3. 画像をアップロード

GCS上で

```text
gs://denkitv/jkbot/
```

という構造にしたい場合

```bash
gcloud storage cp avatars/* \
  gs://denkitv/jkbot/
```

確認

```bash
gcloud storage ls \
  gs://denkitv/jkbot/
```

期待例

```text
gs://denkitv/jkbot/aya.png
gs://denkitv/jkbot/misaki.png
gs://denkitv/jkbot/rin.png
```

---

## 4. 公開設定

画像を誰でも閲覧できるようにする

```bash
gcloud storage buckets add-iam-policy-binding \
  gs://denkitv \
  --member=allUsers \
  --role=roles/storage.objectViewer
```

確認

```bash
gcloud storage buckets get-iam-policy \
  gs://denkitv
```

期待例

```text
allUsers
roles/storage.objectViewer
```

---

## 5. アクセス確認

画像URL

```text
https://storage.googleapis.com/denkitv/jkbot/aya.png
```

ブラウザで画像が表示されれば成功。

---

## 6. Discord Bot 設定

```python
{
    "name": "あや",
    "avatar": "https://storage.googleapis.com/denkitv/jkbot/aya.png"
}
```

```python
{
    "name": "みさき",
    "avatar": "https://storage.googleapis.com/denkitv/jkbot/misaki.png"
}
```

---

## 7. 画像を更新する場合

同じファイル名で再アップロード

```bash
gcloud storage cp aya.png \
  gs://denkitv/jkbot/aya.png
```

再デプロイ不要。

数秒後から新しい画像が利用される。

---

## 8. 画像一覧確認

```bash
gcloud storage ls \
  gs://denkitv/jkbot/
```

---

## 9. バケット削除

画像削除

```bash
gcloud storage rm \
  gs://denkitv/jkbot/*
```

バケット削除

```bash
gcloud storage buckets delete \
  gs://denkitv
```