from controllers import *


# urls.py
# FastAPIのルーティング用関数
# app.add_api_route('/', index)
app.add_api_route('/calc', calc, methods=['GET', 'POST'])  # new
app.add_api_route('/', index, methods=['GET', 'POST'])  # new
