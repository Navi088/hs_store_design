from flask import Flask, render_template, request
from items import GetItems
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():

    get_items = GetItems
    get_list = get_items.paginate_items()

    return render_template('products.html', item=get_list)


@app.route('/gallery', methods=['GET','POST'])
def gallery():
    try:
        if request.method == 'POST':
            item = request.form['receiver']

            urlfile = f'static/css/products/{item}'
            img_list = list(os.listdir(urlfile))

            counter = len(img_list)
            
            if counter > 0:
                item_counter = True

        return render_template('gallery.html', paths=urlfile,
                                                img_count=item_counter, 
                                                imgs=img_list)
    
    except:
        no_imgs = "Sorry, there is no gallery for this item..."

        return render_template('gallery.html')


if __name__=='__main__':
    app.run(debug=True)