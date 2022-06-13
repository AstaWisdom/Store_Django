var updateBtns = document.getElementsByClassName('update_cart')

for (var i = 0;i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var itemId = this.dataset.item
        var action = this.dataset.action
        console.log('itemId:', itemId, 'action:', action)

        console.log('USER:', user)
        if(user == 'AnonymousUser'){
            console.log('Cart:', cart)
            addCookieItem(itemId, action)
        }else{
            console.log('Cart:', cart)
            updateUserOrder(itemId, action)
        }
    })
}


function addCookieItem(itemId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
	    console.log('Cart:', cart)
		if (cart[itemId] == null){
		cart[itemId] = {'quantity':1}

		}else {
			cart[itemId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[itemId]['quantity'] -= 1

		if (cart[itemId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[itemId];
		}
	}

	if (action == 'delete'){
	    cart[itemId]['quantity'] = 0
        console.log('Item should be deleted')
	    delete cart[itemId];
    }
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.reload()
}


function updateUserOrder(itemId, action){
    console.log('User is logged in sending data..')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'itemId': itemId, 'action': action}),
    })


    .then((response) =>{
        return response.json()
    })

    .then((data)=>{
        console.log('data:', data)
        location.reload()
    })
}