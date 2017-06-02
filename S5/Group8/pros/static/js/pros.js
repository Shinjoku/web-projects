$(document).ready(function(){
    $('#cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('#cep').mask('00000-000');
    $('#insc_estadual').mask('000.000.000.000');
    $('#tel').mask('(00) 0000-0000');
    $('#ramal').mask('0000');
    //$('#valor').mask('000.000.000,00', {reverse: true});
    $('#data_aprovado').mask('00/00/0000');
    $('#data_liberacao').mask('00/00/0000');
    $('#data_envio').mask('00/00/0000');
    $('input#cel').focusout(function(){
		var phone, element;
		element = $(this);
		element.unmask();
		phone = element.val().replace(/\D/g, '');
		if(phone.length > 10) {
			element.mask("(99) 99999-99999");
		} else {
			element.mask("(99) 9999-99999");
		}
	}).trigger('focusout');

	$('.remove-empresa').click(function(){
	    $('div.modal-body').empty();
	    var id = $(this).data('id')
	    var name = $(this).data('name')
        $('div.modal-body').append('Deseja apagar a empresa: <strong>' + name + '</strong>?');
        $('a.btn-yes').attr('href', 'delete_empresa/' + id + '/');
    });

	$('.remove-client').click(function(){
	    $('div.modal-body').empty();
	    var id = $(this).data('id')
	    var name = $(this).data('name')
        $('div.modal-body').append('Deseja apagar o cliente: <strong>' + name + '</strong>?');
        $('a.btn-yes').attr('href', 'delete_cliente/' + id + '/');
    });
    
    $('.remove-ordem').click(function(){
	    $('div.modal-body').empty();
	    var id = $(this).data('id')
	    var num = $(this).data('num_pedido')
        $('div.modal-body').append('Deseja apagar a ordem: <strong>' + num + '</strong>?');
        $('a.btn-yes').attr('href', 'delete_ordem/' + id + '/');
    });

    $("#select1").change(function() {
      if ($(this).data('options') === undefined) {
        /*Taking an array of all options-2 and kind of embedding it on the select1*/
        $(this).data('options', $('#select2 option').clone());
      }
      var id = $(this).val();
      var options = $(this).data('options').filter('[value=' + id + ']');
      $('#select2').html(options);
    });

    $('#select1').change(function() {
        $('#select2').prop('disabled', false);
    });

});

