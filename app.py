from flask import Flask, render_template, request, flash, redirect, url_for
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Değiştirin!

# EmailJS Configuration
emailjs_config = {
    'public_key': os.getenv('EMAILJS_PUBLIC_KEY'),
    'service_id': os.getenv('EMAILJS_SERVICE_ID'),
    'template_id': os.getenv('EMAILJS_TEMPLATE_ID')
}

# Portfolio verileri
PORTFOLIO_DATA = {
    'name': 'Yaşar Berk Irgatoğlu',
    'title': 'iOS Developer & Python',
    'email': 'berk.irgatoglu1@gmail.com',
    'github': 'https://github.com/yasberk6',
    'linkedin': 'https://www.linkedin.com/in/yaşar-berk-irgatoğlu-b611a7230/',
    'bio': 'Merhaba! Ben Yaşar Berk Irgatoğlu, Bilgisayar Mühendisliği son sınıf öğrencisiyim. iOS geliştirme, yapay zeka ve mobil odaklı ürünler geliştirme konularına odaklanıyorum. Swift ile native iOS uygulamaları geliştiriyor, Firebase gibi modern servislerle backend entegrasyonları yapıyorum.',
    'skills': [
        {'name': 'Swift', 'level': 90},
        {'name': 'iOS Development', 'level': 88},
        {'name': 'Firebase', 'level': 85},
        {'name': 'CoreML', 'level': 80},
        {'name': 'Python', 'level': 85},
        {'name': 'Machine Learning', 'level': 78}
    ],
    'projects': [
        {
            'title': 'Cooklio - AI Destekli Tarif Uygulaması',
            'description': 'Kullanıcının elindeki malzemelere göre yapay zeka destekli tarif önerileri sunan iOS uygulaması. Görsel tanıma modeli ile yemek fotoğraflarından malzeme çıkarma özelliği.',
            'image': '/static/images/cooklio_logo_300x300.png',
            'screenshots': [
                '/static/images/cooklio/screenshot1.jpg',
                '/static/images/cooklio/screenshot2.jpg',
                '/static/images/cooklio/screenshot3.jpg'
            ],
            'tech': ['Swift (UIKit)', 'Firebase Auth', 'Cloud Firestore', 'Firebase Storage', 'OpenAI API (GPT-4)', 'Google Gemini API'],
            'github': 'https://github.com/yasberk6/cooklio',
            'demo': '#',
            'tech_details': {
                'Swift (UIKit)': 'Uygulamanın native iOS arayüzü ve mantığı',
                'Firebase Auth': 'Kullanıcı kimlik doğrulama işlemleri',
                'Cloud Firestore': 'Malzeme verisi, kullanıcı geçmişi, favoriler vs. için veri tabanı',
                'Firebase Storage': 'Kullanıcıların yüklediği yemek fotoğraflarının saklanması',
                'OpenAI API (GPT-4)': 'Kullanıcının malzemelerine göre tarif önerisi oluşturmak için prompt tabanlı içerik üretimi',
                'Google Gemini API': 'Görüntü işleme (örneğin fotoğraftan bilgi çıkarma)'
            }
        },
        {
            'title': 'Vhalys - Fikir Paylaşım Platformu',
            'description': 'Kullanıcıların yaratıcı fikirlerini paylaştığı, oylama yapabildiği sosyal platform. AI destekli öneri sistemi ve kullanıcı istatistikleri ile gelişmiş deneyim.',
            'image': '/static/images/Vhalys_logo.png',
            'screenshots': [
                '/static/images/vhalys/screenshot1.PNG',
                '/static/images/vhalys/screenshot2.PNG',
                '/static/images/vhalys/screenshot3.PNG',
                '/static/images/vhalys/screenshot4.PNG',
                '/static/images/vhalys/screenshot5.PNG'
            ],
            'tech': ['Swift (UIKit)', 'Firebase Auth', 'Cloud Firestore'],
            'github': 'https://github.com/yasberk6/vhalys',
            'demo': '#',
            'tech_details': {
                'Swift (UIKit)': 'Uygulamanın ön yüzü',
                'Firebase Auth': 'Kullanıcı kayıt/giriş sistemi',
                'Cloud Firestore': 'Fikir gönderileri, oylama verileri, kullanıcı profilleri'
            }
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=PORTFOLIO_DATA, emailjs=emailjs_config)

@app.route('/about')
def about():
    return render_template('about.html', data=PORTFOLIO_DATA, emailjs=emailjs_config)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=PORTFOLIO_DATA, emailjs=emailjs_config)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if not name or not email or not message:
            flash('Lütfen tüm alanları doldurun!', 'error')
        else:
            flash('Mesajınız başarıyla gönderildi! En kısa sürede döneceğim.', 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html', data=PORTFOLIO_DATA, emailjs=emailjs_config)

@app.route('/project/cooklio')
def cooklio_detail():
    project = next((p for p in PORTFOLIO_DATA['projects'] if 'Cooklio' in p['title']), None)
    if not project:
        return redirect(url_for('projects'))
    return render_template('project_detail.html', project=project, data=PORTFOLIO_DATA, emailjs=emailjs_config)

@app.route('/project/vhalys')
def vhalys_detail():
    project = next((p for p in PORTFOLIO_DATA['projects'] if 'Vhalys' in p['title']), None)
    if not project:
        return redirect(url_for('projects'))
    return render_template('project_detail.html', project=project, data=PORTFOLIO_DATA, emailjs=emailjs_config)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

# Vercel için gerekli
app = app