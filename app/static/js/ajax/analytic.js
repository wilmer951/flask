$("#btnanalyticfile").click(function() {

    csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    // Obtenemos el archivo seleccionado en el input de tipo file
    
    var consul="ok"
    

    // Creamos un objeto FormData y agregamos el archivo
    var datos = new FormData();
    datos.append("consul", consul);

    // Realizamos la solicitud AJAX para cargar el archivo
    $.ajax({
        url: "/analytic",  // La ruta del backend
        method: "POST",      // Método POST
        data: datos,         // Datos que se envían (el archivo en este caso)
        cache: false,
        dataType: 'json',    // Esperamos una respuesta JSON
        contentType: false,  // No necesitamos establecer el tipo de contenido, ya que estamos enviando un FormData
        processData: false,  // No procesamos los datos, dejamos que FormData se encargue
        headers: {
            'X-CSRFToken': csrf_token  // Enviar el token en el encabezado
        },
        beforeSend: function() {
            // Aquí puedes ejecutar una acción antes de que se envíe la solicitud
            
            // Mostrar un spinner o mensaje de carga si no se mostró antes

            
            $('#btnclosettop').toggle();
            $('#btnclosemodal').toggle();
            $("#idmsgalert").html('Analizando archivo porfavor espere.');
            $('#modalalert').modal('show');
        },
        success: function(respuesta) {
            
            
            var status = respuesta["status"]
            if (status==1){

                $('#btnclosemodal').show();
                $('.divdonloader').css('display','block');
                $("#idmsgalert").html('<p>Analisis exitoso.<p><p>Puede descargar el archivo</p>');
            }else{

                $('.divdonloader').css('display','none');
                $("#idmsgalert").html('El archivo presenta errores.');
            }
        }
    });
});
