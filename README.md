
## ✨ Özellikler

- **Modern Tasarım**: Gradient arka planlar, animasyonlar ve responsive tasarım
- **Dinamik İçerik**: Python ile yönetilen portfolio verileri
- **İletişim Formu**: Ziyaretçilerin mesaj gönderebilmesi için form
- **Responsive Design**: Tüm cihazlarda mükemmel görünüm
- **Animasyonlar**: CSS ve JavaScript ile güzel geçiş efektleri

## 🔧 Teknolojiler

- **Frontend**: HTML5, CSS3, JavaScript
- **Framework**: Bootstrap 5
- **Fontlar**: Google Fonts (Poppins)

## 📦 Kurulum

### Gereksinimler
- Python 3.7+
- pip

### Adımlar

1. **Projeyi klonlayın**
```bash
git clone <repo-url>
cd Portfolio-Site
```

2. **Virtual environment oluşturun (önerilen)**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# veya
venv\Scripts\activate  # Windows
```

3. **Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

4. **Uygulamayı çalıştırın**
```bash
python app.py
```

5. **Tarayıcıda açın**
```
http://localhost:5000
```

## 📁 Proje Yapısı

```
Portfolio-Site/
├── app.py                 # Ana Flask uygulaması
├── requirements.txt       # Python bağımlılıkları
├── templates/            # HTML şablonları
│   ├── base.html         # Ana şablon
│   ├── index.html        # Ana sayfa
│   ├── about.html        # Hakkımda sayfası
│   ├── projects.html     # Projeler sayfası
│   └── contact.html      # İletişim sayfası
├── static/               # Statik dosyalar
│   ├── css/
│   │   └── style.css     # Ana CSS dosyası
│   ├── js/
│   │   └── main.js       # JavaScript dosyası
│   └── images/           # Görüntü dosyaları
└── README.md
```

## 🎨 Özelleştirme

### Portfolio Verilerini Güncelleme

`app.py` dosyasındaki `PORTFOLIO_DATA` sözlüğünü düzenleyerek kendi bilgilerinizi ekleyebilirsiniz:

```python
PORTFOLIO_DATA = {
    'name': 'Adınız Soyadınız',
    'title': 'Ünvanınız',
    'email': 'email@adresiniz.com',
    'github': 'https://github.com/kullaniciadi',
    'linkedin': 'https://linkedin.com/in/kullaniciadi',
    'bio': 'Kısa biyografi...',
    # ...
}
```

### Renkler ve Stiller

CSS değişkenlerini `static/css/style.css` dosyasında düzenleyebilirsiniz:

```css
:root {
    --primary-color: #6366f1;
    --secondary-color: #8b5cf6;
    --accent-color: #06b6d4;
    /* ... */
}
```

### Yeni Projeler Ekleme

`PORTFOLIO_DATA['projects']` listesine yeni proje sözlükleri ekleyebilirsiniz:

```python
{
    'title': 'Proje Adı',
    'description': 'Proje açıklaması...',
    'image': '/static/images/proje.jpg',
    'tech': ['Python', 'Flask', 'HTML'],
    'github': 'https://github.com/kullanici/proje',
    'demo': 'https://proje-demo.com'
}
```

## 📧 İletişim Formu Yapılandırması

İletişim formundan gelen mesajları e-posta olarak almak için `app.py` dosyasındaki contact route'unu düzenleyin:

```python
# SMTP ayarlarınızı ekleyin
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'your-email@gmail.com'
EMAIL_PASS = 'your-app-password'
```

## 🚀 Deployment

### Heroku
1. Heroku hesabı oluşturun
2. `Procfile` dosyası oluşturun:
```
web: python app.py
```
3. Git ile deploy edin

### Diğer Platformlar
- **PythonAnywhere**: Flask uygulamaları için ideal
- **DigitalOcean**: VPS ile tam kontrol
- **Vercel**: Hızlı deployment

## 🔒 Güvenlik

- Secret key'i production'da mutlaka değiştirin
- HTTPS kullanın
- Form validasyonu ekleyin
- Rate limiting uygulayın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Commit edin (`git commit -am 'Yeni özellik ekle'`)
4. Push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📞 İletişim

Sorularınız için:
- **E-posta**: info@yasarberkirgatoglu.com
- **GitHub**: [@yasarberkirgatoglu](https://github.com/yasarberkirgatoglu)
- **LinkedIn**: [yasarberkirgatoglu](https://linkedin.com/in/yasarberkirgatoglu)

---

**⭐ Beğendiyseniz projeye yıldız vermeyi unutmayın!** 
