# Discord Bot を GKE + ArgoCD でデプロイする手順

## 1. GKE クラスタ作成

GCP コンソール

```text
Kubernetes Engine
↓
クラスター
↓
クラスターを作成
↓
Autopilot
```

例

```text
クラスタ名: discord-jkbot
リージョン: asia-northeast1
```

---

## 2. Google Cloud SDK インストール

### Windows

Google Cloud SDK をインストール

ログイン

```powershell
gcloud auth login
```

プロジェクト確認

```powershell
gcloud projects list
```

プロジェクト選択

```powershell
gcloud config set project denkitv-502714
```

---

## 3. kubectl を GKE に接続

```powershell
gcloud container clusters get-credentials discord-jkbot --region asia-northeast1
```

確認

```powershell
kubectl get nodes
```

---

# ArgoCD導入

## 4. Namespace作成

```bash
kubectl create namespace argocd
```

---

## 5. ArgoCDインストール

```bash
kubectl apply -n argocd \
-f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

確認

```bash
kubectl get pods -n argocd
```

---

## 6. ArgoCD公開

```powershell
kubectl patch svc argocd-server -n argocd `
--type merge `
-p '{"spec":{"type":"LoadBalancer"}}'
```

確認

```bash
kubectl get svc -n argocd
```

例

```text
argocd-server  LoadBalancer  136.xxx.xxx.xxx
```

アクセス

```text
https://136.xxx.xxx.xxx
```

---

## 7. ArgoCD初期パスワード取得

### Linux

```bash
kubectl -n argocd get secret argocd-initial-admin-secret \
-o jsonpath="{.data.password}" | base64 -d
```

### Windows PowerShell

```powershell
$pass = kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}"

[System.Text.Encoding]::UTF8.GetString(
[System.Convert]::FromBase64String($pass)
)
```

ログイン

```text
ユーザー名: admin
パスワード: 上記で取得したもの
```

---

# Artifact Registry

## 8. Dockerリポジトリ作成

```bash
gcloud artifacts repositories create docker \
--repository-format=docker \
--location=asia-northeast1
```

確認

```bash
gcloud artifacts repositories list \
--location=asia-northeast1
```

---

## 9. Docker認証

```bash
gcloud auth configure-docker asia-northeast1-docker.pkg.dev
```

---

# Dockerイメージ作成

## 10. Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "app.chatbot"]
```

---

## 11. ビルド

```bash
docker build -t discord-jkbot .
```

確認

```bash
docker images
```

---

## 12. Artifact Registry用タグ付与

```bash
docker tag discord-jkbot:latest \
asia-northeast1-docker.pkg.dev/denkitv-502714/docker/discord-jkbot:latest
```

---

## 13. Push

```bash
docker push \
asia-northeast1-docker.pkg.dev/denkitv-502714/docker/discord-jkbot:latest
```

---

# Kubernetes Secret

## 14. Secret作成

```bash
kubectl create secret generic discord-jkbot-secret \
--from-literal=DISCORD_TOKEN=xxxxxxxx \
--from-literal=OPENAI_API_KEY=xxxxxxxx
```

確認

```bash
kubectl get secret
```

---

# Deployment作成

## 15. deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: discord-jkbot

spec:
  replicas: 1

  selector:
    matchLabels:
      app: discord-jkbot

  template:
    metadata:
      labels:
        app: discord-jkbot

    spec:
      containers:
      - name: bot

        image: asia-northeast1-docker.pkg.dev/denkitv-502714/docker/discord-jkbot:latest

        imagePullPolicy: Always

        env:
        - name: DISCORD_TOKEN
          valueFrom:
            secretKeyRef:
              name: discord-jkbot-secret
              key: DISCORD_TOKEN

        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: discord-jkbot-secret
              key: OPENAI_API_KEY

        resources:
          requests:
            cpu: 100m
            memory: 128Mi

          limits:
            cpu: 500m
            memory: 512Mi
```

---

## 16. 手動デプロイ

```bash
kubectl apply -f deployment.yaml
```

確認

```bash
kubectl get pods
```

ログ確認

```bash
kubectl logs -f deployment/discord-jkbot
```

---

# GitHub連携

## 17. リポジトリ登録

ArgoCD

```text
Settings
↓
Repositories
↓
Connect Repo
```

SSH の場合

```text
git@github.com:yusuke366/discord-chatgpt.git
```

Deploy Key を GitHub に登録

---

# ArgoCD Application作成

## 18. New App

```text
Applications
↓
NEW APP
```

設定

```text
Application Name:
discord-jkbot

Project:
default

Sync Policy:
Automatic

Repository:
git@github.com:yusuke366/discord-chatgpt.git

Revision:
main

Path:
k8s

Cluster:
https://kubernetes.default.svc

Namespace:
jkbot
```

作成

```text
Create
```

### project作成

```
> kubectl apply -f .\project.yaml
appproject.argoproj.io/jkbot created
> kubectl get appprojects -n argocd
NAME      AGE
default   6h51m
jkbot     14s
```

---

## 19. Sync

```text
Application
↓
SYNC
```

---

# 更新手順

## Dockerイメージ更新

```bash
docker build -t discord-jkbot .
```

```bash
docker tag discord-jkbot:latest \
asia-northeast1-docker.pkg.dev/denkitv-502714/docker/discord-jkbot:latest
```

```bash
docker push \
asia-northeast1-docker.pkg.dev/denkitv-502714/docker/discord-jkbot:latest
```

---

## Pod再起動

latestタグ運用時

```bash
kubectl rollout restart deployment discord-jkbot
```

---

## ArgoCD再同期

```text
Application
↓
Refresh
↓
Hard Refresh
↓
Sync
```

---

# トラブルシュート

## ImagePullBackOff

確認

```bash
kubectl describe pod <
POD名
>
```

原因

- Artifact Registryが存在しない
- imageパスが間違い
- pushしていない

---

## InvalidImageName

確認

```yaml
image:
```

imageの値が正しいか確認

---

## Secret確認

```bash
kubectl get secret
```

---

## Podログ確認

```bash
kubectl logs -f deployment/discord-jkbot
```