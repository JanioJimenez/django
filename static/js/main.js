
$('.campo').on('click', function (e) {
    console.log('maquina');
    $(this).css("font-family", "dubai");
    $(this).css("font-weight", "600");
});



$('#perfil').on('click', function (e) {
    console.log('maquina');
    window.location.href = 'perfil';
});


$('#code').on('click', function (e) {
    console.log('maquina');
    window.location.href = 'editor';
});

$('#cerrar').on('click', function (e) {
    console.log('maquina');
    window.location.href = 'http://localhost:8000/';
});


