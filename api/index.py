from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Hakkımda sayfası
@app.route('/about')
def about():
    return render_template('about.html')

# Projeler sayfası
@app.route('/projects')
def projects():
    projects_data = [
        {
            'id': 'cooklio',
            'title': 'Cooklio',
            'description': 'AI destekli yemek tarifi uygulaması. Fotoğraf çekerek malzemeleri tanımlayın ve kişiselleştirilmiş tarifler alın.',
            'image': '/static/images/cooklio-cover.jpg',
            'github': 'https://github.com/yasberk6/Cooklio',
            'demo': '#',
            'technologies': ['Flutter', 'Dart', 'AI/ML', 'Firebase']
        },
        {
            'id': 'vhalys',
            'title': 'Vhalys',
            'description': 'Modern web teknolojileri ile geliştirilmiş kapsamlı proje yönetim sistemi.',
            'image': '/static/images/project2.jpg',
            'github': 'https://github.com/yasberk6/vhalys',
            'demo': '#',
            'technologies': ['React', 'Node.js', 'MongoDB', 'Express']
        },
        {
            'id': 'portfolio',
            'title': 'Portfolio Website',
            'description': 'Flask ile geliştirilmiş kişisel portfolio websitesi. Modern tasarım ve responsive yapı.',
            'image': '/static/images/project3.jpg',
            'github': 'https://github.com/yasberk6/PortfolioWebSite',
            'demo': '#',
            'technologies': ['Flask', 'Python', 'HTML/CSS', 'JavaScript']
        }
    ]
    return render_template('projects.html', projects=projects_data)

# Proje detay sayfası
@app.route('/project/<project_id>')
def project_detail(project_id):
    projects_data = {
        'cooklio': {
            'title': 'Cooklio - AI Destekli Yemek Tarifi Uygulaması',
            'description': 'Cooklio, yapay zeka teknolojisi kullanarak fotoğraflardan malzemeleri tanımlayan ve kişiselleştirilmiş yemek tarifleri sunan mobil uygulamadır.',
            'image': '/static/images/cooklio-cover.jpg',
            'screenshots': [
                '/static/images/cooklio/screenshot1.jpg',
                '/static/images/cooklio/screenshot2.jpg',
                '/static/images/cooklio/screenshot3.jpg'
            ],
            'github': 'https://github.com/yasberk6/Cooklio',
            'demo': '#',
            'technologies': ['Flutter', 'Dart', 'AI/ML', 'Firebase', 'Google Vision API'],
            'features': [
                'Fotoğraf çekerek malzeme tanıma',
                'AI destekli tarif önerileri',
                'Kişiselleştirilmiş beslenme tavsiyeleri',
                'Favori tarifler sistemi',
                'Sosyal paylaşım özellikleri'
            ]
        },
        'vhalys': {
            'title': 'Vhalys - Proje Yönetim Sistemi',
            'description': 'Modern web teknolojileri ile geliştirilmiş kapsamlı proje yönetim ve takım iş birliği platformu.',
            'image': '/static/images/project2.jpg',
            'screenshots': [
                '/static/images/project2.jpg'
            ],
            'github': 'https://github.com/yasberk6/vhalys',
            'demo': '#',
            'technologies': ['React', 'Node.js', 'MongoDB', 'Express', 'Socket.io'],
            'features': [
                'Proje ve görev yönetimi',
                'Takım iş birliği araçları',
                'Gerçek zamanlı bildirimler',
                'Raporlama ve analitik',
                'Dosya paylaşım sistemi'
            ]
        }
    }
    
    if project_id in projects_data:
        return render_template('project_detail.html', project=projects_data[project_id])
    else:
        return render_template('404.html'), 404

# İletişim sayfası
@app.route('/contact')
def contact():
    return render_template('contact.html')

# API endpoint for contact form (optional)
@app.route('/api/contact', methods=['POST'])
def contact_api():
    try:
        data = request.get_json()
        # Burada EmailJS client-side'da çalışacak, server-side işlem gerekmez
        return jsonify({'status': 'success', 'message': 'Message received'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 