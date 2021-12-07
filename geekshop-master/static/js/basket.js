window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        // console.log(t_href.name); // идентификатор корзины
        // console.log(t_href.value); // количество в корзине (актуальное)

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/', // Этот адрес важен!
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });

        event.preventDefault();
    })
}
