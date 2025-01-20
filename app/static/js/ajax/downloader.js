$("#btndonloeader").click(function() {


    csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    // Obtenemos el archivo seleccionado en el input de tipo file
    
    var consul=$("#idownloader").val();
    console.log(consul)

    

    // Creamos un objeto FormData y agregamos el archivo
    var datos = new FormData();
    datos.append("consul", consul);

    // Realizamos la solicitud AJAX para cargar el archivo
    $.ajax({
        url: "/downloader",  // La ruta del backend
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
             console.log(respuesta)   
                
            var status = respuesta["status"]
            if (status==1){

                
                console.log("descarga exitoso")
            }else{

                
                console.log("error al descargar el archivo")
            }
        }
    });
});
