from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
    <head>
        <title>Muhammad Awat</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0f4ff;
                margin: 0;
                padding: 0;
                color: #2c2c54;
            }
            .container {
                max-width: 650px;
                margin: 50px auto;
                padding: 30px;
                background-color: #ffffff;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
                border-left: 5px solid #7f5af0;
            }
            .title {
                text-align: center;
                color: #7f5af0;
                font-size: 28px;
                font-weight: 700;
                margin-bottom: 5px;
            }
            .subtitle {
                text-align: center;
                color: #5e5e8f;
                font-size: 16px;
                margin-bottom: 30px;
            }
            section {
                margin-bottom: 25px;
            }
            h3 {
                color: #4c4c84;
                margin-bottom: 8px;
                font-size: 18px;
            }
            p, ul {
                margin: 0;
                font-size: 15px;
                line-height: 1.6;
            }
            ul {
                padding-left: 20px;
            }
            li {
                margin-bottom: 6px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="title">Muhammad Awat</div>
            <div class="subtitle">Motion Designer & CS Student</div>
            
            <section>
                <h3>Intro</h3>
                <p>Creative thinker with a passion for visual storytelling and technology. I blend design and code to bring ideas to life.</p>
            </section>

            <section>
                <h3>Skills</h3>
                <ul>
                    <li>Motion Graphics & Animation</li>
                    <li>Visual Design</li>
                    <li>Problem Solving with Code</li>
                </ul>
            </section>

            <section>
                <h3>Work</h3>
                <p>I create engaging motion content and study CS to better understand the logic behind creative tools.</p>
            </section>

            <section>
                <h3>Fun</h3>
                <p>I love movies, experimental visuals, and exploring how tech can empower creativity.</p>
            </section>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
