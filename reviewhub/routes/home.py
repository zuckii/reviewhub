from flask import Blueprint, render_template, redirect, url_for, session

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def homepage():
    # redirect to login if not authenticated or in guest mode
    if not session.get('user_id') and not session.get('guest_mode'):
        return redirect(url_for('auth.login'))
    
    # Mock movies data - replace with database query later
    movies = [
        {'id': 1, 'title': 'Inception', 'poster': 'https://via.placeholder.com/300x450/2563eb/ffffff?text=Inception'},
        {'id': 2, 'title': 'The Dark Knight', 'poster': 'https://via.placeholder.com/300x450/1e40af/ffffff?text=Dark+Knight'},
        {'id': 3, 'title': 'Interstellar', 'poster': 'https://via.placeholder.com/300x450/7c3aed/ffffff?text=Interstellar'},
        {'id': 4, 'title': 'Matrix', 'poster': 'https://via.placeholder.com/300x450/059669/ffffff?text=Matrix'},
        {'id': 5, 'title': 'Parasite', 'poster': 'https://via.placeholder.com/300x450/dc2626/ffffff?text=Parasite'},
        {'id': 6, 'title': 'Pulp Fiction', 'poster': 'https://via.placeholder.com/300x450/f59e0b/ffffff?text=Pulp+Fiction'},
        {'id': 7, 'title': 'Gladiator', 'poster': 'https://via.placeholder.com/300x450/8b5cf6/ffffff?text=Gladiator'},
        {'id': 8, 'title': 'Avatar', 'poster': 'https://via.placeholder.com/300x450/0891b2/ffffff?text=Avatar'},
    ]
    
    return render_template("home/index.html", movies=movies)

