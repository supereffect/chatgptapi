# Base image olarak Python kullanalım
FROM python:3.9

# Uygulama dosyalarını /app dizinine kopyalayalım
COPY . /app

# Çalışma dizinini /app olarak ayarlayalım
WORKDIR /app

# Gerekli paketleri yükleyelim
RUN pip install flask flask_cors openai

# Uygulama portu
EXPOSE 8081

# Flask uygulamasını çalıştıralım
CMD ["python", "app.py"]