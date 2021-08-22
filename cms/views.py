from cms import app


@app.route('/')
@app.route('/home/')
def home():
    return 'Hello World!'


@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    return 'new article'


@app.route('/posts/<int:id>', methods=['GET', 'POST'])
def post(id):
    print(id)
    return 'Article ' + str(id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'Login'


@app.route('/logout')
def logout():
    return 'Logout'
