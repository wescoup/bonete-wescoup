from flask import Flask, render_template, request

app = Flask(__name__)

# Alternative approach using query parameters for testing
@app.route('/')
@app.route('/')
@app.route('/')

def home():
    # Get the host from the request
    host = request.host.lower()
    
    # For local testing: Allow query parameter override
    test_version = request.args.get('version')
    if test_version == 'ph':
        return render_template('index_ph.html')
    elif test_version == 'us':
        return render_template('index_us.html')
    
    # Normal domain-based logic
    if '.ph' in host or 'com.ph' in host:
        return render_template('index_ph.html')
    else:
        return render_template('index_us.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Add to app.py
@app.route('/switch_language')
def switch_language():
    # Get the 'next' parameter which contains the page to redirect to
    next_page = request.args.get('next', 'home')
    # Get the language to switch to
    lang = request.args.get('lang', 'en')
    
    # Store in session if you want to persist throughout the visit
    session['language'] = lang
    
    # Redirect back to the page they were on
    return redirect(url_for(next_page, _anchor='top'))

if __name__ == '__main__':
    app.run(debug=True)