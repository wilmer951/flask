$("#btnloadfile").click(function() {

    $('.divanalytic').css('display','none');
    $('.divdonloader').css('display','none');

    csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    // Obtenemos el archivo seleccionado en el input de tipo file
    var file = $('#file')[0].files;  // Usamos [0] para obtener el primer archivo (en caso de que se seleccione más de uno)
    

    if (file.length === 0) {
        // Verificar si no hay archivo seleccionado
        $("#idmsgalert").html('No ha seleccionado ningun archivo');
        $('#modalalert').modal('show');
    }


    // Creamos un objeto FormData y agregamos el archivo
    var datos = new FormData();
    datos.append("file", file[0]);

    // Realizamos la solicitud AJAX para cargar el archivo
    $.ajax({
        url: "/upload",  // La ruta del backend
        method: "POST",      // Método POST
        data: datos,         // Datos que se envían (el archivo en este caso)
        cache: false,
        dataType: 'json',    // Esperamos una respuesta JSON
        contentType: false,  // No necesitamos establecer el tipo de contenido, ya que estamos enviando un FormData
        processData: false,  // No procesamos los datos, dejamos que FormData se encargue
        headers: {
            'X-CSRFToken': csrf_token  // Enviar el token en el encabezado
        },
        success: function(respuesta) {
            
            $("#file").val('');  // Establecemos el valor a vacío, limpiando la selección del archivo
            var status = respuesta["status"]
            if (status==1){

               
                $('.divanalytic').css('display','block');

                $("#idmsgalert").html('Se cargo de forma exitosa el archivo');
                $('#modalalert').modal('show');
                

            }else{

                $('.divanalytic').css('display','none');
                $('.divdonloader').css('display','none');


                $("#idmsgalert").html('El archivo no es valido, solo se permite archivos EXCEl xls o xlsx');
                $('#modalalert').modal('show');
                
                
            }
        }
    });
});
