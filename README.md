# Skylark
Skylark - 雲雀(競馬予測素体作成)


```sql
CREATE DATABASE skylark CHARACTER SET utf8mb4;
CREATE USER 'skylark'@'%' IDENTIFIED BY 'skylarkpw!';
GRANT ALL PRIVILEGES ON skylark . * TO 'skylark'@'%';
FLUSH PRIVILEGES;
```

```bash
sudo dnf install -y chromium-headless at-spi2-atk

git clone git@github.com:m10i-0nyx/skylark.git
cd skylark
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv -p 3.14 .venv
source .venv/bin/activate
uv pip install -U -r requirements.txt
playwright install chromium-headless-shell
python3 ./app.py -U -S -F
streamlit run webui.py

```
