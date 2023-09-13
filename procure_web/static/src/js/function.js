
odoo.define("scoring.FormFunction", function (require) {
    const core = require('web.core')
    secteur = $("#secteur");
    activities = $("#activity");
    secteur.change(()=> {
        console.log(secteur.val());
        activities.find('option')
                .remove()
                .end()
        $.ajax({
            url: "/scoring-request/getActivities",
            type: 'GET',
            data : {
                'secteur_id' :secteur.val()
            },
            dataType: 'json', //added data type
            success: function(res) {
                items = JSON.stringify(res);
                items_parsed = JSON.parse(items);
                for (var key in items_parsed) {
                    activities.append($('<option>', {
                        value: key,
                        text : items_parsed[key]
                    }));
                }},
            error : function(e){
                console.log(e)
                }
            });
        });

    buttonEl = $('.addBtn');
    submitBtnEl = $('.submit');
    quantityEl = $('#quantity');
    articleEl = $('#article');
    tbodyEl = $('tbody');
    achatsTotalEl = $('#achatsTotal');
    submitting = false;

    articleEl.change(()=>{
        quantityEl.val('1');
    })


    buttonEl.click(()=>{
        get_quantity = quantityEl.val();
        get_article = articleEl.val();
        console.log(get_article);
        $.ajax({
            url: "/scoring-request/addArticle",
            type: 'GET',
            data : {
                'article_id' :get_article,
                'quantity': get_quantity
            },
            dataType: 'json', //added data type
            success: function(res) {
                console.log(res);
                subtotal = parseInt(get_quantity) * parseInt(res.price);
                console.log(subtotal);
                button = '<button class="btn btn-secondary deleteBtn" onclick="SomeDeleteRowFunction(this);">'+"X"+'</button>' ;
                row = '<tr class="col-12"><td class="col-4">'+ res.name +'</td><td class="col-2">'+ get_quantity +'</td><td class="col-2">'+ res.price +'</td><td class="col-2">'+ subtotal +'</td>';
                row += '<td>'+ button +'</td></tr>' ;
                tbodyEl.append(row);
                quantityEl.val('1');
                achatsTotalEl.val(sumRows());
                },
            error : function(e){
                console.log(e)
                }
            });
        });

    submitBtnEl.click(()=>{
        submitting = true;
    });

    if(window.location.pathname == '/scoring-request'){
        console.info(performance.navigation.type);
        if (performance.navigation.type == performance.navigation.TYPE_RELOAD) {
              console.info( "This page is reloaded"+window.location.pathname );
              $.ajax({
                    url: "/scoring-request/deleteArticles",
                    type: 'GET',
                    data : {
                    },
                    dataType: 'json', //added data type
                    success: function(res) {
                        console.log(res);
                        },
                    error : function(e){
                        console.log(e)
                        }
                    });}
        else {
          console.info( "This page is not reloaded");
          $.ajax({
                    url: "/scoring-request/deleteArticles",
                    type: 'GET',
                    data : {
                    },
                    dataType: 'json', //added data type
                    success: function(res) {
                        console.log(res);
                        },
                    error : function(e){
                        console.log(e)
                        }
                    });
        }
    }




    /**console.log($ ("#secteur option:selected").text ());
    console.log($ ("#secteur").val());
    console.log($ ('select[name="secteur"]').val());**/
});

function SomeDeleteRowFunction(deleteBtn) {
    btn = $(deleteBtn);
    cells = btn.closest("tr").find('td');
    $.ajax({
            url: "/scoring-request/deleteArticle",
            type: 'GET',
            data : {'article': cells[0].innerHTML,
                    'quantity': cells[1].innerHTML,
                    'price':cells[2].innerHTML,
                    'subtotal':cells[3].innerHTML,
            },
            dataType: 'json', //added data type
            success: function(res) {
                console.log(res);
                alert('L`article a été supprimer avec succès')
                achatsTotalEl.val(sumRows());
                },
            error : function(e){
                console.log(e)
                }
            });
    btn.closest("tr").remove();
}

function sumRows() {
        var totalRowCount = 0;
        var rowCount = 0;
        var table = document.getElementById("articles");
        var rows = table.getElementsByTagName("tr")
        for (var i = 0; i < rows.length; i++) {
            totalRowCount++;
            var cells = rows[i].getElementsByTagName("td");
            if (cells.length > 0) {
                rowCount = rowCount +parseInt(cells[3].innerHTML);
            }
        }
        console.log(rowCount);
        return rowCount;
    }

