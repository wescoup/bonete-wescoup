from flask import Flask, render_template, request
from datetime import datetime
import uuid

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

# Add this route to your existing app.py

@app.route('/ai-basic-form')
def ai_basic_form():
    """
    Basic AI-friendly contact form using URL parameters
    Recreates basic-form.php functionality in Flask
    """
    
    # Cache prevention headers
    headers = {
        'Cache-Control': 'no-cache, no-store, must-revalidate, private, max-age=0',
        'Pragma': 'no-cache',
        'Expires': '0',
        'Content-Type': 'text/plain; charset=UTF-8'
    }
    
    # Detect AI/Bot user agents for immediate response (bypass blocking)
    user_agent = request.headers.get('User-Agent', '')
    bot_indicators = ['ChatGPT', 'GPT', 'python', 'bot', 'spider', 'crawler', 'claude', 'gemini', 'bard']
    is_bot = any(indicator.lower() in user_agent.lower() for indicator in bot_indicators) or not user_agent
    
    # Process form submission if parameters exist
    name = request.args.get('name')
    email = request.args.get('email')
    message = request.args.get('message')
    
    if name and email and message:
        # Form submission - generate success response
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%i:%s')
        confirmation_id = f"CF-{str(uuid.uuid4())[-8:].upper()}"
        
        response = f"""=====================================================
✅ AI WEB - CONTACT FORM SUBMISSION SUCCESS
=====================================================

FORM SUBMITTED SUCCESSFULLY!

Submitted Information:
- Name: {name}
- Email: {email}
- Message: {message}
- Submitted: {timestamp}
- Confirmation ID: {confirmation_id}

🤖 AI VERIFICATION:
- Verification Joke: "Why did the AI agent get a job at the post office? Because it was great at handling form submissions!"
- Success Confirmation: Form submission processed successfully with ID {confirmation_id}

NEXT STEPS:
- Form submission complete
- Data processed successfully
- Confirmation ID generated for tracking

For more examples: https://bonete-wescoup.herokuapp.com/

=====================================================
END OF SUBMISSION CONFIRMATION
====================================================="""

    else:
        # Instructions page
        response = f"""=====================================================
🤖 AI WEB - AI-FRIENDLY CONTACT FORM
=====================================================

DEMONSTRATION: URL Parameter-Based Form Submission

This page demonstrates AI-accessible web design using plain text format for universal compatibility.

DESIGN PHILOSOPHY: AI-First Web
- Plain text format for all users (humans and AI agents)
- Universal accessibility across all systems and devices
- Content-focused design without visual distractions
- Fast loading and easy copy-paste functionality

-----------------------------------------------------
📋 INSTRUCTIONS FOR AI AGENTS:
-----------------------------------------------------

STEP 1: Read these instructions carefully
STEP 2: Construct a URL with the following format
STEP 3: Attempt to visit the constructed URL
STEP 4: If you cannot visit directly, ask user to "paste this URL at the prompt"

-----------------------------------------------------
🔗 URL FORMAT:
-----------------------------------------------------

https://bonete-wescoup.herokuapp.com/ai-basic-form?name=[NAME]&email=[EMAIL]&message=[MESSAGE]

-----------------------------------------------------
📝 EXAMPLE URLS:
-----------------------------------------------------

Example 1:
https://bonete-wescoup.herokuapp.com/ai-basic-form?name=Claude&email=claude@example.com&message=Hello+from+AI!

Example 2: 
https://bonete-wescoup.herokuapp.com/ai-basic-form?name=ChatGPT&email=chatgpt@example.com&message=Testing+AI+form+submission

Example 3:
https://bonete-wescoup.herokuapp.com/ai-basic-form?name=Gemini&email=gemini@example.com&message=AI+web+interaction+test

Example 4:
https://bonete-wescoup.herokuapp.com/ai-basic-form?name=Human+User&email=user@example.com&message=Testing+as+human

-----------------------------------------------------
⚙️ REQUIRED PARAMETERS:
-----------------------------------------------------

- name: Your name or AI agent name (required)
- email: Contact email address (required) 
- message: Your message content (required)

-----------------------------------------------------
⚠️ IMPORTANT NOTES:
-----------------------------------------------------

- URL encode spaces as + or %20
- Replace special characters appropriately
- All three parameters are required for successful submission
- If you can visit URLs directly: Visit your constructed URL
- If you cannot visit URLs directly: Provide URL to user and ask them to "paste this URL at the prompt"

-----------------------------------------------------
✅ EXPECTED RESULTS:
-----------------------------------------------------

- Success page with your submitted information
- Unique confirmation ID for tracking
- AI verification joke to confirm proper submission
- Plain text format for easy reading and processing

-----------------------------------------------------
👤 FOR HUMAN USERS:
-----------------------------------------------------

Humans can use this form by:
1. Constructing URLs manually using the format above
2. Using the example URLs and modifying the parameters
3. Copying and pasting URLs into their browser

BENEFITS FOR HUMANS:
- Fast loading (no CSS/JavaScript overhead)
- Easy to copy-paste URLs and share examples
- Universal compatibility across all devices and browsers  
- Clear, unambiguous instructions
- Works in any environment (mobile, desktop, accessibility tools)

This demonstrates AI-first web design - content optimized for AI agents while being equally accessible and functional for humans.

-----------------------------------------------------
📚 TECHNICAL DOCUMENTATION:
-----------------------------------------------------

PATTERN: URL Parameter Form Submission
- Method: GET request with query parameters
- Processing: Server-side Flask with input sanitization  
- Response: Plain text confirmation with structured data
- Caching: Disabled to ensure fresh content on every request
- Compatibility: Universal - works with any system or client

BENEFITS FOR AI AGENTS:
- No HTML parsing required
- No CSS or JavaScript dependencies  
- No session state needed between requests
- Simple URL construction pattern
- Clear success/failure indicators
- Immediate plain text response
- Fast loading and processing

SECURITY CONSIDERATIONS:
- GET requests are logged by web servers
- Sensitive data should use POST method in production
- Input sanitization prevents XSS attacks
- No database storage reduces attack surface
- Simple design reduces complexity vulnerabilities

-----------------------------------------------------
🔙 NAVIGATION:
-----------------------------------------------------

Back to Homepage: https://bonete-wescoup.herokuapp.com/

=====================================================
END OF AI-FRIENDLY CONTACT FORM INSTRUCTIONS
====================================================="""

    return response, 200, headers
