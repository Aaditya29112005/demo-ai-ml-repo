from api.main import app
@app.get('/')
def health(): return {'status': 'ok'}
